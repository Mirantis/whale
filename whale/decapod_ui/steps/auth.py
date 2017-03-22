"""
--------------------------------
Decapod steps for authentication
--------------------------------
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

import base
from whale import config


class AuthSteps(base.BaseSteps):
    """Authentication steps."""

    def _page_login(self):
        """Open login page if it's not opened."""
        return self._open(self.app.page_login)

    @steps_checker.step
    def login(self, username=config.DECAPOD_LOGIN,
              password=config.DECAPOD_PASSWORD, check=True):
        """Step to log in user account.

        Arguments:
            - username: string, user name.
            - password: string, user password.
        """
        with self._page_login().form_login as form:
            form.field_username.value = username
            form.field_password.value = password
            form.submit()
            self.app.current_username = username

        if check:
            self.app.page_base.current_user.wait_for_presence(30)

    @steps_checker.step
    def logout(self, check=True):
        """Step to log out user account."""
        self.app.page_base.logout.click()
        self.app.current_username = None

        if check:
            self.app.page_login.form_login.wait_for_presence(30)

    @steps_checker.step
    def check_alert_present(self):
        """Step to check alert message is present."""
        self._page_login().label_alert_message.wait_for_presence()
