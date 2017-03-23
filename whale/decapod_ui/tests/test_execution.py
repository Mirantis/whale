"""
---------------
Execution tests
---------------
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


@pytest.mark.idempotent_id('d055a21c-8cbe-49ec-82eb-360d9973264d')
def test_create_execution_deploy_cluster(playbook_config,
                                         execution_steps,
                                         ui_configuration_steps):
    """**Scenario:** Execution for cluster deployment may be created in UI.

    **Setup:**

    #. Create cluster via API
    #. Create playbook `cluster deploy` configuration via API

    **Steps:**

    #. Create execution via UI
    #. Check execution was successfully completed via API

    **Teardown:**

    #. Delete playbook configuration via API
    #. Delete cluster via API
    """
    ui_configuration_steps.create_execution(playbook_config['data']['name'])

    execution = execution_steps.get_last_execution_by_config_id(
        playbook_config['id'])
    execution_steps.check_execution_status(execution['id'])


@pytest.mark.idempotent_id('539e6207-de8d-4fd6-aacf-4e1ba95b7892')
def test_create_execution_purge_cluster(cluster_steps,
                                        server_steps,
                                        playbook_config_steps,
                                        execution_steps,
                                        ui_configuration_steps):
    """**Scenario:** Execution for cluster deletion may be created in UI.

    **Steps:**

    #. Get available servers
    #. Create cluster via API
    #. Create playbook configuration for cluster deployment via API
    #. Create execution for cluster deployment via API
    #. Create playbook configuration for cluster deletion via API
    #. Create execution for cluster deletion via UI
    #. Check cluster has been deleted

    **Teardown:**

    #. Delete playbook configuration
    """
    server_ids = server_steps.get_server_ids()
    cluster = cluster_steps.create_cluster()

    playbook_config_deploy = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_DEPLOY_CLUSTER,
        server_ids=server_ids)

    execution_steps.create_execution(playbook_config_deploy['id'])

    playbook_config_purge = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_PURGE_CLUSTER,
        server_ids=[])

    ui_configuration_steps.create_execution(
        playbook_config_purge['data']['name'])
    execution = execution_steps.get_last_execution_by_config_id(
        playbook_config_purge['id'])
    execution_steps.check_execution_status(execution['id'])

    cluster_steps.check_cluster_presence(cluster['id'],
                                         must_present=False)
