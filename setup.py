from setuptools import setup, find_packages

install_requires=[
    "py-dummy-pkg @ git+ssh://git@github.com/az0uz/py-dummy-pkg.git@v0.1.0"
]
setup(name="py-foo-pkg", version="0.1.0", python_requires=">=3.6", install_requires=install_requires, packages=find_packages())
