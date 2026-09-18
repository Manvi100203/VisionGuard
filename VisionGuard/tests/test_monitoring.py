from src.monitoring.monitor import MonitoringEngine


def test_monitoring_initializes():
    engine = MonitoringEngine({
        "log_events": False,
        "unknown_face_alert": False,
    })
    assert engine.fps == 0.0
