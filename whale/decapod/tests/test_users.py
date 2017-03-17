"""
----------
User tests
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


@pytest.mark.idempotent_id('a9c69976-e661-42bb-9fbc-9afa3d30f3e8')
def test_create_delete_user(user_steps):
    """**Scenario:** Check user creation and deletion.

    **Steps:**

    #. Create user
    #. Delete user
    """
    user = user_steps.create_user()
    user_steps.delete_user(user['id'])


@pytest.mark.idempotent_id('28eb8dbb-a5ae-480a-a09a-1694b08736bc')
def test_update_user(user, user_steps):
    """**Scenario:** Check updating of user.

    **Setup:**

    #. Create user

    **Steps:**

    #. Update user with new login, email and full name

    **Teardown:**

    #. Delete user
    """
    new_data = {'login': next(utils.generate_ids('login')),
                'email': next(utils.generate_ids('email')) + '@example.com',
                'full_name': next(utils.generate_ids('new_name'))}
    user_steps.update_user(user, new_data)


@pytest.mark.idempotent_id('af7aa0fe-a9ae-48ce-9ad9-a8ae0744d75b')
def test_get_user(user, user_steps):
    """**Scenario:** Check getting of user.

    **Setup:**

    #. Create user

    **Steps:**

    #. Get user by id

    **Teardown:**

    #. Delete user
    """
    user_steps.get_user(user['id'])


@pytest.mark.idempotent_id('a5d6e791-6f9e-4405-ae50-e38c32a80968')
def test_list_users(user_steps):
    """Scenario:** Check getting of all users.

    **Steps:**

    #. List all users
    """
    user_steps.get_users()
