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

from stepler.third_party import utils

from whale.decapod import steps

__all__ = [
    'get_user_steps',
    'user_steps',
    'create_user',
    'user',
]


@pytest.fixture(scope="session")
def get_user_steps(get_decapod_client):
    """Callable session fixture to get users steps.

    Args:
        get_decapod_client (function): function to get decapod client.

    Returns:
        function: function to get users steps.
    """
    def _get_steps():
        return steps.UserSteps(get_decapod_client())

    return _get_steps


@pytest.fixture
def user_steps(get_user_steps):
    """Function fixture to get user steps.

    Args:
        get_user_steps (function): function to get user steps

    Returns:
        user_steps (object): instantiated user steps
    """
    return get_user_steps()


@pytest.yield_fixture
def create_user(user_steps):
    """Callable fixture to create user with options.

    Can be called several times during a test.
    After the test it destroys all created users.

    Args:
        user_steps (object): instantiated user steps

    Yields:
        function: function to create user with options

    """
    users = []

    def _create_user(*args, **kwargs):
        user = user_steps.create_user(*args, **kwargs)
        users.append(user)
        return user

    yield _create_user

    for user in users:
        user_steps.delete_user(user['id'])


@pytest.fixture
def user(role, create_user):
    """Function fixture to create user with default options before test.

    Args:
        role (dict): model of the role
        create_user (function): function to create user with options

    Returns:
        json model: model of new user
    """
    user_name = next(utils.generate_ids('user'))
    return create_user(user_name=user_name,
                       full_name=next(utils.generate_ids('full_name')),
                       email='{0}@example.com'.format(user_name),
                       role_id=role['id'])
