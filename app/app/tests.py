"""SimpleTestCase - No integration with database"""

from django.test import SimpleTestCase

from app.calc import Calculator


class AvailableDays(SimpleTestCase):

    def test_1(self):
        datasets = [
            (5, 10),
            (2.1, 8.9),
            (2.5, 1),
        ]
        expected_results = [15.0, 11.0, 3.5]

        for dataset, expected in zip(datasets, expected_results):
            result = Calculator.add(dataset[0], dataset[1])
            self.assertEqual(expected, result)

    def test_2(self):
        datasets = [
            (15, 10),
            (8.8, 5.5),
            (2.5, 1),
        ]
        expected_results = [5.0, 3.3, 1.5]

        for dataset, expected in zip(datasets, expected_results):
            result = Calculator.subtract(dataset[0], dataset[1])
            self.assertEqual(expected, result)
