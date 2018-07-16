# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Andi Albrecht, albrecht.andi@gmail.com
#
# This module is part of python-sqlparse and is released under
# the BSD License: https://opensource.org/licenses/BSD-3-Clause

"""filter"""

from sqlparse import lexer
from sqlparse.engine import grouping
from sqlparse.engine.statement_splitter import StatementSplitter

# FileerStack 类
class FilterStack(object):

    # python 中的构造方法
    def __init__(self):
        self.preprocess = []            # 前处理
        self.stmtprocess = []           # 过程处理
        self.postprocess = []           # 后处理
        self._grouping = False

    def enable_grouping(self):
        self._grouping = True

    #
    def run(self, sql, encoding=None):
        stream = lexer.tokenize(sql, encoding)      # 通过词法分析器的分析，吐出一个流，其中信息均以(tokentype, value)的形式存在
        # Process token stream
        # 遍历前处理列表中的过滤器
        for filter_ in self.preprocess:
            stream = filter_.process(stream)    # 前处理的过滤器开始进行处理

        stream = StatementSplitter().process(stream)    # 整理前处理结果

        # Output: Stream processed Statements
        # 进行事中处理和后处理
        for stmt in stream:
            if self._grouping:
                stmt = grouping.group(stmt)

            for filter_ in self.stmtprocess:
                filter_.process(stmt)

            for filter_ in self.postprocess:
                stmt = filter_.process(stmt)

            yield stmt
