from setuptools import setup, find_packages
import imdb

setup(
    name = 'imdb',
    version = imdb.__version__,
    packages = find_packages(),
    long_description=open('README.rst', 'rt').read(),
    install_requires = ['beautifulsoup4 == 4.1.3', 'html5lib == 0.95', 'requests == 1.1.0'],
    author = 'Chris Grice',
    author_email = 'chris@chrisgrice.com',
    license = 'MIT',
    description = 'Markdown-based blog engine that compiles to static html pages',
    url='http://github.com/cgrice/imdb/',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    zip_safe = False
)