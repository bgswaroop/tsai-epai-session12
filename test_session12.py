import inspect
import re
import os

import calculator
from calculator import derivatives


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add at least 200 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(calculator, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_cos():
    """
    Test the method cos in the calculator package
    :return: None
    """
    output = calculator.cos(0)
    assert output == 1
    output = derivatives.derivative_cos(0)
    assert output == 0


def test_exp():
    """
    Test the method exp in the calculator package
    :return: None
    """
    output = calculator.exp(0)
    assert output == 1
    output = derivatives.derivative_exp(0)
    assert output == 1


def test_log():
    """
    Test the method log in the calculator package
    :return: None
    """
    output = calculator.log(1)
    assert output == 0
    output = derivatives.derivative_log(1)
    assert output == 1


def test_relu():
    """
    Test the method relu in the calculator package
    :return: None
    """
    output = calculator.relu(0)
    assert output == 0
    output = derivatives.derivative_relu(0)
    assert output == 0


def test_sigmoid():
    """
    Test the method sigmoid in the calculator package
    :return: None
    """
    output = calculator.sigmoid(0)
    assert output == 0.5
    output = derivatives.derivative_sigmoid(0)
    assert output == 0.25


def test_sin():
    """
    Test the method sin in the calculator package
    :return: None
    """
    output = calculator.sin(0)
    assert output == 0
    output = derivatives.derivative_sin(0)
    assert output == 1


def test_softmax():
    """
    Test the method softmax in the calculator package
    :return: None
    """
    output = calculator.softmax([1, 2, 3])
    assert output == [0.033120396946264216, 0.06624079389252843, 0.09936119083879263]
    output = derivatives.derivative_softmax([1, 2],  [1, 1])
    assert output == [-1, 0]


def test_tan():
    """
    Test the method tan in the calculator package
    :return: None
    """
    output = calculator.tan(0)
    assert output == 0
    output = derivatives.derivative_tan(0)
    assert output == 1


def test_tanh():
    """
    Test the method tanh in the calculator package
    :return: None
    """
    output = calculator.tanh(0)
    assert output == 0
    output = derivatives.derivative_tanh(0)
    assert output == 1
