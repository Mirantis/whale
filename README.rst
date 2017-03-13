=====
Whale
=====

Whale is intended to provide the community with a testing toolkit based on
`Stepler <https://github.com/Mirantis/stepler>`_ framework that is capable to
perform testing of Decapod (a tool to manage a life cycle of Ceph clusters).

How to run a docker container with Whale tests:

.. code-block:: console

    $ docker run \
        --rm \
        --net=host \
        -e DECAPOD_URL=${DECAPOD_URL} \
        -v $(pwd)/reports:/opt/app/test_reports \
        ${image}
