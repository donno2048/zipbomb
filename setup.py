from setuptools import setup, find_packages
setup(
    name='zipbomb',
    version='1.0.3',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description="Create zipbombs using python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/zipbomb',
    project_urls={
        'Documentation': 'https://github.com/donno2048/zipbomb#readme',
        'Bug Reports': 'https://github.com/donno2048/zipbomb/issues',
        'Source Code': 'https://github.com/donno2048/zipbomb',
    },
    python_requires='>=3.0',
    packages=find_packages(),
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'zipbomb=zipbomb.__main__:main' ] }
)
