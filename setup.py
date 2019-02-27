from setuptools import setup, find_packages
import os

this_directory = os.path.abspath(os.path.dirname(__file__))
def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

install_requires = ['pandas', 'requests']

setup(
    name='DSSPparser',
    version='0.10',
    url='https://github.com/neolei/DSSPparser',
    download_url='https://github.com/neolei/DSSPparser',
    author='neolei',
    author_email='wl20132017@webmail.edu.cn',
    description='parse protein secondary structure dssp file; DSSP api interface',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(where="."),
    zip_safe=True,
    classifiers=['Intended Audience :: Developers',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5'],
    install_requires=install_requires,
    extras_require={}
)