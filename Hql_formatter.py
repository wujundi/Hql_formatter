import sublime, sublime_plugin

# 导入python系统模块
import sys 
# 导入python操作系统模块
import os

# 将后者加入到操作系统path变量中 | 返回该脚本的路径
sys.path.append(os.path.dirname(__file__)) 

# 首先识别Python版本，然后根据不同的版本导入对应的 sqlparse 模块
'''
if sys.version_info >= (3, 0):
    import sqlparse3 as sqlparse
else:
    import sqlparse2 as sqlparse
'''
# 尝试无差别导入
import sqlparse as sqlparse


# for ST2
settings = sublime.load_settings('SQL Beautifier.sublime-settings')

# for ST3
# 定义一个名叫 plugin_loaded 的函数
def plugin_loaded():
    #  定义一个全局变量（也就是可以跨函数使用的变量）
    global settings
    settings = sublime.load_settings('SQL Beautifier.sublime-settings')

# 定义一个叫 SqlBeautifierCommand 的类，继承自 sublime_plugin.TextCommand
# sublime_plugin.TextCommand 是文本编辑相关的基类，文本编辑相关的命令都继承于这个基类
class Hql_formatterCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")

    # 定义一个叫 format_sql 的函数 将 raw_sql 传进去
    # python稍稍傻逼的一点，在java中是可以随处调用this的，但是在python中，需要加入形参self，表示“当前实例的XXX”

    def format_sql(self, raw_sql):
        # 异常处理，捕获可能出现的异常，并打印处理出来，和 Java try catch 一样一样的
        try:
            # 调用 sqlparse 模块的 format 方法
            formatted_sql = sqlparse.format(raw_sql,
                keyword_case=settings.get("keyword_case"),
                identifier_case=settings.get("identifier_case"),
                strip_comments=settings.get("strip_comments"),
                indent_tabs=settings.get("indent_tabs"),
                indent_width=settings.get("indent_width"),
                reindent=settings.get("reindent")
            )
            # 这里的 self 其含义类似于 Java this 关键字，view 应该是 sublime.View Class
            # 如果 sublime.view.settings().get('ensure_newline_at_eof_on_save') 的值置为 true，那么就在最后加上一个回车
            if self.view.settings().get('ensure_newline_at_eof_on_save'):
                formatted_sql += "\n"
            return formatted_sql
        except Exception as e:
            print(e)
            return None

    # 将 格式化好的文字，替换原有的文字
    def replace_region_with_formatted_sql(self, edit, region):
        # view.substr(region) Returns the contents of the region as a string.
        selected_text = self.view.substr(region)
        foramtted_text = self.format_sql(selected_text)
        self.view.replace(edit, region, foramtted_text)

    def run(self, edit):
        # 获取包含当前 view 的 window
        window = self.view.window()
        # 获取当前 window 下正在编辑的 view
        view = window.active_view()
        # view.sel() 返回选中项的引用
        for region in self.view.sel():
            # 如果 region 是空的
            if region.empty():
                # 根据起止点创建并获取一个 region
                selection = sublime.Region(0, self.view.size())
                self.replace_region_with_formatted_sql(edit, selection)
                # Changes the syntax used by the view. 改变“语法”是几个意思？
                self.view.set_syntax_file("Packages/SQL/SQL.tmLanguage")
            else:
                self.replace_region_with_formatted_sql(edit, region)