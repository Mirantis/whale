"""
----------
Role tests
----------
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


@pytest.mark.idempotent_id('338fa783-4c06-481c-a978-a7201f440946')
def test_create_and_delete(role_steps):
    """**Scenario:** Check creating and deleting of role.

    **Steps:**

    #. Create role
    #. Delete role
    """
    role = role_steps.create_role()
    role_steps.delete_role(role['id'])


@pytest.mark.idempotent_id('8b64c9e9-8fae-4fe7-90bc-920e5b9fd32f')
def test_update_role(role, role_steps):
    """**Scenario:** Check role updating.

    **Setup:**

    #. Create role

    **Steps:**

    #. Update role with the new name

    **Teardown:**

    #. Delete role
    """
    new_data = {'name': next(utils.generate_ids('new_name'))}
    role_steps.update_role(role=role, new_data=new_data)


@pytest.mark.idempotent_id('876661aa-de0b-4b5e-81a6-0e725f08613b')
def test_get_role(role, role_steps):
    """**Scenario:** Check role getting.

    **Setup:**

    #. Create role

    **Steps:**

    #. Get role by id

    **Teardown:**

    #. Delete role
    """
    role_steps.get_role(role['id'])


@pytest.mark.idempotent_id('6cbbc03f-051f-40af-9897-b5213bf72d99')
def test_list_roles(role_steps):
    """**Scenario:** Check getting of all roles.

    **Steps:**

    #. List all roles
    """
    role_steps.get_roles()


@pytest.mark.idempotent_id('ca697d9a-0dd4-4c3d-8a9c-0c1225b194fd')
def test_list_permissions(role_steps):
    """**Scenario:** Check getting all role permissions.

    **Steps:**

    #. List all role permissions
    """
    role_steps.get_permissions()
