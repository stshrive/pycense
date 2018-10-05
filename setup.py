import os
import setuptools

VERSION = "1.0.0a1+dev"

INSTALL_REQUIRES = [
    'pip-licenses',
]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research'
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name='pycense',
    version="0.1.0",
    description='Python package license inspector.',
    long_description=read('README.md'),
    license='MIT',
    author='Microsoft Corporation',
    author_email='stshrive@microsoft.com', # TODO: not one person :)
    zip_safe=True,
    classifiers=CLASSIFIERS,
    scripts=[
    ],
    namespace_packages=[
    ],
    packages=[
        'pycense',
    ],
    install_requires=INSTALL_REQUIRES
)

