==========
Annotation
==========
This repo contains decapod integration UI tests, which work with dashboard as user. They are based on STEPS-methodology to provide scalable, modular and portable code. And under hood they use `POM <https://github.com/sergeychipiga/pom>`_-microframework, which provide the logic to operate with DOM.

====================
Architectural levels
====================

- ``tests`` - (pytest specific) use steps to work with dashboard
- ``fixtures`` - (pytest specific) provide setup and teardown actions
- ``steps`` - (cross platform) actions over page content
- ``pages`` - declarative description of page structure
- ``POM`` - unified methods to manipulate with pages and UI elements.
- ``selenium`` - low level to manipulate with DOM

===========
Preparation
===========

``sudo apt-get install libav-tools firefox``

Download the latest executable geckodriver from https://github.com/mozilla/geckodriver/releases to run the latest firefox using selenium.
Add the directory containing the executable to the system path.

For example for Ubuntu run the following commands:
``wget https://github.com/mozilla/geckodriver/releases/download/v0.14.0/geckodriver-v0.14.0-linux64.tar.gz``
``tar -xzvf geckodriver-v0.14.0-linux64.tar.gz``
``export PATH=$PATH:$(pwd)``

==========
How to run
==========
Before launching you should export some openstack environment variables::

* ``DECAPOD_URL`` (default value ``'default'``)
* ``DECAPOD_LOGIN`` (default value ``'user'``)
* ``DECAPOD_PASSWORD`` (default value ``'password'``)

Let’s view typical commands to launch test in different ways:

``py.test whale/decapod_ui -v`` - single-threaded mode to launch tests at display

``VIRTUAL_DISPLAY=1 py.test whale/decapod_ui -v`` - single-threaded mode to launch tests in virtual frame buffer (headless mode)

``VIRTUAL_DISPLAY=1 py.tests whale/decapod_ui -v -n 4`` - multi-processed mode to launch tests in virtual frame buffers (create 4 parallel processes to launch tests)

============
Test results
============
After tests finishing there will be a directory ``test_reports`` which contains folders named test names, where there are:

- ``video.mp4`` - video capture of test (can be played with browser player)
- ``remote_connection.log`` - log of selenium webdriver requests to browser
- ``timeit.log`` - log of time execution of steps and UI element actions
- ``test.log`` - log of everything else

==================
How to write tests
==================
In progress...

================
Current coverage
================
In progress...
