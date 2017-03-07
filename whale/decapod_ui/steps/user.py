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
