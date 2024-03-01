from unittest import TestCase

import seven_segment_display1


class Test(TestCase):
    def test_segment_can_print_one(self):
        # first_display = '1'
        self.assertEqual("& & & & &", seven_segment_display1.first_display('1'))
