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
from stepler.third_party import utils


@pytest.mark.idempotent_id('fe62201b-de1f-4f13-bbfc-4a43a0603dc7')
def test_create_delete_cluster(cluster_steps):
    """**Scenario:** Check cluster deletion.

    **Steps:**

    #. Create cluster
    #. Delete cluster
    """
    cluster = cluster_steps.create_cluster()
    cluster_steps.delete_cluster(cluster)


@pytest.mark.idempotent_id('82ea75ee-240e-43d6-b6f6-3e5ce2576d52')
def test_update_cluster(cluster_steps, cluster):
    """**Scenario:** Check cluster update.

    **Setup:**

    #. Create cluster

    **Steps:**

    #. Update cluster

    **Teardown:**

    #. Delete cluster
    """
    new_cluster_name = next(utils.generate_ids('cluster'))
    cluster_steps.update_cluster(cluster, new_cluster_name)