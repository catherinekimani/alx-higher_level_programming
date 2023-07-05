#!/usr/bin/python3
# 5-text_indentation.py
""" Defines a function that prints a text"""


def text_indentation(text):
    """
    Prints a text with 2 new lines
    Args:
        text(str): input to be processed
    Raises:
    TypeError: If the text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for punc_marks in ".?:":
        text = (punc_marks + "\n\n").join(
            [line.strip(" ") for line in text.split(punc_marks)])

    print(f"{text}", end="")
