# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "module")))

from module import __main__


def main() -> None:
    __main__.main()


if __name__ == "__main__":
    main()
