import os
import uuid


def gen_new_file_name(tmp, file_name):

    suffix = os.path.splitext(file_name)
    return tmp + suffix[1]
