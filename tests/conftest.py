import ast
import os

from flake8_cognitive_complexity.checker import CognitiveComplexityChecker


def run_validator_for_test_file(
    filename: str,
    max_cognitive_complexity: int = None,
    ignore_django_orm_queries: bool = True,
):
    test_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_files',
        filename,
    )
    with open(test_file_path, 'r') as file_handler:
        raw_content = file_handler.read()
    tree = ast.parse(raw_content)
    checker = CognitiveComplexityChecker(tree=tree, filename=filename)
    if max_cognitive_complexity:
        checker.max_cognitive_complexity = max_cognitive_complexity

    return list(checker.run())
