from setuptools import setup, find_packages

install_requires = ['pandas', 'requests']

setup(
    name='DSSPparser',
    version='0.10',
    url='https://github.com/neolei',
    download_url='',
    author='neolei',
    author_email='wl20132017@webmail.edu.cn',
    description='parse protein secondary structure dssp file; DSSP api interface',
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