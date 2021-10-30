import os


def cls():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def pause(with_linebreak):
    if with_linebreak:
        print()

    if os.name == 'nt':
        os.system("pause")
    else:
        pass


def separator(path):
    return "\\" if "\\" in path else "/"
