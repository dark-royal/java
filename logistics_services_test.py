from unittest import TestCase

import logistics_services


class TestLogisticService(TestCase):
    def test_that_collection_rate_is_less_than_50_percent(self):
        self.assertEqual(9000, logistics_services.services(45))
