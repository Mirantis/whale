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
    'cluster',
    'deploy_cluster',
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
def delete_cluster(get_cluster_steps,
                   playbook_config_steps,
                   execution_steps):
    """Callable fixture to delete cluster.

    If cluster is deployed, this fixture creates execution to delete it.
    Otherwise cluster_steps are used.
    This fixture is used in cluster_steps for clusters cleanup so we have
    to use get_cluster_steps for cluster_steps getting to avoid recursion.

    Args:
        get_cluster_steps (function): function to get cluster steps
        playbook_config_steps (obj): instantiated playbook config steps
        execution_steps (obj): instantiated execution steps

    Returns:
        function: function to delete cluster
    """
    def _delete_cluster(cluster_id):
        _cluster_steps = get_cluster_steps()

        cluster = _cluster_steps.get_cluster(cluster_id)
        if cluster['data']['configuration']:
            # cluster has servers
            if 'osds' in cluster['data']['configuration']:
                # we can't remove cluster with osd
                server_ids = [
                    server['server_id']
                    for server in cluster['data']['configuration']['osds']
                ]
                osd_config = playbook_config_steps.create_playbook_config(
                    cluster['id'],
                    config.PLAYBOOK_REMOVE_OSD,
                    server_ids=server_ids)
                execution_steps.create_execution(osd_config['id'])

            cluster_config = playbook_config_steps.create_playbook_config(
                cluster['id'], config.PLAYBOOK_PURGE_CLUSTER, server_ids=[])
            execution_steps.create_execution(cluster_config['id'])
        else:
            # cluster doesn't have servers
            _cluster_steps.delete_cluster(cluster_id)

    return _delete_cluster


@pytest.fixture
def cluster(cluster_steps):
    """Fixture to create cluster with default options before test.

    Args:
        cluster_steps (obj): instantiated cluster steps

    Returns:
        dict: model of the cluster
    """
    return cluster_steps.create_cluster()


@pytest.fixture
def deploy_cluster(cluster_steps, playbook_config_deploy, execution_steps):
    """Fixture to create and deploy cluster before test.

    Args:
        cluster_steps (obj): instantiated cluster steps
        playbook_config_deploy (dict): created playbook configuration
            to deploy cluster
        execution_steps (obj): instantiated execution steps

    Returns:
        dict: model of the cluster
    """
    execution_steps.create_execution(playbook_config_deploy['id'])
    return cluster_steps.get_cluster(
        playbook_config_deploy['data']['cluster_id'])


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
