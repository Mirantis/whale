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

from whale.decapod import steps

__all__ = [
    'get_cluster_steps',
    'cluster_steps',
    'create_cluster',
    'cluster',
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
def cluster_steps(get_cluster_steps):
    """Function fixture to get cluster steps.

    Args:
        get_cluster_steps (function): function to get cluster steps

    Returns:
        ClusterSteps: instantiated cluster steps
    """
    return get_cluster_steps()


@pytest.fixture
def create_cluster(cluster_steps):
    """Callable fixture to create cluster with options.

    Can be called several times during a test.
    After the test it destroys all created clusters.

    Args:
        cluster_steps (object): instantiated cluster steps

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
        cluster_steps.delete_cluster(cluster)


@pytest.fixture
def cluster(create_cluster):
    """Fixture to create cluster with default options before test.

    Args:
        create_cluster (function): function to create cluster with options

    Returns:
        cluster (dict): model of the cluster
    """
    return create_cluster()
