"""This package exports a factory of loaders.

Loaders are objects which can download tests from a website
and store them on the computer. They have two structural
components (a downloader, and a writer) and should have a method
which loads the actual testcases.

Some loaders could also contain a parser if they need to scrape
testcases from a website which does not offer them through its API.
"""

from .factory import get_loader
