import unittest

from report import remove_none_values
from report import sort_pages

class Tests(unittest.TestCase):
    def test_remove_none_values(self):
        self.assertEqual({}, remove_none_values({"1": None}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1", "2": None}))
        self.assertEqual({}, remove_none_values({}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1"}))

    def test_sorted_dict(self):
        self.assertEqual([('first', 45), ('second', 25), ('third', 15)], sort_pages({"first": 45, "third": 15, "second": 25}))
        self.assertEqual([('first', 45), ('second', 25), ('third', 15)], sort_pages({"third": 15, "first": 45, "second": 25}))
        self.assertEqual(
            [("0", 45), ("1", 35), ("2", 25), ("3", 0)],
            sort_pages({"3": 0, "1": 35, "2": 25, "0": 45}),
        )
        self.assertEqual(
            [("0", 3), ("1", 2), ("2", 1), ("3", 0)],
            sort_pages({"3": 0, "1": 2, "2": 1, "0": 3}),
        )
        self.assertEqual(
            [],
            sort_pages({}),
        )

if __name__ == "__main__":
    unittest.main()