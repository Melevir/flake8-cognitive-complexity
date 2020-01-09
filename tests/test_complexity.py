from conftest import run_validator_for_test_file


def test_fails():
    errors = run_validator_for_test_file('complex_functions.py', max_cognitive_complexity=3)
    assert len(errors) == 1
