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


@pytest.mark.idempotent_id('d055a21c-8cbe-49ec-82eb-360d9973264d')
def test_create_execution_deploy_cluster(playbook_config,
                                         execution_steps,
                                         ui_configuration_steps):
    """**Scenario:** Execution may be created in UI.

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
