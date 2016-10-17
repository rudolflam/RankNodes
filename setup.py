from distutils.core import setup	
import os.path
import sys

setup(
	name = 'ranknodes',
	version = '0.1',
	packages = ['ranknodes'],
	author = 'Rudolf Lam',
	author_email = 'rudolf.lam@mail.mcgill.ca',
	description = 'A minimalistic package for analysing nodes in a network ',
	license = 'GNU GPLv3',
	keywords = ['network','pipable'],
    entry_points={'console_scripts': ['ranknodes = ranknodes.__main__:main']},
	classifiers=[
		'Development Status :: 5',

		'Environment :: Console',

		'Intended Audience :: Science/Research',
		'Intended Audience :: Information Technology',

		'Topic :: Scientific/Engineering',
		'Topic :: Scientific/Engineering :: Information Analysis',
		'Topic :: Utilities',

		'Programming Language :: Python :: 2.7']
)