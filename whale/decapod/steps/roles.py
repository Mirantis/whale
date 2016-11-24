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

from hamcrest import (equal_to, assert_that,
                      has_properties, is_not, empty)  # noqa
from decapodlib import exceptions

from stepler.base import BaseSteps
from stepler.third_party.matchers import expect_that
from stepler.third_party import steps_checker
from stepler.third_party import waiter

__all__ = [
    'RoleSteps'
]


class RoleSteps(BaseSteps):
    """Role steps."""

    @steps_checker.step
    def create_role(self, role_name, permissions, check=True, **kwargs):
        """Step to create role.

        Args:
            role_name (str): the name of the role
            permissions (dict): the dict of the role permission
            check (bool): flag whether to check step or not
            **kwargs: any suitable to role keyword arguments

        Returns:
            role (dict): model of the role

        Raises:
            TimeoutExpired: if check failed after timeout
        """
        role = self._client.create_role(role_name, permissions, **kwargs)

        if check:
            self.check_role_presence(role['id'])
        return role

    @steps_checker.step
    def delete_role(self, role_id, check=True, **kwargs):
        """Step to delete role.

        Args:
            role_id (str): role id
            check (bool): flag whether to check step or not
            **kwargs: any suitable to role keyword arguments

        Raises:
            TimeoutExpired|AssertionError: if check failed
        """
        self._client.delete_role(role_id, **kwargs)
        if check:
            self.check_role_presence(role_id, must_present=False)

    @steps_checker.step
    def get_role(self, check=True, **kwargs):
        """Step to retrieve role.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable to role keyword arguments

        Returns:
            role (dict): model of the role
        """
        role = self._client.get_role(**kwargs)
        if check:
            assert_that(role, has_properties(**kwargs))

        return role

    @steps_checker.step
    def get_role_id(self, name, check=True, **kwargs):
        """Step to retrieve role id.

        Args:
            name (str): role name
            check (bool): flag whether to check step or not
            **kwargs: any suitable to role keyword arguments

        Returns:
            role_id (str): role id
        """
        roles = self._client.get_roles(**kwargs)
        for role in roles['items']:
            if role['data']['name'] == name:
                role_id = role['id']

        if check:
            assert_that(role_id, is_not(empty()))

        return role_id

    @steps_checker.step
    def get_permissions(self, check=True, **kwargs):
        """Step to retrieve permission.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable to role keyword arguments

         Returns:
            permissions (dict):  a dict of permissions

        """
        permissions = self._client.get_permissions(**kwargs)

        if check:
            assert_that(permissions, is_not(empty()))

        return permissions['items']

    @steps_checker.step
    def check_role_presence(self, role_id, must_present=True, timeout=0):
        """Check step that role is present.

        Args:
            role_id (str or obj): the role to be checked on the server
            must_present (bool): flag whether role should present or no
            timeout (int): seconds to wait a result of check

        Raises:
            TimeoutExpired/DecapodAPIError: if check failed after timeout or
            API response exception
        """

        def _check_role_presence():
            try:
                role = self._client.get_role(role_id)
                if role['time_deleted'] == 0:
                    is_present = True
                if role['time_deleted'] != 0:
                    is_present = False
            except exceptions.DecapodAPIError:
                is_present = False

            return expect_that(is_present, equal_to(must_present))

        waiter.wait(_check_role_presence, timeout_seconds=timeout)
