import os


def file_exists_check(file_name):
    file_path = file_abs_path()
    file_status = os.path.exists(file_path + file_name)

    return file_status


def file_abs_path():
    file_path = os.path.dirname(os.path.realpath(__file__))

    file_dir_path = file_path + '/'
    return file_dir_path


if __name__ == '__main__':
    file_abs_path()
