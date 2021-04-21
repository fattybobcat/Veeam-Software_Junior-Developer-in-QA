import hashlib
import os
import sys


def hash_file(file_name, hash_mode):
    BLOCK_SIZE = 65536
    try:
        with open(file_name, "rb") as f:
            file_hash = hashlib.new(hash_mode)
            while chunk := f.read(BLOCK_SIZE):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except Exception:
        return -1


def check_hash_files(path_to_file_check: str, path_to_check_files: str):
    try:
        with open(path_to_file_check, "r") as f:
            for line in f.readlines():
                file_name, mode, hash_sum = line.split()
                path_file_check = os.path.join(path_to_check_files, file_name)
                hash_f = hash_file(path_file_check, mode)
                if hash_f == -1:
                    print("{} NOT FOUND".format(file_name))
                elif hash_f == hash_sum:
                    print("{} OK".format(file_name))
                else:
                    print("{} FAIL".format(file_name))
    except FileNotFoundError as e:
        print(e)
        sys.exit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("""Program requires two parameters:
        1: path to file with parameters for check (name, hash mode, hash sum)
        in '';
        2: path to files to chek hash sum in ''.
        """)
        sys.exit(1)

    file_check = str(sys.argv[1])
    path_to_check_files = str(sys.argv[2])
    check_hash_files(file_check, path_to_check_files)
