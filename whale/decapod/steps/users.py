"""
----------
User steps
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

from hamcrest import assert_that, empty, equal_to, is_not  # noqa H301
from stepler.third_party import steps_checker

from whale import base

__all__ = [
    'UserSteps'
]


class UserSteps(base.BaseSteps):
    """User steps."""

    @steps_checker.step
    def create_user(self, user_login, user_email, user_full_name,
                    role_id=None, check=True, **kwargs):
        """Step to create new user.

        Args:
            user_login (str): the new login of the user
            user_email (str): the new email of the user
            user_full_name (str): the new full name of the user
            role_id (str): the new role id of the user
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            user (dict): model of new user

        Raises:
            TimeoutExpired|AssertionError: if check was triggered to an error
        """
        user = self._client.create_user(login=user_login,
                                        email=user_email,
                                        full_name=user_full_name,
                                        role_id=role_id,
                                        **kwargs)

        if check:
            self.check_resource_presence(user['id'], self._client.get_user)
            assert_that(user['data']['login'], equal_to(user_login))
            assert_that(user['data']['email'], equal_to(user_email))
            assert_that(user['data']['full_name'], equal_to(user_full_name))
            if role_id:
                assert_that(user["data"]["role_id"], equal_to(role_id))

        return user

    @steps_checker.step
    def delete_user(self, user_id, check=True, **kwargs):
        """Step to delete user.

        Args:
            user_id (str): user id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments
        """
        self._client.delete_user(user_id, **kwargs)

        if check:
            self.check_resource_presence(user_id, self._client.get_user,
                                         must_present=False)

    @steps_checker.step
    def get_users(self, check=True, **kwargs):
        """Step to get users.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            users (list): list of dicts of existing users

        Raises:
            AssertionError: if check failed
        """
        users = self._client.get_users(**kwargs)['items']

        if check:
            assert_that(users, is_not(empty()))

        return users

    @steps_checker.step
    def get_user_by_login(self, user_login, check=True):
        """Step to retrieve user by login.

        Args:
            user_login (str): user login
            check (bool): flag whether to check step or not

        Returns:
            user (dict): model of user

        Raises:
            AssertionError: if check failed
        """
        return self.get_resource_by_field(user_login, self.get_users,
                                          field_name='login', check=check)
