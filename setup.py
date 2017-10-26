#!/usr/bin/env python3

from setuptools import setup

import os
import sys

if sys.version_info[:2] <= (3,5):
	sys.exit('Sorry, only Python 3.5+ is supported')

#https://pythonhosted.org/an_example_pypi_project/setuptools.html
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='fuse-3ds',
	version='1.0',
	description='Allows mounting of 3DS-related files using FUSE',
	license='MIT',
	keywords='3DS extract filesystem',
	author='ihaveamac',
	author_email='ian@ianburgwin.net',
	long_description=read('README.md'),
	classifiers=[
		"Topic :: Utilities",
		"License :: OSI Approved :: MIT License",
    ],
	install_requires=['pycryptodomex', 'fusepy'],
	dependency_links=['git+https://github.com/billziss-gh/fusepy.git'],
	packages=['fuse-3ds'],
	entry_points={ "console_scripts": [ "mount_cci=mount_cci.mount_cci:main",
										"mount_cdn=mount_cdn.mount_cdn:main",
										"mount_cia=mount_cia.mount_cia:main",
										"mount_nand=mount_nand.mount_nand:main",
										"mount_ncch=mount_ncch.mount_ncch:main",
										"mount_romfs=mount_romfs.mount_romfs:main",
										"mount_sd=mount_sd.mount_sd:main" ] }
)