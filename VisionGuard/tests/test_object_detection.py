def test_detection_result_schema():
    result = {
        "box": (0, 0, 10, 10),
        "label": "person",
        "confidence": 0.9,
    }
    assert set(result) == {"box", "label", "confidence"}
