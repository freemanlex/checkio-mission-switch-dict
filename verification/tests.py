"""
TESTS is a dict with all of your tests.
Keys for this will be the categories" names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it"s used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [{"rouses": "red", "car": "red", "sky": "blue"}],
            "answer": {"red": {"rouses", "car"}, "blue": {"sky"}},
        },
        {
            "input": [{1: 1, 2: 2, 3: 3, 4: 4}],
            "answer": {"1": {"1"}, "2": {"2"}, "3": {"3"}, "4": {"4"}},
        }
    ],
    "Extra": [
        {
            "input": [{"a": "b", "b": "c", "c": "a"}],
            "answer": {"b": {"a"}, "c": {"b"}, "a": {"c"}},
        },
        {
            "input": [{"": "", "a": "", "b": "", "c": ""}],
            "answer": {"": {"", "a", "b", "c"}},
        },
        {
            "input": [{2: 2, "2": 2}],
            "answer": {"2": {"2"}},
        },
        {
            "input": [{0: "zero"}],
            "answer": {"zero": {"0"}},
        },
        {
            "input": [{2: "number", 1: "bool", "text": "string", "3": "string", 100.0: "number"}],
            "answer": {"number": {"2", "100.0"}, "bool": {"1"}, "string": {"3", "text"}},
        },
        {
            "input": [{1: "number", 2: "number", 3: "number"}],
            "answer": {"number": {"1", "2", "3"}},
        }
    ]
}
