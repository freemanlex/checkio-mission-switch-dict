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
            "input": [{"1": "one", "2": "two", "3": "one", "4": "two"}],
            "answer": {"one": {"1", "3"}, "two": {"2", "4"}},
        },
        {
            "input": [{"a": "b", "b": "c", "c": "a"}],
            "answer": {"b": {"a"}, "c": {"b"}, "a": {"c"}},
        }
    ],
    "Extra": [
        {
            "input": [{"": "", "a": "", "b": "", "c": ""}],
            "answer": {"": {"", "a", "b", "c"}},
        },
        {
            "input": [{2: 2, "2": 2}],
            "answer": {"2": {"2"}},
        },
        {
            "input": [{"0": "zero"}],
            "answer": {"zero": {"0"}},
        },
        {
            "input": [{"True": "bool", "text": "string", "2": "string", "100.0": "number"}],
            "answer": {"string": {"text", "2"}, "bool": {"True"}, "number": {"100.0"}},
        },
        {
            "input": [{"1": "number", "2": "number", "3": "number"}],
            "answer": {"number": {"1", "2", "3"}},
        },
        {
            "input": [{"Mile": "student", "Jeff": "pupil", "Frank": "pupil"}],
            "answer": {"student": {"Mile"}, "pupil": {"Frank", "Jeff"}},
        }
    ]
}
