import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='idtool',
    version='2.1.0',
    author='AlumiK',
    author_email='nczzy1997@gmail.com',
    license='MIT',
    description='A simple customizable ID generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AlumiK/id-tool',
    packages=setuptools.find_packages(include=['idtool', 'idtool.*']),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
