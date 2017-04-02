"""
-------------
Role UI tests
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

from whale import config


@pytest.mark.idempotent_id('458f3541-5b4f-42be-92d4-8cc6f8cc6aa6')
def test_create_role(role_steps, ui_role_steps):
    """**Scenario:** Role may be created in UI.

    **Steps:**

    #. Create role via UI
    #. Find role by name via API

    **Teardown:**

    #. Delete role using API
    """
    role_name = ui_role_steps.create_role()
    role_steps.get_role_by_name(role_name)


@pytest.mark.idempotent_id('5bb8a647-738b-4c03-90a3-f73e0de2c6d3')
def test_update_role(role, role_steps, ui_role_steps):
    """**Scenario:** Role may be updated in UI.

    **Setup:**

    #. Create role with all permissions via API

    **Steps:**

    #. Check role has required permissions via API
    #. Update role using UI
    #. Check role's permissions has been changed via API

    **Teardown:**

    #. Delete role using API
    """
    api_permissions = [config.PERMISSION_CREATE_CLUSTER]
    playbook_permissions = [config.PERMISSION_CLUSTER_DEPLOY]

    for permission in api_permissions:
        role_steps.check_role_permission_presence(
            role['id'],
            permission=permission,
            group_name=config.PERMISSIONS_GROUP_API,
            must_present=True)
    for permission in playbook_permissions:
        role_steps.check_role_permission_presence(
            role['id'],
            permission=permission,
            group_name=config.PERMISSIONS_GROUP_PLAYBOOK,
            must_present=True)

    ui_role_steps.update_role(role['data']['name'],
                              api_permissions=api_permissions,
                              playbook_permissions=playbook_permissions)

    for permission in api_permissions:
        role_steps.check_role_permission_presence(
            role['id'],
            permission=permission,
            group_name=config.PERMISSIONS_GROUP_API,
            must_present=False)
    for permission in playbook_permissions:
        role_steps.check_role_permission_presence(
            role['id'],
            permission=permission,
            group_name=config.PERMISSIONS_GROUP_PLAYBOOK,
            must_present=False)


@pytest.mark.idempotent_id('f1bc17dc-6bda-4ed6-8408-e2cb4af2cdca')
def test_delete_role(role, ui_role_steps):
    """**Scenario:** Role may be deleted in UI.

    **Setup:**

    #. Create role via API

    **Steps:**

    #. Delete role using API
    """
    ui_role_steps.delete_role(role['data']['name'])
