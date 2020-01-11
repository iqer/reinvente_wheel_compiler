#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Analysis Class File
"""
KEYWORD_SET = set(
    'if', 'when', 'elsif', 'while', 'until', 'begin', 'for', 'do', 'try',
    'catch', 'finally', 'end', 'def', 'var', 'this', 'null', 'throw', 'break',
    'continue', 'return', 'operator'
)


class AnalysisType():
    """
    Enum of all type supported
    """

    keyword = 'keyword'
    number = 'number'
    identifier = 'identifier'
    sign = 'sign'
    annotation = 'annotation'
    string = 'string'
    regex = 'regex'
    space = 'space'
    newline = 'newline'
    endsymbol = 'endsymbol'


class Token():
    """
    Token type and value
    """

    def __init__(self, v_type, value):
        if v_type == AnalysisType.identifier:
            first_char = value[0]
            if '0' <= first_char <= '9':
                v_type = AnalysisType.number
            elif value in KEYWORD_SET:
                v_type = AnalysisType.keyword
        elif v_type == AnalysisType.annotation:
            value = value[1:]
        elif v_type == AnalysisType.string:
            value = value[1:-1]
        elif v_type == AnalysisType.regex:
            value = value[1:-1]
        elif v_type == AnalysisType.endsymbol:
            value = None
        self.v_type = v_type
        self.value = value
