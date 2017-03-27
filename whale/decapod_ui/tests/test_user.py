"""
-------------
User UI tests
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


@pytest.mark.idempotent_id('3476fac7-3415-4d99-92fd-41725a183044')
def test_create_user(role, user_steps, ui_user_steps):
    """**Scenario:** User may be created in UI.

    **Setup:**

    #. Create role using API

    **Steps:**

    #. Create user via UI
    #. Find user by login via API

    **Teardown:**

    #. Delete user via API
    #. Delete role using API
    """
    user_login = ui_user_steps.create_user(role['data']['name'])
    user_steps.get_user_by_login(user_login)


@pytest.mark.idempotent_id('04f33149-9d68-4caa-bb18-426bdaef959a')
def test_update_user(user, role_steps, user_steps, ui_user_steps):
    """**Scenario:** User may be updated in UI.

    **Setup:**

    #. Create role using API
    #. Create user via API

    **Steps:**

    #. Create new role using API
    #. Update user login, full name, email and role via UI
    #. Find user by login via API

    **Teardown:**

    #. Delete user via API
    #. Delete created roles using API
    """
    new_role = role_steps.create_role()
    user_login = ui_user_steps.update_user(
        user['data']['login'], new_role_name=new_role['data']['name'])
    user_steps.get_user_by_login(user_login)


@pytest.mark.idempotent_id('0cbf2e4c-c526-4b6b-b3cb-7b0fbe903ff9')
def test_delete_user(user, ui_user_steps):
    """**Scenario:** User may be deleted in UI.

    **Setup:**

    #. Create role using API
    #. Create user via API

    **Steps:**

    #. Delete user via UI

    **Teardown:**

    #. Delete role using API
    """
    ui_user_steps.delete_user(user['data']['login'])
