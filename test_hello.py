import subprocess
import pytest
import shlex
from hello import parse_args, main

def test_shlex():
    # I want to write this
    command = '-d -g Brian'

    # command parsers want this
    as_list = ['-d', '-g', 'Brian']

    # shlex.split() does the work for me
    assert shlex.split(command) == as_list


test_cases = [
    ("", "Hello, World!"),  # no args
    ("Okken", "Hello, Okken!"),  # one arg
    ("-g", "Goodbye, World!"),  # the other arg
    ("--goodbye", "Goodbye, World!"),  # long form
    ("Okken -g", "Goodbye, Okken!"),  # both args
]

@pytest.mark.parametrize('command, expected_output', test_cases)
def test_main(capsys, command, expected_output):
    main(shlex.split(command))
    output = capsys.readouterr().out.rstrip()
    assert output == expected_output


@pytest.mark.parametrize('command, expected_output', test_cases)
def test_app(command, expected_output):
    full_command = ["python", "hello.py"] + shlex.split(command)
    result = subprocess.run(full_command,
                            capture_output=True, text=True)
    output = result.stdout.rstrip()
    assert output == expected_output


@pytest.mark.parametrize(
    'command, debug, goodbye, name',
    [
        # no params
        ("", False, False, 'World'),
        # each param
        ("-d", True, False, 'World'),
        ("-g", False, True, 'World'),
        ("Name", False, False, 'Name'),
        # all params
        ("-d -g Earth", True, True, 'Earth'),
        # long form
        ("--goodbye", False, True, 'World'),

    ])
def test_parse_args(command, debug, goodbye, name):
    args = parse_args(shlex.split(command))

    # combine test into in one assert
    assert ((args.debug, args.goodbye, args.name) ==
            (debug, goodbye, name))

    # or split them up, either works
    assert args.debug == debug
    assert args.goodbye == goodbye
    assert args.name == name

