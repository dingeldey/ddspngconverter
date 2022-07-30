from wand import image
from typing import List
import sys


def main(arg_list: List[str]):
    for file in arg_list[1:]:
        with image.Image(filename=file) as img:
            img.compression = "no"
            f = file.split(".dds")[0] + ".png"
            img.save(filename=f)


if __name__ == '__main__':
    main(sys.argv)
