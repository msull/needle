from distutils.core import import setup

setup(
    name='needle',
    packages = ['needle']
    py_modules=['needle'],
    description = 'Easy file searching from the command-line'
    author = 'Sully Sullenberger',
    author_email = 'sully@sadburger.com'
    url = 'https://github.com/msull/needle',
    download_url = 'https://github.com/msull/needle/tarball/0.1',
    keywords = ['search', 'files', 'terminal'],
    classifiers = [],
    version='0.1',
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        ndl=needle.cli:cli
    """,
)
