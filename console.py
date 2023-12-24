#!/usr/bin/python3
"""SQlite Console for app entry"""
import cmd


class LiteCompiler(cmd.Cmd):
    """
        Lite Compiler is a version of sqlite created to explore and learn
        how the sqlite was created and to have an indepth knowledge in sql.
        .....
        The lite compiler inherits from the Cmd class
    """
    intro = 'sql python replica of the sqlite compiler.'
    prompt = 'sql >'

    def do_create(self):
        """create command from data definition language"""


if __name__ == '__main__':
    LiteCompiler().cmdloop()