def unknown_face_alert(recognitions):
    return any(item["name"] == "Unknown" for item in recognitions)
