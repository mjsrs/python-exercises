from setuptools import setup

setup(
    name='myparser',
    version='0.1',
    py_modules=['myparser'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        myparser=myparser:cli
    ''',
)
