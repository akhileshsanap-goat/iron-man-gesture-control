import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self, max_hands=1, detection_confidence=0.7, tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
        )
        self.mp_draw = mp.solutions.drawing_utils

    def process_frame(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        annotated = frame.copy()
        hand_landmarks = []

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    annotated,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_draw.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                    self.mp_draw.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
                )

                lm_list = []
                for lm in hand.landmark:
                    x = int(lm.x * frame.shape[1])
                    y = int(lm.y * frame.shape[0])
                    lm_list.append((x, y))
                hand_landmarks.append(lm_list)

        return annotated, hand_landmarks

    def close(self):
        self.hands.close()
