def draw_bounding_box(image, bbox, label, color=(0, 255, 0), thickness=2):
    x1, y1, x2, y2 = bbox
    cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)
    return image

def draw_detections(image, detections):
    for detection in detections:
        bbox = detection['bbox']
        label = detection['label']
        image = draw_bounding_box(image, bbox, label)
    return image