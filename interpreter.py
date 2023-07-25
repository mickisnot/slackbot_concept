"""
Interpreter Module

Interprets messages and calls t he appropriate functions to return to the slackbot

Functions:
    1. interpret_message(message): Interpret the message and return a response

Author: Ian Jackson
"""

import add  # TODO: figure out how to dynamically load and call module


def interpret_message(message):
    """
    Interprets the message and returns a response

    Parameters:
        message (string): The message to interpret

    Returns:
        string|None: The response to return, or None

    """
    args = message.split()
    if args[0] == "add":
        return add.add(args[1], args[2])

    if args[0] == "hi":
        return "hello"

    return None
