from setuptools import setup

setup(
        name='table_generator',
        version='0.1',
        py_modules=['main'],
        install_requires=[
                    'Click',
                ],
        entry_points='''
        [console_scripts]
                generate_table=main:create_table
                    ''',
)
