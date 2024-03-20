from unittest import TestCase

import mr_chinedu_task


class Task(TestCase):

    def test_occurance_of_number_in_the_list(self):
        number = [2,3,3,5,6,7]
        expected = [2,3]
        self.assertEqual(expected,mr_chinedu_task.element_occurence(number))
