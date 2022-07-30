from wand import image
from typing import List
import sys


def main(arg_list: List[str]):
    for file in arg_list[1:]:
        with image.Image(filename=file) as img:
            img.compression = "dxt5"
            f = file.split(".png")[0] + ".dds"
            img.save(filename=f)


if __name__ == '__main__':
    main(sys.argv)

