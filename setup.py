from setuptools import setup, find_packages

install_requires = ['pandas', 'requests']

setup(
    name='DSSPparser',
    version='0.12',
    url='https://github.com/neolei/DSSPparser',
    download_url='https://github.com/neolei/DSSPparser',
    author='neolei',
    author_email='wl20132017@webmail.hzau.edu.cn',
    maintainer='neolei',
    description='parse protein secondary structure; dssp file; DSSP api interface; transform PDB format to dssp format',
    keywords=['Bioinformation', 'DSSP'],
    long_description=open("README.rst").read(),
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
