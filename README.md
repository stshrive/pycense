# pycense
Pip package scanner for licenses.

Working with pip packages can sometimes mean pulling in a package that uses a license incompatible with your development scenarios.

In order to ensure you are using only compliant licenses within your organization you need to know what licenses your underlying dependencies are using. The aim of this package is to provide a simple solution for sanning a project to collect the license information.

#Usage
Make sure your project is installed.
Run the pycense and provide the path to the root of your package: `-p <package_root>`
