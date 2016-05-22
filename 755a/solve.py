# coding: utf-8
import os


def find_max_size_file(dir_path):
    dirs_and_files = os.listdir(dir_path)
    dirs_and_files_path = map(lambda x: dir_path + "/" + x, dirs_and_files)
    max_file_size_in_path = map(lambda x: (x, os.path.getsize(x)) if os.path.isfile(x) else find_max_size_file(x), dirs_and_files_path)
    if not max_file_size_in_path:
        return ("", 0)
    max_file = max(max_file_size_in_path, key=lambda s: s[1])
    return max_file


if __name__ == '__main__':
    print find_max_size_file('/home/bill/Desktop/github/qlcoder/755a/root')