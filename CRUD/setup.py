from setuptools import setup

setup(
    name='pv',
    version='01',
    py_modules=['pv'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)

