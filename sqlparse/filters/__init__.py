# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Andi Albrecht, albrecht.andi@gmail.com
#
# This module is part of python-sqlparse and is released under
# the BSD License: https://opensource.org/licenses/BSD-3-Clause

from sqlparse.filters.others import SerializerUnicode
from sqlparse.filters.others import StripCommentsFilter
from sqlparse.filters.others import StripWhitespaceFilter
from sqlparse.filters.others import SpacesAroundOperatorsFilter

from sqlparse.filters.output import OutputPHPFilter
from sqlparse.filters.output import OutputPythonFilter

from sqlparse.filters.tokens import KeywordCaseFilter
from sqlparse.filters.tokens import IdentifierCaseFilter
from sqlparse.filters.tokens import TruncateStringFilter

from sqlparse.filters.reindent import ReindentFilter
from sqlparse.filters.right_margin import RightMarginFilter
from sqlparse.filters.aligned_indent import AlignedIndentFilter

__all__ = [
    'SerializerUnicode',
    'StripCommentsFilter',
    'StripWhitespaceFilter',
    'SpacesAroundOperatorsFilter',

    'OutputPHPFilter',
    'OutputPythonFilter',

    'KeywordCaseFilter',
    'IdentifierCaseFilter',
    'TruncateStringFilter',

    'ReindentFilter',
    'RightMarginFilter',
    'AlignedIndentFilter',
]

# 这样的目录结构实际上是方便代码的拆分的，将逻辑全部分散到各个专用的代码中去，然后在上一层的 __init__.py 中引用过来，结构更加清晰
