marklearningtravis
==================

[![Build Status](https://travis-ci.org/mjordan/marklearningtravis.png?branch=master)](https://travis-ci.org/mjordan/marklearningtravis)

Test repo for me to learn about using [travis-ci](https://travis-ci.org/).

.travis.yml installs a couple of Python libraries using pip, creates a MySQL database and populates it with sample data, configures Apache to run a [bottle](bottlepy.org/) application, and then runs a Pytest test suite.

tests.py tests whether an HTTP request to the bootle app returns successful, and whether there are any rows in the database.

Thanks to [@beghelli](https://github.com/beghelli) and [@MichaelThessel](https://github.com/MichaelThessel) for initial tips.

