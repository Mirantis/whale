"""
----------------------------
Playbook configuration tests
----------------------------
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

from whale import config


@pytest.mark.idempotent_id('e9eeec46-6208-4301-b133-ac9a5de4eae0')
def test_create_delete_playbook_config(playbook_config_steps, cluster,
                                       server_steps):
    """**Scenario:** Check playbook configuration creation and deletion.

    **Setup:**

    #. Create cluster

    **Steps:**

    #. Get list of all servers
    #. Create playbook configuration
    #. Delete playbook configuration

    **Teardown:**

    #. Delete cluster
    """
    server_ids = server_steps.get_server_ids()
    playbook_id = config.PLAYBOOK_DEPLOY_CLUSTER
    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'], playbook_id=playbook_id,
        server_ids=server_ids)
    playbook_config_steps.delete_playbook_config(playbook_config['id'])


@pytest.mark.idempotent_id('6263626a-f2c4-4b34-a746-c3e8675b8ff5')
def test_update_playbook_config(playbook_config_steps, playbook_config):
    """**Scenario:** Check playbook configuration updating.

    **Setup:**

    #. Create playbook configuration

    **Steps:**

    #. Update playbook configuration with new name

    **Teardown:**

    #. Delete playbook configuration
    """
    new_data = {'name': next(utils.generate_ids('new_name'))}
    playbook_config = playbook_config_steps.update_playbook_config(
        playbook_config, new_data)


@pytest.mark.idempotent_id('c75fd086-d25b-4e30-b999-b421fc29b708')
def test_get_playbook_config(playbook_config_steps, playbook_config):
    """**Scenario:** Check playbook configuration getting.

    **Setup:**

    #. Create playbook configuration

    **Steps:**

    #. Get playbook configuration by its id

    **Teardown:**

    #. Delete playbook configuration
    """
    playbook_config_steps.get_playbook_config(playbook_config['id'])


@pytest.mark.idempotent_id('0f22c1f9-56ab-4d25-b262-590b9a64623d')
def test_list_playbook_configs(playbook_config, playbook_config_steps):
    """**Scenario:** Check getting of all playbook configurations.

    **Setup:**

    #. Create playbook configuration

    **Steps:**

    #. Check playbook configs is not empty

    **Teardown:**

    #. Delete playbook configuration
    """
    playbook_config_steps.get_playbook_configs()
