import cv2


def draw_results(frame, faces, recognitions, objects, fps):
    output = frame.copy()

    for (x, y, w, h) in faces:
        cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)

    for item in recognitions:
        x, y, w, h = item["box"]
        label = item["name"]
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            output,
            label,
            (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )

    for item in objects:
        x1, y1, x2, y2 = item["box"]
        label = f"{item['label']} {item['confidence']:.2f}"
        cv2.rectangle(output, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(
            output,
            label,
            (x1, max(y1 - 8, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (0, 0, 255),
            2,
        )

    cv2.putText(
        output,
        f"FPS: {fps:.1f}",
        (15, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2,
    )

    return output
