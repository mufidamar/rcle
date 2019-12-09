from setuptools import setup

setup(name='rcle',
	version='1.5',
	description='Install Let\'s Encrypt SSL on RunCloud servers the easy way.',
	author="Amaruddin Mufid",
	author_email="mufidamar@outlook.com",
	url="https://github.com/mufidamar/rcle/",
	license="MIT",
	entry_points={
		'console_scripts': [
			'rcle = rcle.rcle:main'
		],
	},
	packages=[
		'rcle'
	],
	install_requires=[
		'python-nginx'
	]
)