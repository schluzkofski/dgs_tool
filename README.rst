.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/birgits/dgs_tool/master

Installation
============

First of all you need a working Python 3 environment. On Windows it is easiest to use `anaconda`_ and best to install anaconda directly under C: (not C:\\Program Files as it contains a whitespace).  

.. _anaconda:
  https://www.anaconda.com/distribution/

We highly recommend to use virtual environments. Please see the
`installation page`_ of the oemof documentation for complete
instructions on how to install python and a virtual environment on your
operating system.
In case of anaconda see the `getting started`_ on how to work with environments in anaconda.

.. _getting started: https://conda.io/projects/conda/en/latest/user-guide/getting-started.html

As installation of geopackages is known to cause problems when installing them using pip on Windows, please install the python package fiona using conda:

.. code::

    conda install fiona

Next clone or download the repository to your local file system and install it through:

.. code::

    pip install -e path/to/dgs_tool

This tool is designed for Python 3 and tested on Python >= 3.6.

.. _installation page:
  http://oemof.readthedocs.io/en/stable/installation_and_setup.html

Basic Usage
============

This repository provides a Jupyter Notebook for downloading weather data and plotting.

To launch jupyter notebook type ``jupyter notebook`` in the terminal.
This will open a browser window. In Anaconda there is also a button you can use to launch jupyter notebook. See `here`_ for more information.

Navigate to the directory containing
the notebook(s) to open it. See the jupyter notebook quick start guide
for more information on `how to run`_ jupyter notebooks.
 
.. _how to run: http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html
.. _here: https://docs.anaconda.com/anaconda/user-guide/getting-started/#run-python-in-a-jupyter-notebook

License
=======

MIT License

Copyright (C) 2020 Reiner Lemoine Institute
