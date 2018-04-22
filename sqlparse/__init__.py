# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Andi Albrecht, albrecht.andi@gmail.com
#
# This module is part of python-sqlparse and is released under
# the BSD License: https://opensource.org/licenses/BSD-3-Clause

"""Parse SQL statements."""

# Setup namespace


from sqlparse import sql                # sqlparse/sql.py
from sqlparse import cli                # sqlparse/cli.py
from sqlparse import engine             # sqlparse/engine/__init__.py
from sqlparse import tokens             # sqlparse/tokens.py
from sqlparse import filters            # sqlparse/filters/__init__.py
from sqlparse import formatter          # sqlparse/formatter.py
from sqlparse.compat import text_type   # sqlparse/compat.py

__version__ = '0.2.4'
__all__ = ['engine', 'filters', 'formatter', 'sql', 'tokens', 'cli']

# 从字符串类型的数据中，解析sql
def parse(sql, encoding=None):
    """Parse sql and return a list of statements.

    :param sql: A string containing one or more SQL statements.
    :param encoding: The encoding of the statement (optional).
    :returns: A tuple of :class:`~sqlparse.sql.Statement` instances.
    """
    # 不可变的有序集合，tuple
    return tuple(parsestream(sql, encoding))

# 流式读取文件，进行sql解析
def parsestream(stream, encoding=None):
    """Parses sql statements from file-like object.

    :param stream: A file-like object.
    :param encoding: The encoding of the stream contents (optional).
    :returns: A generator of :class:`~sqlparse.sql.Statement` instances.
    """
    stack = engine.FilterStack()
    stack.enable_grouping()
    return stack.run(stream, encoding)

# 根据设置，格式化 sql ，其中 options 是 key-value 形式的参数
def format(sql, encoding=None, **options):
    """Format *sql* according to *options*.

    Available options are documented in :ref:`formatting`.

    In addition to the formatting options this function accepts the
    keyword "encoding" which determines the encoding of the statement.

    :returns: The formatted SQL statement as string.
    """
    stack = engine.FilterStack()                                # 首先建立一个过滤器栈
    options = formatter.validate_options(options)               # 检查一遍所有传进来的参数是否符合枚举值的要求
    stack = formatter.build_filter_stack(stack, options)        # 设置 “过滤器栈” 中各个处理过程的值
    stack.postprocess.append(filters.SerializerUnicode())
    return u''.join(stack.run(sql, encoding))                   # 以 unicode 的编码格式
                                                                # 使用 ''(空字符) 将 stack.run 吐出的结果连起来
                                                                #


def split(sql, encoding=None):
    """Split *sql* into single statements.

    :param sql: A string containing one or more SQL statements.
    :param encoding: The encoding of the statement (optional).
    :returns: A list of strings.
    """
    stack = engine.FilterStack()
    return [text_type(stmt).strip() for stmt in stack.run(sql, encoding)]
