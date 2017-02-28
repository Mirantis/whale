"""
-------------
Cluster steps
-------------
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

from hamcrest import (assert_that, equal_to, is_not,
                      empty, has_properties)  # noqa
from decapodlib import exceptions

from stepler.base import BaseSteps
from stepler.third_party import steps_checker
from stepler.third_party import waiter

__all__ = [
    'ClusterSteps'
]


class ClusterSteps(BaseSteps):
    """Cluster steps."""

    @steps_checker.step
    def create_cluster(self, cluster_name, check=True, **kwargs):
        """Step to create cluster.

        Args:
            cluster_name (str): the name of the cluster
            check (bool): flag whether to check step or not
            **kwargs: any suitable to cluster keyword arguments

        Returns:
            cluster (dict): model of the cluster

        Raises:
            TimeoutExpired: if check failed after timeout
        """
        cluster = self._client.create_cluster(cluster_name, **kwargs)

        if check:
            self.check_cluster_presence(cluster['id'])
            assert_that(cluster['data']['name'], equal_to(cluster_name))

        return cluster

    @steps_checker.step
    def delete_cluster(self, cluster_id, check=True, **kwargs):
        """Step to delete cluster.

        Args:
            cluster_id (str): cluster id
            check (bool): flag whether to check step or not
            **kwargs: any suitable to cluster keyword arguments

        Raises:
            TimeoutExpired|AssertionError: if check failed
        """
        self._client.delete_cluster(cluster_id, **kwargs)
        if check:
            self.check_cluster_presence(cluster_id, must_present=False)

    @steps_checker.step
    def get_cluster(self, cluster_id, check=True, **kwargs):
        """Step to retrieve cluster.

        Args:
            cluster_id (str): cluster id
            check (bool): flag whether to check step or not
            **kwargs: any suitable to cluster keyword arguments

        Returns:
            cluster (dict): model of the cluster
        """
        cluster = self._client.get_cluster(cluster_id=cluster_id, **kwargs)
        if check:
            assert_that(cluster, has_properties(**kwargs))

        return cluster

    @steps_checker.step
    def get_cluster_id(self, cluster_name, check=True, **kwargs):
        """Step to retrieve cluster id.

        Args:
            cluster_name (str): cluster name
            check (bool): flag whether to check step or not
            **kwargs: any suitable to cluster keyword arguments

        Returns:
            cluster_id (str): cluster id
        """
        clusters = self._client.get_clusters(**kwargs)
        for cluster in clusters['items']:
            if cluster['data']['name'] == cluster_name:
                cluster_id = cluster['id']

        if check:
            assert_that(cluster_id, is_not(empty()))

        return cluster_id

    @steps_checker.step
    def check_cluster_presence(self, cluster_id, must_present=True, timeout=0):
        """Check step that cluster is present.

        Args:
            cluster_id (str or obj): the cluster to be checked on the server
            must_present (bool): flag whether cluster should present or no
            timeout (int): seconds to wait a result of check

        Raises:
            TimeoutExpired/DecapodAPIError: if check failed after timeout or
            API response exception
        """

        def _check_cluster_presence():
            try:
                cluster = self._client.get_cluster(cluster_id)
                if cluster['time_deleted'] == 0:
                    is_present = True
                else:
                    is_present = False
            except exceptions.DecapodAPIError:
                is_present = False

            return waiter.expect_that(is_present, equal_to(must_present))

        waiter.wait(_check_cluster_presence, timeout_seconds=timeout)
