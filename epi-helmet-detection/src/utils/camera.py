def open_camera():
    import cv2

    cap = cv2.VideoCapture(0)  # Open the default camera

    if not cap.isOpened():
        raise Exception("Could not open video device")

    return cap


def read_frame(cap):
    ret, frame = cap.read()
    if not ret:
        raise Exception("Could not read frame from camera")
    return frame


def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()