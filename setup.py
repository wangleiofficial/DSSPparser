from setuptools import setup, find_packages

install_requires = ['pandas', 'requests', 'biopython']

setup(
    name='DSSPparser',
    version='0.1.3',
    url='https://github.com/wangleiofficial/DSSPparser',
    author='wanglei',
    author_email='wanglei94@hust.edu.cn',
    maintainer='wanglei',
    description='parse protein secondary structure; dssp file; DSSP api interface; transform PDB format to dssp format',
    keywords=['Bioinformation', 'DSSP'],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(where=".", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
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
    extras_require={},
    entry_points={
        'console_scripts': ['pdbToXssp=DSSPparser.cmdline:main'],
    }
)
