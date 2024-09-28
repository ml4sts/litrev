from setuptools import setup
# from setuptools import find_packages
# my_packages=find_packages()


setup(
    name='litreview-helper',
    version='0.1.1',
     include_package_data=True,
    packages=['litrev'               ],
    install_requires=[
        'Click', 'bibtexparser>=2.0.0b7'
    ],
    # package_data = {'':['assests/paper.md']},
    entry_points={
        'console_scripts': [
            'litrev = litrev.cli:lit_rev',
        ],
    },
)
