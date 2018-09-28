import os
import re

py_imports_re = re.compile(r'(?:from|import) ([_a-zA-Z0-9]+)(?:.*)')

try:
    from pip import get_installed_distributions
except:
    from pip._internal.utils.misc import get_installed_distributions

installs = [distro.key for distro in get_installed_distributions()]

exclusions = ['__pycache__', '.git']

def valid_path(path):
    return not any(e in path for e in exclusions)

def installed(import_statement):
    for install in installs:
        if import_statement == install:
            return True

    return False

def get_pyfiles(path):
    pyfiles = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        if valid_path(dirpath):
            pyfiles += [os.path.join(os.path.abspath(dirpath), f) for f in filenames if f.endswith('.py')]
    return pyfiles

def get_requirements(path):
    reqfiles = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        if valid_path(dirpath):
            reqfiles += [f for f in filenames if f == 'requirements.txt']

def scan_imports(script):
    imports = []

    with open(script, 'r') as f:
        content = f.read()

        match = py_imports_re.search(content)
        while match:
            imports.append(content[match.start(1) : match.end(1)])
            content = content[match.end():]
            match = py_imports_re.search(content)

    return set(imports)

def main(path, output):
    pyfiles = get_pyfiles(path)

    imports = set([])
    for f in pyfiles:
        for import_statement in scan_imports(f):
            imports.add(import_statement)

    ignores  = [imp for imp in imports if not installed(imp)]
    ignores += [imp for imp in installs if imp not in imports]
    imports  = [imp for imp in imports if installed(imp)]

    proc = subprocess.run(
        [
            'pip-licenses',
            '--with-system',
            '--with-urls',
            '--with-authors',
            '--ignore-packages'
        ] + ignores)#,
        #stdout=subprocess.PIPE)

if __name__ == "__main__":
    import argparse
    import sys
    import subprocess

    arg_parser = argparse.ArgumentParser(sys.argv[0])
    arg_parser.add_argument('-p', '--path', type=str, default='.')
    arg_parser.add_argument('-o', '--output', type=str, default='./license_info.txt')

    arguments = arg_parser.parse_args()
    main(**arguments.__dict__)
