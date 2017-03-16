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

from hamcrest import (assert_that, empty, equal_to, has_entries,
                      is_not)  # noqa H301
from stepler.third_party import steps_checker
from stepler.third_party import utils

from whale import base

__all__ = [
    'ClusterSteps'
]


class ClusterSteps(base.BaseSteps):
    """Cluster steps."""

    @steps_checker.step
    def create_cluster(self, cluster_name=None, check=True, **kwargs):
        """Step to create cluster.

        Args:
            cluster_name (str|None): the name of the cluster
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: model of the cluster

        Raises:
            TimeoutExpired|AssertionError: if check failed
        """
        cluster_name = cluster_name or next(utils.generate_ids())
        # only letters and digits are allowed for cluster name
        cluster_name = cluster_name.replace('-', '')

        cluster = self._client.create_cluster(cluster_name, **kwargs)

        if check:
            self.check_resource_presence(cluster['id'],
                                         self._client.get_cluster)
            assert_that(cluster['data']['name'], equal_to(cluster_name))

        return cluster

    @steps_checker.step
    def update_cluster(self, cluster, new_data, check=True, **kwargs):
        """Step to update cluster.

        Args:
            cluster (dict|str): cluster dict or id
            new_data (dict): new data for the cluster
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: model of the updated cluster

        Raises:
            AssertionError: if check failed
        """
        if not isinstance(cluster, dict):
            cluster = self.get_cluster(cluster)

        cluster['data'].update(new_data)

        cluster = self._client.update_cluster(cluster, **kwargs)

        if check:
            assert_that(cluster['data'], has_entries(new_data))

        return cluster

    @steps_checker.step
    def delete_cluster(self, cluster_id, check=True, **kwargs):
        """Step to delete cluster.

        Args:
            cluster_id (str): cluster id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Raises:
            TimeoutExpired: if check failed
        """
        self._client.delete_cluster(cluster_id, **kwargs)

        if check:
            self.check_resource_presence(cluster_id, self._client.get_cluster,
                                         must_present=False)

    @steps_checker.step
    def get_clusters(self, check=True, **kwargs):
        """Step to retrieve clusters.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            list: list of clusters

        Raises:
            AssertionError: if check failed
        """
        clusters = self._client.get_clusters(**kwargs)['items']

        if check:
            assert_that(clusters, is_not(empty()))

        return clusters

    @steps_checker.step
    def get_cluster(self, cluster_id, check=True, **kwargs):
        """Step to retrieve cluster.

        Args:
            cluster_id (str): cluster id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: model of the cluster

        Raises:
            AssertionError: if check failed
        """
        cluster = self._client.get_cluster(cluster_id, **kwargs)

        if check:
            assert_that(cluster['id'], equal_to(cluster_id))

        return cluster

    @steps_checker.step
    def get_cluster_by_name(self, cluster_name, check=True):
        """Step to retrieve cluster by name.

        Args:
            cluster_name (str): cluster name
            check (bool): flag whether to check step or not

        Returns:
            dict: model of cluster

        Raises:
            AssertionError: if check failed
        """
        return self.get_resource_by_field(
            cluster_name, self.get_clusters, check=check)
