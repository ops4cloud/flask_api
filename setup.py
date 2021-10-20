from setuptools import setup, find_packages

setup(
    name='flask_api',
    version='1.0.0',
    description='Boilerplate code for a RESTful API based on Flask-RESTPlus',
    url='https://github.com/ops4cloud/flask_api.git',
    author='Gregory OTOOLE',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers LMFR',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='rest restful api flask swagger openapi flask-restplus',

    packages=find_packages(),

    install_requires=['flask-restplus==0.13.0'],
)