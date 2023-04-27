import unittest
from main import filter_unique_dicts


class TestFilterUniqueDictsFunction(unittest.TestCase):
    def test_unique_list(self) -> None:
        input_values: list[list[dict[str, (str, int)]]] = [
            [
                {},
                {"key1": "value1"},
                {"key2": "value2"},
                {"key3": "value3"},
                {"key1": 1},
                {"key2": 2},
                {"key3": 3},
            ],

            [
                {},
                {"key1": 1, "key2": 2, "key3": 3},
                {"key1": 3, "key2": 2, "key3": 1},
                {"key1": 2, "key2": 2, "key3": 2},
            ],

            [
                {},
                {"key1": "value1"},
                {"key1": "value1", "key2": "value2"},
                {"key1": "value1", "key2": "value2", "key3": "value3"}
            ]
        ]
        error_msg: str = "Функция filter_unique_dicts работает некорректно на уникальных входных списках"

        for input_value in input_values:
            with self.subTest(input_value=input_value):
                expected_result: list[dict[str, (str, int)]] = input_value
                actual_result: list[dict[str, (str, int)]] = filter_unique_dicts(list_dicts=input_value)
                self.assertEqual(first=expected_result, second=actual_result, msg=error_msg)

    def test_not_unique_list(self) -> None:
        input_values: list[list[dict[str, (str, int)]]] = [
            [
                {},
                {},
                {},
            ],

            [
                {"key1": "value1", "key2": "value2", "key3": "value3"},
                {"key3": "value3", "key2": "value2", "key1": "value1"},
                {"key2": "value2", "key3": "value3", "key1": "value1"}
            ],

            [
                {},
                {"key1": 1},
                {"key1": "value1"},
                {"key1": 1}
            ],

            [
                {"key1": "value1", "key2": 2},
                {"key1": 1, "key2": 2},
                {"key2": 2, "key1": 1}
            ]
        ]
        correct_result: list[list[dict[str, (str, int)]]] = [
            [
                {}
            ],

            [
                {"key1": "value1", "key2": "value2", "key3": "value3"}
            ],

            [
                {},
                {"key1": 1},
                {"key1": "value1"},
            ],

            [
                {"key1": "value1", "key2": 2},
                {"key1": 1, "key2": 2}
            ]
        ]
        error_msg: str = "Функция filter_unique_dicts работает некорректно на не уникальных входных списках"
        for index in range(len(input_values)):
            with self.subTest(input_value=input_values[index]):
                expected_result: list[dict[str, (str, int)]] = correct_result[index]
                actual_result: list[dict[str, (str, int)]] = filter_unique_dicts(list_dicts=input_values[index])
                self.assertEqual(first=expected_result, second=actual_result, msg=error_msg)

