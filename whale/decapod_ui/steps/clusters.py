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

from stepler.third_party import steps_checker
from stepler.third_party import utils

from whale.decapod_ui.steps import base

__all__ = ['ClusterSteps']


class ClusterSteps(base.BaseSteps):
    """Cluster steps."""

    def _clusters_page(self):
        self.app.page_base.header.link_clusters.click()
        return self.app.page_clusters

    @steps_checker.step
    def create_cluster(self, name=None, check=True):
        """Step to create cluster.

        Args:
            name (str, optional): name of cluster
            check (bool, optional): flag whether to check step or not

        Returns:
            str: cluster name

        Raises:
            Exception: if cluster is not present on page
        """
        name = name or next(utils.generate_ids())
        # only letters and digits are allowed for cluster name
        name = name.replace('-', '')

        page = self._clusters_page()
        page.button_create_cluster.click()
        page.form_create_cluster.field_name.value = name
        page.form_create_cluster.submit(modal_absent=False)

        if check:
            page.list_clusters.row(name).wait_for_presence()

        return name

    @steps_checker.step
    def update_cluster(self, name, new_name=None, check=True):
        """Step to create cluster.

        Args:
            name (str): name of cluster to be updated
            new_name (str, optional): name of cluster after update
            check (bool, optional): flag whether to check step or not

        Returns:
            str: cluster name

        Raises:
            Exception: if cluster name was not changed
        """
        new_name = new_name or next(utils.generate_ids())
        # only letters and digits are allowed for cluster name
        new_name = new_name.replace('-', '')

        page = self._clusters_page()
        page.list_clusters.row(name).edit_icon.click()
        page.form_create_cluster.field_name.value = new_name

        page.form_create_cluster.submit(modal_absent=False)

        if check:
            page.list_clusters.row(name).wait_for_absence()
            page.list_clusters.row(new_name).wait_for_presence()

        return new_name
