#!/usr/bin/python3
"""SQlite Console for app entry"""
import cmd

class SQLite(cmd.Cmd):
    """
        Lite Compiler is a version of sqlite created to explore and learn
        how the sqlite was created and to have an indepth knowledge in sql.
        .....
        The lite compiler inherits from the Cmd class
    """
    intro = 'sql python replica of the sqlite compiler.'
    prompt = 'sql > '

    def do_create(self):
        """create command from data definition language"""
        pass

    def do_help(self, arg: str) -> bool | None:
        """"""
        pass

    def precmd(self, line: str) -> str:
        print(line)

    def emptyline(self) -> bool:
        """a method that overrides an empty line when enter key is pressed"""
        pass

    def do_EOF(self, line: str):
        """a method that Exit the console"""
        return True

    def do_quit(self, line):
        """a method that quit the program"""
        return True


if __name__ == '__main__':
    SQLite().cmdloop()