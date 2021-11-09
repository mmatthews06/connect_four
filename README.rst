Connect_Four
============

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |Python Version| image:: https://img.shields.io/pypi/pyversions/connect_four
   :target: https://pypi.org/project/connect_four
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/connect_four
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/connect_four/latest.svg?label=Read%20the%20Docs
   :target: https://connect_four.readthedocs.io/
   :alt: Read the documentation at https://connect_four.readthedocs.io/
.. |Tests| image:: https://github.com/mmatthews06/connect_four/workflows/Tests/badge.svg
   :target: https://github.com/mmatthews06/connect_four/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/mmatthews06/connect_four/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/mmatthews06/connect_four
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Features
--------

* A Connect Four game in the console.
* Created using Cruft_, from the cookiecutter-hypermodern-python repository mentioned below.
* Written with Python 3.10.0, though I've confirmed that it works with 3.9.7

The actual CLI "UX" could use some polish. The implementation is slightly more than a first pass, but seems pretty good right now.

This will include development instructions later, or upon request. Basically, install Poetry and Nox, and the development process should be pretty easy.

Installation
------------

You can install *Connect_Four* via pip_ from a clone of this repository:

.. code:: console

   $ mkdir connect_four_test && cd connect_four_test
   $ git clone https://github.com/mmatthews06/connect_four.git
   $ mkdir test && cd test
   $ python -m venv env
   $ source env/bin/activate
   $ pip install ../connect_four
   $ connect_four # should start the CLI.



Usage
-----

Please see the `Command-line Reference <Usage_>`_ for details.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `MIT license`_,
*Connect_Four* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT license: https://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/mmatthews06/connect_four/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://connect_four.readthedocs.io/en/latest/usage.html
.. _Cruft: https://cruft.github.io/cruft/
