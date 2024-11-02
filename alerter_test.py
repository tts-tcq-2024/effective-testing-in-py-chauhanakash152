import unittest
from alerter import alert_in_celcius

class TestAlerter(unittest.TestCase):
    def setUp(self):
        global alert_failure_count
        alert_failure_count = 0  # Reset count before each test

    def test_alert_below_threshold(self):
        """Test alert behavior below threshold with a successful alert."""
        alert_in_celcius(30)  # Should not cause alert_failure_count increment
        self.assertEqual(alert_failure_count, 0)

    def test_alert_above_threshold_successful(self):
        """Test alert behavior above threshold with a successful alert (200)."""
        alert_in_celcius(400.5)  # Stub returns 200, no increment expected
        self.assertEqual(alert_failure_count, 0)

    def test_alert_failure_count_increment(self):
        """Test alert failure count increments on non-200 response."""
        # Override the stub to simulate a failure response
        def network_alert_stub_failure(celcius):
            print(f'ALERT: Temperature is {celcius} celcius')
            return 500  # Simulate network failure
        
        global network_alert_stub
        original_stub = network_alert_stub
        network_alert_stub = network_alert_stub_failure  # Temporarily override

        alert_in_celcius(400.5)
        self.assertEqual(alert_failure_count, 1)  # Expected increment on failure

        # Restore the original stub after the test
        network_alert_stub = original_stub

if __name__ == '__main__':
    unittest.main()