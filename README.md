
An example of "Hello, World!" in Python that uses `arparse` to satisfy the following requirements:

* If a name is passed in, we'd like it to replace "World" with the name.
    * ex: `python hello.py Brian` should print `"Hello, Brian!"`
* If someone passes in `-g` or `--goodbye`, "Hello" should be replaced with "Goodbye".
    * ex: `python hello.py -g Brian` should print `"Goodbye, Brian!"`

<!--
This goes along with 
* a blog post: [Testing argparse Applications]()
* a podcast episode: [209: Testing argparse Applications]()
-->


Example test run, with `pytest`, `coverage`, and `pytest-cov` installed:

```shell
$ pytest test_hello.py --cov=hello --cov-branch -v 
=============================== test session starts ================================
collected 17 items                                                                 

test_hello.py::test_shlex PASSED                                             [  5%]
test_hello.py::test_main[-Hello, World!] PASSED                              [ 11%]
test_hello.py::test_main[Okken-Hello, Okken!] PASSED                         [ 17%]
test_hello.py::test_main[-g-Goodbye, World!] PASSED                          [ 23%]
test_hello.py::test_main[--goodbye-Goodbye, World!] PASSED                   [ 29%]
test_hello.py::test_main[Okken -g-Goodbye, Okken!] PASSED                    [ 35%]
test_hello.py::test_app[-Hello, World!] PASSED                               [ 41%]
test_hello.py::test_app[Okken-Hello, Okken!] PASSED                          [ 47%]
test_hello.py::test_app[-g-Goodbye, World!] PASSED                           [ 52%]
test_hello.py::test_app[--goodbye-Goodbye, World!] PASSED                    [ 58%]
test_hello.py::test_app[Okken -g-Goodbye, Okken!] PASSED                     [ 64%]
test_hello.py::test_parse_args[-False-False-World] PASSED                    [ 70%]
test_hello.py::test_parse_args[-d-True-False-World] PASSED                   [ 76%]
test_hello.py::test_parse_args[-g-False-True-World] PASSED                   [ 82%]
test_hello.py::test_parse_args[Name-False-False-Name] PASSED                 [ 88%]
test_hello.py::test_parse_args[-d -g Earth-True-True-Earth] PASSED           [ 94%]
test_hello.py::test_parse_args[--goodbye-False-True-World] PASSED            [100%]

---------- coverage: platform darwin, python 3.11.6-final-0 ----------
Name       Stmts   Miss Branch BrPart  Cover
--------------------------------------------
hello.py      15      0      4      0   100%
--------------------------------------------
TOTAL         15      0      4      0   100%

================================ 17 passed in 0.80s ================================
```
