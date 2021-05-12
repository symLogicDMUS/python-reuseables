import os


def replace_in_file_name(rootdir, find, replace):
    """
    :param rootdir: the directory to traverse
    :param find: str, the string to find
    :param replace: str, the string to replace with
    :return: None
    """
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if find in filepath:
                new_file_path = filepath.replace(find, replace)
                os.rename(filepath, new_file_path)


if __name__ == '__main__':
    replace_in_file_name(
        'C:\\Users\\bjrat\\source\\repos\\Javascript\\ChessKingsCouncil\\app\\public\\Images\\text\\main menu\\normal\\8\\',
                         '.svg', '-dark.svg')
