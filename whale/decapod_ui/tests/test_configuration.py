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

from whale import config


@pytest.mark.idempotent_id('cf029aa7-9f5f-4695-9b69-77dbcc1eefe9')
def test_create_config_deploy_cluster(cluster,
                                      playbook_steps,
                                      server_steps,
                                      playbook_config_steps,
                                      ui_configuration_steps):
    """**Scenario:** Playbook configuration may be created in UI.

    **Setup:**

    #. Create cluster via API

    **Steps:**

    #. Get servers list via API
    #. Find playbook name by ID using API
    #. Create playbook `cluster deploy` configuration via UI

    **Teardown:**

    #. Delete playbook configuration via API
    #. Delete cluster via API
    """
    servers = server_steps.get_servers()
    playbook_config = playbook_steps.get_playbook(
        config.PLAYBOOK_DEPLOY_CLUSTER)
    ui_configuration_steps.create_deploy_configuration(playbook_config['name'],
                                                       cluster['data']['name'],
                                                       servers)
