"""
-------------------------
Decapod UI steps for role
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


class RoleSteps(base.BaseSteps):
    """Role steps."""

    def _page_roles(self):
        """Open roles page if it isn't opened."""
        self.app.page_base.header.link_users_management.click()
        self.app.page_base.users_management_header.link_roles.click()
        return self.app.page_roles

    @steps_checker.step
    def create_role(self, role_name=None, check=True):
        """Step to create role.

        Args:
            role_name (str): role name
            check (bool, optional): flag whether to check step or not

        Returns:
            str: role name

        Raises:
            Exception: if role is not present on page
        """
        role_name = role_name or next(utils.generate_ids())

        page_roles = self._page_roles()

        page_roles.button_create_role.click()
        page_roles.form_create_role.field_role_name.value = role_name
        page_roles.form_create_role.submit(modal_absent=False)

        if check:
            page_roles.table_roles.header.cell(role_name).wait_for_presence()

        return role_name
