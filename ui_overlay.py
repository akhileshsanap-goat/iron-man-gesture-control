import cv2


def draw_hud(frame, gesture_name, pointer=None):
    overlay = frame.copy()
    height, width, _ = overlay.shape

    cv2.rectangle(overlay, (20, 20), (420, 90), (0, 0, 0), -1)
    cv2.rectangle(overlay, (20, 20), (420, 90), (0, 255, 255), 2)
    cv2.putText(
        overlay,
        f"Gesture: {gesture_name}",
        (35, 55),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2,
    )

    if pointer is not None:
        x, y = pointer
        cv2.line(overlay, (x - 12, y), (x + 12, y), (0, 255, 255), 2)
        cv2.line(overlay, (x, y - 12), (x, y + 12), (0, 255, 255), 2)

    cv2.line(overlay, (0, int(height * 0.18)), (width, int(height * 0.18)), (0, 255, 255), 1)
    cv2.line(overlay, (0, int(height * 0.82)), (width, int(height * 0.82)), (0, 255, 255), 1)

    return overlay
