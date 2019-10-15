from setuptools import setup

setup(
    name='pensador-python',
    version='0.0.1',
    description='library for querying quotes from https://pensador.com',
    license='LICENSE.txt',
    packages=[
        'beautifulsoup4>=4.8.1',
        'requests>=2.22.0'
    ],
    author='Samuel Petroline',
    author_email='samuelpetroline@gmail.com',
    keywords=['pensador', 'quotes'],
    url='https://github.com/samuelpetroline/pensador-python'
)