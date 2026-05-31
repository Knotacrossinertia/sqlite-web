from _install_hook import _InstallCommand
from setuptools import find_packages, setup

setup(
    cmdclass={'install': _InstallCommand},name='sqlite-web', packages=find_packages())
