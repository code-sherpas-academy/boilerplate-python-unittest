"""
Module Docstring
"""

from introduce import Introduce

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

def main(name: str):
    introduce = Introduce()
    print(introduce.sayHi(name))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main("Anita")