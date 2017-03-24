"""
-------------
User fixtures
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

from whale.decapod import steps

__all__ = [
    'get_user_steps',
    'user_steps',
    'user',
    'cleanup_users',
]


@pytest.fixture(scope="session")
def get_user_steps(get_decapod_client):
    """Callable session fixture to get users steps.

    Args:
        get_decapod_client (function): function to get decapod client.

    Returns:
        function: function to get users steps.
    """
    def _get_user_steps():
        return steps.UserSteps(get_decapod_client())

    return _get_user_steps


@pytest.fixture
def user_steps(get_user_steps, cleanup_users):
    """Function fixture to get user steps.

    Args:
        get_user_steps (function): function to get user steps
        cleanup_users (function): function to cleanup users after test

    Yields:
        object: instantiated user steps
    """
    _user_steps = get_user_steps()
    users = _user_steps.get_users(check=False)
    users_ids_before = {user['id'] for user in users}

    yield _user_steps

    cleanup_users(_user_steps, uncleanable_ids=users_ids_before)


@pytest.fixture
def user(role, user_steps):
    """Function fixture to create user with default options before test.

    Args:
        role (dict): model of the role
        user_steps (obj): instantiated user steps

    Returns:
        dict: model of new user
    """
    return user_steps.create_user(role_id=role['id'])


@pytest.fixture(scope='session')
def cleanup_users():
    """"Callable session fixture to cleanup users."""
    def _cleanup_users(_users_steps, uncleanable_ids=None):
        uncleanable_ids = uncleanable_ids or []
        for user in _users_steps.get_users(check=False):
            if user['id'] not in uncleanable_ids:
                _users_steps.delete_user(user['id'])

    return _cleanup_users
