# flake8-expression-complexity


An extension for flake8 that validates cognitive functions complexity.

Cognitive complexity is analog of cyclomatic complexity, that measure
how difficult to understand piece of code. Introduced by [G. Ann Campbell](https://github.com/ganncamp)
and currently used by SonarSource, CodeClimate and others.
You can find more readings about cognitive complexity in
[cognitive-complexity readme file](https://github.com/Melevir/cognitive_complexity/blob/master/README.md#what-is-cognitive-complexity).



## Installation

    pip install flake8-cognitive-complexity


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
