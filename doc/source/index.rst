.. whale documentation master file, created by
   sphinx-quickstart on Fri Sep 23 18:01:17 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

================================
Whale: test decapod step by step
================================

----------
Annotation
----------

Whale is intended to provide the community with a testing toolkit based on
Stepler framework that is capable of perform testing of tool to manage
lifecycle of Ceph cluster named Decapod.

------------
Architecture
------------

Architecture has following abstraction levels, where code lives (from higher to less):

* **clients** are able to manipulate resources: *users, roles, servers, etc*. For ex: *keystone client, nova client, node client, etc*.
* **steps** are actions, that we want to make over resources via **clients**: *create, delete, update, migrate, etc*. They should end with check, that step was finished correct.
* **fixtures** manage resources *construction, destruction, etc* via **steps**.
* **tests** combine **steps** and **fixtures** according to scenario.

Detailed information about autotests construction is available in `our guideline <http://autotests-guideline.readthedocs.io/>`_.

Sometimes it needs to have code for *ssh connection, proxy server, etc*. They are not related with **clients**, **steps**, **fixtures** and **tests** and are considered as third party helpers and must be implemented based on its purpose with OOP and design principles.

Whale uses `py.test <http://doc.pytest.org/>`_ as test runner and `tox <https://tox.readthedocs.io/>`_ for routine operations. Be sure you know them.

--------------
How to install
--------------

Make following commands in terminal::

   git clone https://github.com/Mirantis/whale.git
   cd whale
   virtualenv .venv
   . .venv/bin/activate
   pip install -U pip
   pip install -r requirements.txt
   pip install lib/decapodlib-{appropriate-version}-py2.py3-none-any.whl

----------------
How to run tests
----------------

*If you know how to launch tests with py.test, you may skip this section.*

Before launching you should export some openstack environment variables:

* ``DECAPOD_URL`` (default value ``'default'``)
* ``DECAPOD_LOGIN`` (default value ``'user'``)
* ``DECAPOD_PASSWORD`` (default value ``'password'``)


To get details look into ``whale/config.py``

Let's view typical commands to launch test in different ways:

* If you want to launch all tests (``-v`` is used to show full name and status of each test)::

   py.test whale -v

* For ex, you write the test ``test_create_user`` and want to launch it only::

   py.test whale -k test_create_user

* If your test was failed and you want to debug it, you should disable stdout capture::

   py.test whale -k test_create_user -s

* Full information about ``py.test`` is obtainable with::

   py.test -h

------------------
How to debug tests
------------------

We recommend to use ``ipdb`` to set up break points inside code. Just put following chunk before code line where you want to debug (don't forget about ``-s`` to disable  ``py.test`` stdout capture):

.. code:: python

   import ipdb; ipdb.set_trace()

-----------------
Deep to structure
-----------------

.. toctree::
   :maxdepth: 1

   decapod
   decapod_ui
