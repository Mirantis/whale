"""
-------------
Role fixtures
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
    'get_role_steps',
    'role_steps',
    'role',
    'cleanup_roles',
]


@pytest.fixture(scope="session")
def get_role_steps(get_decapod_client):
    """Callable session fixture to get role steps.

    Args:
        get_decapod_client (function): function to get decapod client

    Returns:
        function: function to get role steps
    """
    def _get_role_steps():
        return steps.RoleSteps(get_decapod_client())

    return _get_role_steps


@pytest.fixture
def role_steps(get_role_steps, cleanup_roles):
    """Function fixture to get role steps.

    Args:
        get_role_steps (function): function to get role steps
        cleanup_roles (function): function to cleanup roles after test

    Returns:
        RoleSteps: instantiated role steps
    """
    _role_steps = get_role_steps()
    roles = _role_steps.get_roles(check=False)
    roles_ids_before = {role['id'] for role in roles}

    yield _role_steps

    cleanup_roles(_role_steps, uncleanable_ids=roles_ids_before)


@pytest.fixture
def role(role_steps):
    """Fixture to create role with default options before test.

    Args:
        role_steps (obj): instantiated role steps

    Returns:
        dict: model of the role
    """
    return role_steps.create_role()


@pytest.fixture(scope='session')
def cleanup_roles():
    """"Callable session fixture to cleanup roles."""
    def _cleanup_roles(_roles_steps, uncleanable_ids=None):
        uncleanable_ids = uncleanable_ids or []
        for role in _roles_steps.get_roles(check=False):
            if role['id'] not in uncleanable_ids:
                _roles_steps.delete_role(role['id'])

    return _cleanup_roles
