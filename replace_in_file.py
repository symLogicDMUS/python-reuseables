import os


def replace_in_file(rootdir, find, replace):
    """
    :param rootdir: the directory to traverse
    :param find: str, the string to find
    :param replace: str, the string to replace with
    :return: None
    """
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            f = open(filepath, 'r')
            contents = f.read()
            f.close()
            contents = contents.replace(find, replace)
            f = open(filepath, 'w')
            f.write(contents)
            f.close()


if __name__ == '__main__':
    replace_in_file(
        'C:\\Users\\bjrat\\source\\repos\\Javascript\\ChessKingsCouncil\\app\\public\\Images\\text\\main menu\\normal\\8\\',
        '.svg', '-dark.svg')
