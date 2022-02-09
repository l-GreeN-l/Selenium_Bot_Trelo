from setuptools import setup
from setuptools import find_packages


setup(
    name = 'trello_Bot',
    version = '0.0.1',
    description = '',
    autor = [ 'zgreenz'],
    email = ['valdisvan@mail.ru'],
    install_requires = [
        'pytest==6.1.2',
        'selenium==3.14.0',
        'requests==2.23.0', 
        'pytest-html==2.1.1',
        'psycopg2-binary==2.8.6',
        'stopit==1.1.2',
        'pytz==2021.1'
    ],
    packages=find_packages()
)
