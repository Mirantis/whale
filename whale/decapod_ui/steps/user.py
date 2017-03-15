"""
-------------------------
Decapod UI steps for user
-------------------------
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

from hamcrest import assert_that, equal_to  # noqa H301
from stepler.third_party import steps_checker
from stepler.third_party import utils

from whale.decapod_ui.steps import base


class UserSteps(base.BaseSteps):
    """User steps."""

    def _page_users(self):
        """Open users page if it isn't opened."""
        self.app.page_base.header.link_users_management.click()
        return self.app.page_users

    @steps_checker.step
    def create_user(self, role_name, login=None, full_name=None, check=True):
        """Step to create user.

        Args:
            role_name (str): role name of user
            login (str, optional): login of user
            name (str, optional): full name of user
            check (bool, optional): flag whether to check step or not

        Returns:
            str: user login

        Raises:
            Exception: if user is not present on page
        """
        login = login or next(utils.generate_ids())
        full_name = full_name or next(utils.generate_ids())

        page_users = self._page_users()
        page_users.button_create_user.click()
        with page_users.form_create_user as form:
            form.field_login.value = login
            form.field_full_name.value = full_name
            form.field_email.value = login + "@ex.com"
            form.combobox_role.value = role_name

            form.submit(modal_absent=False)

        if check:
            page_users.list_users.row(login).wait_for_presence()

        return login

    @steps_checker.step
    def update_user(self,
                    login,
                    new_login=None,
                    new_full_name=None,
                    new_email=None,
                    new_role_name=None,
                    check=True):
        """Step to update user.

        Args:
            login (str, optional): login of user to be changed
            new_login (str, optional): new login of user
            new_full_name (str, optional): new full name of user
            new_email (str, optional): new email of user
            new_role_name (str, optional): new role of user
            check (bool, optional): flag whether to check step or not

        Returns:
            str: user login

        Raises:
            Exception: if check failed
        """
        new_login = new_login or next(utils.generate_ids())
        new_full_name = new_full_name or next(utils.generate_ids())
        new_email = new_email or new_login + "@ex.com"

        page_users = self._page_users()
        page_users.list_users.row(login).maximize_icon.click()

        with page_users.form_user_details as form:
            form.field_login.value = new_login
            form.field_full_name.value = new_full_name
            form.field_email.value = new_email
            if new_role_name:
                form.combobox_role.value = new_role_name

            form.submit(modal_absent=False)

        page_users.list_users.row(new_login).minimize_icon.click()

        if check:
            page_users.list_users.row(login).wait_for_absence()
            page_users.list_users.row(new_login).wait_for_presence()

            page_users.list_users.row(new_login).maximize_icon.click()
            with page_users.form_user_details as form:
                assert_that(form.field_login.value, equal_to(new_login))
                assert_that(form.field_full_name.value,
                            equal_to(new_full_name))
                assert_that(form.field_email.value, equal_to(new_email))
                if new_role_name:
                    assert_that(form.combobox_role.value,
                                equal_to(new_role_name))

        return new_login

    @steps_checker.step
    def delete_user(self, login, check=True):
        """Step to delete user.

        Args:
            login (str): login of user to be deleted
            check (bool, optional): flag whether to check step or not

        Raises:
            Exception: if user is present on page
        """
        page_users = self._page_users()
        page_users.list_users.row(login).maximize_icon.click()

        page_users.form_user_details.cancel(modal_absent=False)
        page_users.form_confirm_user_deletion.submit(modal_absent=False)

        if check:
            page_users.list_users.row(login).wait_for_absence()
