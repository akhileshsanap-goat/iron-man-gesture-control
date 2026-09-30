import time

import cv2
import pyautogui

from config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT, WINDOW_NAME
from gesture_controller import GestureController
from hand_tracker import HandTracker
from ui_overlay import draw_hud


pyautogui.FAILSAFE = False


def main():
    screen_width, screen_height = pyautogui.size()
    controller = GestureController(screen_width, screen_height)
    tracker = HandTracker()

    cap = cv2.VideoCapture(CAMERA_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    if not cap.isOpened():
        raise RuntimeError("Could not access the webcam. Check that it is connected and available.")

    last_fps_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        annotated, hand_landmarks_list = tracker.process_frame(frame)

        if hand_landmarks_list:
            detected = controller.detect(hand_landmarks_list[0])
            gesture_name = detected.get("gesture", "idle")
            pointer = detected.get("pointer")

            if pointer is not None:
                target_x = int((pointer[0] / frame.shape[1]) * screen_width)
                target_y = int((pointer[1] / frame.shape[0]) * screen_height)
                pyautogui.moveTo(target_x, target_y, duration=0.02)

            if controller.should_click(gesture_name):
                pyautogui.click()

            if controller.should_scroll(gesture_name):
                pyautogui.scroll(-30)
        else:
            gesture_name = "idle"
            pointer = None

        annotated = draw_hud(annotated, gesture_name, pointer)

        current_time = time.time()
        fps = 1.0 / max(current_time - last_fps_time, 0.0001)
        last_fps_time = current_time
        cv2.putText(
            annotated,
            f"FPS: {int(fps)}",
            (annotated.shape[1] - 135, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2,
        )

        cv2.imshow(WINDOW_NAME, annotated)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    tracker.close()


if __name__ == "__main__":
    main()
