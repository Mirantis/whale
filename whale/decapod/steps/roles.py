"""
----------
Role steps
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

from hamcrest import (assert_that, empty, equal_to, has_entries,
                      is_not)  # noqa H301
from stepler.third_party import steps_checker
from stepler.third_party import utils

from whale import base

__all__ = [
    'RoleSteps'
]


class RoleSteps(base.BaseSteps):
    """Role steps."""

    @steps_checker.step
    def create_role(self, role_name=None, permissions=None, check=True,
                    **kwargs):
        """Step to create role.

        Args:
            role_name (str|None): the name of the role
            permissions (list|None): the list of the role permissions
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: model of the role

        Raises:
            TimeoutExpired: if check failed after timeout
        """
        role_name = role_name or next(utils.generate_ids('role'))
        permissions = permissions or self.get_permissions()

        role = self._client.create_role(role_name, permissions, **kwargs)

        if check:
            self.check_resource_presence(role['id'], self._client.get_role)
            assert_that(role['data']['name'], equal_to(role_name))
            assert_that(sorted(role['data']['permissions']),
                        equal_to(sorted(permissions)))

        return role

    @steps_checker.step
    def update_role(self, role, new_data, check=True, **kwargs):
        """Step to update role with new data.

        Args:
            role (dict|str): role or its id
            new_data (dict): new data for role
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: model of updated role

        Raises:
            AssertionError: if check failed
        """
        if not isinstance(role, dict):
            role = self.get_role(role)

        role['data'].update(new_data)

        role = self._client.update_role(role, **kwargs)

        if check:
            assert_that(role['data'], has_entries(new_data))

        return role

    @steps_checker.step
    def delete_role(self, role_id, check=True, **kwargs):
        """Step to delete role.

        Args:
            role_id (str): role id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Raises:
            TimeoutExpired: if check failed
        """
        self._client.delete_role(role_id, **kwargs)

        if check:
            self.check_resource_presence(role_id, self._client.get_role,
                                         must_present=False)

    @steps_checker.step
    def get_role(self, role_id, check=True, **kwargs):
        """Step to retrieve role.

        Args:
            role_id (str): role id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: model of the role
        """
        role = self._client.get_role(role_id, **kwargs)

        if check:
            assert_that(role['id'], equal_to(role_id))

        return role

    @steps_checker.step
    def get_roles(self, check=True, **kwargs):
        """Step to get list of all roles.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            list: list of roles

        Raises:
            AssertionError: if check was triggered to an error
        """
        roles = self._client.get_roles(**kwargs)['items']

        if check:
            assert_that(roles, is_not(empty()))

        return roles

    @steps_checker.step
    def get_permissions(self, check=True, **kwargs):
        """Step to retrieve permissions.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            list: a list of permissions
        """
        permissions = self._client.get_permissions(**kwargs)['items']

        if check:
            assert_that(permissions, is_not(empty()))

        return permissions
