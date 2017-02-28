"""
--------------------
User Management page
--------------------
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

from pom import ui
from selenium.webdriver.common.by import By

from whale.decapod_ui.app.pages import base
from whale.decapod_ui.app import ui as _ui


@ui.register_ui(navigate_menu=_ui.NavigateMenu(
    By.XPATH, '//ul[@class="col-xs-12 navigation"]/li'))
class PageUserManagement(base.PageBase):
    """User Management page."""

    url = '/'
    navigate_items = None

    def navigate(self, navigate_items):
        """Open page via navigation menu."""
        self.navigate_menu.go_to(navigate_items)
