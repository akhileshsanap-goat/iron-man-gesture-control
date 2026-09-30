import time


class GestureController:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.last_click_time = 0
        self.last_scroll_time = 0

    def _distance(self, a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    def _is_extended(self, landmarks, tip_index, pip_index):
        tip = landmarks[tip_index]
        pip = landmarks[pip_index]
        return tip[1] < pip[1]

    def detect(self, hand_landmarks):
        if not hand_landmarks:
            return {"gesture": "idle", "pointer": None}

        hand = hand_landmarks

        thumb_tip = hand[4]
        index_tip = hand[8]
        middle_tip = hand[12]
        ring_tip = hand[16]
        pinky_tip = hand[20]

        finger_states = {
            "thumb": self._is_extended(hand, 4, 2),
            "index": self._is_extended(hand, 8, 6),
            "middle": self._is_extended(hand, 12, 10),
            "ring": self._is_extended(hand, 16, 14),
            "pinky": self._is_extended(hand, 20, 18),
        }

        pointer = index_tip
        finger_count = sum(1 for state in finger_states.values() if state)

        # Pointer mode: only index finger extended
        if finger_states["index"] and not finger_states["middle"] and not finger_states["ring"] and not finger_states["pinky"]:
            return {"gesture": "pointer", "pointer": pointer, "finger_count": finger_count}

        # Open palm: several fingers extended
        if finger_count >= 4:
            return {"gesture": "open_palm", "pointer": pointer, "finger_count": finger_count}

        # Fist: all fingers folded
        if not any(finger_states.values()):
            return {"gesture": "fist", "pointer": pointer, "finger_count": finger_count}

        # Pinch: thumb and index close together
        if finger_states["thumb"] and finger_states["index"]:
            pinch_distance = self._distance(thumb_tip, index_tip)
            if pinch_distance < 45:
                return {"gesture": "pinch", "pointer": pointer, "finger_count": finger_count}

        return {"gesture": "idle", "pointer": pointer, "finger_count": finger_count}

    def should_click(self, gesture_name):
        now = time.time()
        if gesture_name == "fist" and now - self.last_click_time > 0.45:
            self.last_click_time = now
            return True
        return False

    def should_scroll(self, gesture_name):
        now = time.time()
        if gesture_name == "pinch" and now - self.last_scroll_time > 0.30:
            self.last_scroll_time = now
            return True
        return False
