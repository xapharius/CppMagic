from distutils.core import setup

setup(
    name='CppMagic',
    version='0.1.0',
    author='Mihai Suteu',
    author_email='mihai.suteu@xapharius.com',
    packages=['cppmagic'],
    url='http://github.com/xapharius/cppmagic',
    license='LICENSE',
    description='Ipython cell magic to run and time c++ code',
    long_description=open('README.md').read(),
)
