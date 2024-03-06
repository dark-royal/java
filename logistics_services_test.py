from unittest import TestCase

import logistics_services


class TestLogisticsServices(TestCase):

    def test_collection_rate_is_less_than_50_percent(self):
        self.assertEqual(9000, logistics_services.services(25))

    def test_collection_rate_is_between_50_to_59_percent(self):
        self.assertEqual(16000,logistics_services.services(55))

    def test_collection_rate_is_between_60_to_69_percent(self):
        self.assertEqual(21750,logistics_services.services(67))

    def test_collection_rate_is_greater_than_or_equals_to_70(self):
        self.assertEqual(44000,logistics_services.services(78))
