import ast
from typing import Generator, Tuple

from cognitive_complexity.api import get_cognitive_complexity

from flake8_cognitive_complexity import __version__ as version


class CognitiveComplexityChecker:
    DEFAULT_MAX_COGNITIVE_COMPLEXITY = 7

    name = 'flake8-cognitive-complexity'
    version = version

    max_cognitive_complexity = DEFAULT_MAX_COGNITIVE_COMPLEXITY

    def __init__(self, tree, filename: str):
        self.filename = filename
        self.tree = tree

    @classmethod
    def add_options(cls, parser) -> None:
        parser.add_option(
            '--max-cognitive-complexity',
            type=int,
            default=cls.DEFAULT_MAX_COGNITIVE_COMPLEXITY,
            parse_from_config=True,
        )

    @classmethod
    def parse_options(cls, options) -> None:
        cls.max_cognitive_complexity = int(options.max_cognitive_complexity)

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        funcdefs = (
            n for n in ast.walk(self.tree)
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        )
        for funcdef in funcdefs:
            complexity = get_cognitive_complexity(funcdef)
            if complexity > self.max_cognitive_complexity:
                yield (
                    funcdef.lineno,
                    funcdef.col_offset,
                    f'CCR001 Cognitive complexity is too high '
                    f'({complexity} > {self.max_cognitive_complexity})',
                    type(self),
                )
