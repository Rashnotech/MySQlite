#!/usr/bin/env python3
"""SQlite Console for app entry"""
import cmd
from models.create import Create

class SQLite(cmd.Cmd):
    """
        Lite Compiler is a version of sqlite created to explore and learn
        how the sqlite was created and to have an indepth knowledge in sql.
        .....
        The lite compiler inherits from the Cmd class
    """
    intro = 'sql python replica of the sqlite compiler.'
    prompt = 'sql > '
    _cmd = ['create', 'select']
    flag = False

    def do_create(self, line):
        """create command from data definition language"""
        args = line.split()
        if len(args) == 5:
            _, _, _, _args, _name = args
        else:
            _args, _name = args
        _name = _name.replace(';', '')
        cls = Create()
        if _args == 'database':
            cls.database(self.flag, _name)
        if _args == 'table':
            cls.table(_name)

    def do_help(self, arg: str) -> bool | None:
        """"""
        pass

    def precmd(self, line: str) -> str:
        try:
            if line.endswith(';'):
                args = line.lower().split()
                _cmd, params = args[0], args[1:]
                if _cmd not in self._cmd:
                    raise Exception
                for idx, attr in enumerate(params):
                    if attr in ['if', 'not', 'exist']:
                        line.replace(attr, '')
                        self.flag = True
                return line
            else:
                raise SyntaxError
        except Exception as e:
            print(e)




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