# activate virtual environment (Windows)
# cd windows_venv/Lib
# activate
#
# activate virtual environment (Linux)
# source linux_venv/bin/activate

from GUIs import *
from dataExtractor import DataExtractor

de = None


def main():
    de = DataExtractor()
    main_gui(de)


if __name__ == '__main__':
    main()
