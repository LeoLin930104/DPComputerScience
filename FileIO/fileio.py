import os
import os.path as path

if __name__ == "__main__":
    cwd = os.getcwd()
    file_path = path.join(cwd, "FileIO", "data.txt")
    print(file_path)
    with open(file_path, "r") as f:
        print(f.read())
        f.seek(0)
        print(f.read())

# File Open Option
# r - read
# rb - read binary
# w - write Over
# wb - write binary
# a - append