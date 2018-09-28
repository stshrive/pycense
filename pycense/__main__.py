from pycense import main
import argparse
import sys
import subprocess

arg_parser = argparse.ArgumentParser(sys.argv[0])
arg_parser.add_argument('-p', '--path', type=str, default='.')
arg_parser.add_argument('-o', '--output', type=str, default='./license_info.txt')
arg_parser.add_argument('-r', '--exclude-requirements', action='store_true')
arg_parser.add_argument('-i', '--exclude-imports', action='store_true')

arguments = arg_parser.parse_args()
main(**arguments.__dict__)
