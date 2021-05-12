import os


def change_extentions(rootdir, old_exten, new_exten):
    """change all files in the directory with the old extention to the new extention"""
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(old_exten):
                new_file_path = filepath.replace(old_exten, new_exten)
                print(new_file_path)
                os.rename(filepath, new_file_path)


if __name__ == '__main__':
    pass  # TODO: test
