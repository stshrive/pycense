from pip_module_scanner.scanner import Scanner

def main(path, output):
    scanner = Scanner(path=path)
    scanner.run()

    for lib in scanner.libraries_found:
        with open(output, 'w') as f:
            f.write(f'{lib.key} == {lib.version}')

if __name__ == "__main__":
    import argparse
    import sys

    arg_parser = argparse.ArgumentParser(sys.argv[0])
    arg_parser.add_argument('-p', '--path', type=str, default='.')
    arg_parser.add_argument('-o', '--output', type=str, default='./license_info.txt')

    arguments = arg_parser.parse_args()
    main(**arguments.__dict__)
