"""
-------------
Navigate menu
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

import pom
from pom import ui
from selenium.webdriver.common.by import By


class NavigateMenu(ui.Block):
    """Navigate menu."""

    _item_selector = '//li/a[contains(text(),"{}")]'

    @pom.timeit
    def go_to(self, item_names):
        """Go to page via navigate menu.

        Arguments:
            - item_names: list of items of navigate menu.
        """
        container = self
        last_name = item_names[-1]

        for item_name in item_names:
            item = ui.UI(By.XPATH, self._item_selector.format(item_name))
            item.container = container

            if item_name == last_name:
                item.click()
                break
