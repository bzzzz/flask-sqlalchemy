"""
Flask-SQLAlchemy
----------------

Adds SQLAlchemy support to your Flask application.

Links
`````

* `documentation <http://packages.python.org/Flask-SQLAlchemy>`_
* `development version
  <http://github.com/mitsuhiko/flask-sqlalchemy/zipball/master#egg=Flask-SQLAlchemy-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-SQLAlchemy',
    version='0.10',
    url='http://github.com/mitsuhiko/flask-sqlalchemy',
    license='BSD',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    description='Adds SQLAlchemy support to your Flask application',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'setuptools',
        'Flask',
        'SQLAlchemy'
    ],
    test_suite='test_sqlalchemy',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
