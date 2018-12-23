import unittest
from scenario_script import scenario_1, scenario_2


class TestSearchInYandex(unittest.TestCase):

    def test_search_in_ya(self):
        self.assertTrue(scenario_1())

    def test_run_images(self):
        self.assertTrue(scenario_2())


if __name__ == '__main__':

    unittest.main()
