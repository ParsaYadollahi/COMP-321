from Cython.Build import cythonize
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',
                        '--path',
                        default = os.getcwd())
    args = parser.parse_args()

    path = args.path

    cythonized_files = cythonize(path, language_level = 3)
