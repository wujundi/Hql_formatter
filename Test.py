import sqlparse as sqlparse
import unittest

class Test(unittest.TestCase):

    # 测试用sql
    str = "select * from db.tab where name= 'dad'"
    print('before')
    formatted_sql = sqlparse.format(str,
                                    keyword_case='upper',
                                    identifier_case = 'upper',
                                    strip_comments = False,
                                    indent_tabs = True,
                                    indent_width = '1',
                                    reindent = True)
    print('after')
    print(formatted_sql)

if __name__=="__main__":
  unittest.main()