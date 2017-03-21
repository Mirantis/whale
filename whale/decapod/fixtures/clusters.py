"""
----------------
Cluster fixtures
----------------
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from whale import config
from whale.decapod import steps

__all__ = [
    'get_cluster_steps',
    'cluster_steps',
    'delete_cluster',
    'create_cluster',
    'cluster',
    'cleanup_clusters',
]


@pytest.fixture(scope="session")
def get_cluster_steps(get_decapod_client):
    """Callable session fixture to get cluster steps.

    Args:
        get_decapod_client (function): function to get decapod client

    Returns:
        function: function to get cluster steps
    """
    def _get_cluster_steps():
        return steps.ClusterSteps(get_decapod_client())

    return _get_cluster_steps


@pytest.fixture
def cluster_steps(get_cluster_steps, cleanup_clusters):
    """Function fixture to get cluster steps.

    Args:
        get_cluster_steps (function): function to get cluster steps
        cleanup_clusters (function): function to cleanup clusters after test

    Yields:
        ClusterSteps: instantiated cluster steps
    """
    _cluster_steps = get_cluster_steps()
    clusters = _cluster_steps.get_clusters(check=False)
    clusters_ids_before = {cluster['id'] for cluster in clusters}

    yield _cluster_steps

    cleanup_clusters(_cluster_steps, uncleanable_ids=clusters_ids_before)


@pytest.fixture
def delete_cluster(get_cluster_steps, create_playbook_config,
                   get_execution_steps):
    """Callable fixture to delete cluster.

    If cluster is deployed, this fixture creates execution to delete it.
    Otherwise cluster_steps are used.

    Args:
        get_cluster_steps (object): function to get cluster steps
        create_playbook_config (function): create configuration
        get_execution_steps (object): function to get execution steps

    Returns:
        function: function to delete cluster
    """
    def _delete_cluster(cluster_id, version=1):
        _cluster_steps = get_cluster_steps()
        _execution_steps = get_execution_steps()

        cluster = _cluster_steps.get_cluster(cluster_id)
        if cluster['data']['configuration']:
            # cluster has servers
            playbook_config = create_playbook_config(
                cluster['id'], config.PLAYBOOK_PURGE_CLUSTER, server_ids=[])
            _execution_steps.create_execution(playbook_config['id'],
                                              version)
        else:
            # cluster doesn't have servers
            _cluster_steps.delete_cluster(cluster_id)

    return _delete_cluster


@pytest.fixture
def create_cluster(cluster_steps, delete_cluster):
    """Callable fixture to create cluster with options.

    Can be called several times during a test.
    After the test it destroys all created clusters.

    Args:
        cluster_steps (object): instantiated cluster steps
        delete_cluster (function): function to delete cluster

    Yields:
        function: function to create cluster with options
    """
    clusters = []

    def _create_cluster(*args, **kwargs):
        cluster = cluster_steps.create_cluster(*args, **kwargs)
        clusters.append(cluster)
        return cluster

    yield _create_cluster

    for cluster in clusters:
        delete_cluster(cluster['id'])


@pytest.fixture
def cluster(create_cluster):
    """Fixture to create cluster with default options before test.

    Args:
        create_cluster (function): function to create cluster with options

    Returns:
        dict: model of the cluster
    """
    return create_cluster()


@pytest.fixture
def cleanup_clusters(delete_cluster):
    """"Callable session fixture to cleanup clusters.

    Args:
        delete_cluster (function): function to delete cluster

    Returns:
        function: function to cleanup clusters after tests
    """
    def _cleanup_clusters(_cluster_steps, uncleanable_ids=None):
        uncleanable_ids = uncleanable_ids or []
        for cluster in _cluster_steps.get_clusters(check=False):
            if cluster['id'] not in uncleanable_ids:
                delete_cluster(cluster['id'])

    return _cleanup_clusters
