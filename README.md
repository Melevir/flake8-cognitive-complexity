# flake8-cognitive-complexity

[![Build Status](https://travis-ci.org/Melevir/flake8-cognitive-complexity.svg?branch=master)](https://travis-ci.org/Melevir/flake8-cognitive-complexity)
[![Maintainability](https://api.codeclimate.com/v1/badges/579738d149e489c631a6/maintainability)](https://codeclimate.com/github/Melevir/flake8-cognitive-complexity/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/579738d149e489c631a6/test_coverage)](https://codeclimate.com/github/Melevir/flake8-cognitive-complexity/test_coverage)
[![PyPI version](https://badge.fury.io/py/flake8-cognitive-complexity.svg)](https://badge.fury.io/py/flake8-cognitive-complexity)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-cognitive-complexity)

An extension for flake8 that validates cognitive functions complexity.

Cognitive complexity is analog of cyclomatic complexity, that measure
how difficult to understand piece of code. Introduced by [G. Ann Campbell](https://github.com/ganncamp)
and currently used by SonarSource, CodeClimate and others.
You can find more readings about cognitive complexity in
[cognitive-complexity readme file](https://github.com/Melevir/cognitive_complexity/blob/master/README.md#what-is-cognitive-complexity).

Default complexity is 7, can be configured via `--max-cognitive-complexity` option.

## Installation

```terminal
pip install flake8-cognitive-complexity
```

## Example

```python
def f(a, b):
    if a:
        for i in range(b):
            if b:
                return 1
```

Usage:

```terminal
$ flake8 --max-cognitive-complexity=3 test.py
text.py:1:5: CCR001 Cognitive complexity is too high (6 > 3)
```

Tested on Python 3.7.x and flake8 3.7.8.

## Error codes

| Error code |                     Description          |
|:----------:|:----------------------------------------:|
|   CCR001   | Cognitive complexity is too high (X > Y) |
