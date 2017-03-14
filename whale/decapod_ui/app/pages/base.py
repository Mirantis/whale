"""
-------------------------
Base page of user account
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

import pom
from pom import ui
from selenium.webdriver.common.by import By

from whale.decapod_ui.app import ui as _ui


@ui.register_ui(
    link_clusters=ui.Link(By.CSS_SELECTOR, 'a[href="/clusters"]'),
    link_users_management=ui.Link(By.CSS_SELECTOR, 'a[href="/admin"]'))
class Header(ui.Block):
    """Header block."""


@ui.register_ui(
    current_user=ui.Link(
        By.XPATH, '//div[@class="current-user"]/a[1]'),
    logout=ui.Link(
        By.XPATH, '//div[@class="current-user"]/a[2]'),
    navigate_menu=_ui.NavigateMenu(
        By.XPATH, './/ul[@class="col-xs-8 navigation"]/li'),
    header=Header(By.CSS_SELECTOR, "div.header"))
class PageBase(pom.Page):
    """Base page of user account."""

    url = '/'

    page_header_value = None
    _page_header_selector = '//h1[contains(text(),"{}")]'

    navigate_items = None

    def navigate(self, navigate_items):
        """Open page via navigation menu."""
        self.navigate_menu.go_to(navigate_items)

    @property
    def page_header(self):
        return ui.UI(By.XPATH,
                     self._page_header_selector.format(
                         self.page_header_value))
