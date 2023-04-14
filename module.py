# -*- coding: utf-8 -*-
import runpy


def main() -> None:
    runpy.run_module("module", run_name="__main__")


if __name__ == "__main__":
    main()
