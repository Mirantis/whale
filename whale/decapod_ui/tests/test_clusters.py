"""
-------------
Cluster tests
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

import pytest


@pytest.mark.idempotent_id('38036bb4-1afb-4344-acaf-2558099bfbef')
def test_create_cluster(ui_cluster_steps, cluster_steps):
    """**Scenario:** Cluster may be created in UI.

    **Steps:**

    #. Create cluster via UI
    #. Find cluster by name via API
    #. Delete cluster via API
    """
    cluster_name = ui_cluster_steps.create_cluster()
    cluster_id = cluster_steps.get_cluster_id(cluster_name)
    cluster_steps.delete_cluster(cluster_id)


@pytest.mark.idempotent_id('a660cc41-6be4-4bb4-b03d-ccab363a6891')
def test_update_cluster(cluster, ui_cluster_steps, cluster_steps):
    """**Scenario:** Cluster may be updated in UI.

    **Setup:**

    #. Create cluster via API

    **Steps:**

    #. Update cluster name via UI
    #. Find cluster by name via API

    **Teardown:**

    #. Delete cluster via API
    """
    cluster_name = ui_cluster_steps.update_cluster(cluster['data']['name'])
    cluster_steps.get_cluster_id(cluster_name)
