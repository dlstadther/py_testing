# py_testing

[dlstadther.github.io/py_testing/](https://dlstadther.github.io/py_testing/)

Experiment with various Python testing frameworks
* unit testing
    * unittest w/ nose2
    * pytest
* static testing / linting
    * flake8
    * pylint
    * mypy

Control execution with `tox`

## Examples

```shell
# run all tests
$ tox

# run all py37 unittests
$ tox -e py37-unittest

# run all py37 pytests
$ tox -e py37-pytest

# run pylint on pkg and tests
$ tox -e pylint

# run pylint on specific file
$ tox -e pylint tests/pytest/test_func.py

# run py37 and pylint, only
$ tox -e py37,pylint
```

## TODO
* increase complexity of tests
    * unit testing
        * add fixtures
        * add config `.ini`s
    * static testing / linting
        * add custom rules [example](https://github.com/PyCQA/pylint/blob/master/pylint/extensions/emptystring.py)
* support single function execution
* run tests inside docker
* setup within TravisCI


Sphinx Resources:
* 3 part usage/configuration of sphinx docs
* setup + basic customization - https://towardsdatascience.com/advanced-code-documentation-beyond-comments-and-docstrings-2cc5b2ace28a
* extensions + confluence hosting - https://towardsdatascience.com/advanced-code-documentation-with-sphinx-part-2-32c82860a535
* docstring coverage + unittest - https://towardsdatascience.com/advanced-code-documentation-with-coverage-and-unit-tests-part-3-3f7b698497fb
