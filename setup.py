from setuptools import setup

# read the contents of your README file 
with open('README.md') as f:
    long_description = f.read()

setup(
    name='rcle',
	version='1.1.1',
	description='Install Let\'s Encrypt SSL on RunCloud servers the easy way.',
    long_description=long_description,
    long_description_content_type='text/markdown',
	author="Amaruddin Mufid",
	author_email="mufidamar@outlook.com",
	url="https://github.com/mufidamar/rcle/",
	license="MIT",
    packages=['rcle'],
	entry_points={
		'console_scripts': [
			'rcle = rcle.rcle:main'
		],
	},
	install_requires=[
		'python-nginx'
	],
)
