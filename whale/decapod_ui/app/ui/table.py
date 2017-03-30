"""
------------------
Custom table block
------------------
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
from pom.ui import table as ui_table
from selenium.webdriver.common.by import By


def _merge_xpath(xpath, attr):
    if xpath.endswith(']'):
        return xpath[:-1] + ' and {}]'.format(attr)
    else:
        return xpath + '[{}]'.format(attr)


class ListField(ui.List):
    """Custom row class to get row by field value"""

    def row(self, *args):
        """Get row of table by field name and value."""

        xpath = self.row_xpath
        for name, value in args:
            xpath = _merge_xpath(xpath, '@{0}="{1}"'.format(name, value))

        row = self.row_cls(By.XPATH, xpath)
        row.container = self
        return row


class _CellIndexMixin(ui_table._CellsMixin):
    """Cell mixin to add index to columns dict if it doesn't exist."""

    element_xpath = './/div[@title="{}"]'

    def get_index(self, name):
        """Get index by cell name."""
        locator = By.XPATH, '*'
        elements = self.find_elements(locator)

        element = ui.Block(By.XPATH, self.element_xpath.format(name))
        element.container = self

        if element.webelement in elements:
            result = elements.index(element.webelement) + 1
        else:
            result = -1

        return result

    def cell(self, name):
        """Get cell by name."""
        self.container.columns = self.container.columns or {}

        index = self.get_index(name)
        self.container.columns[name] = index

        return super(_CellIndexMixin, self).cell(name)


class Header(ui_table.Header, _CellIndexMixin):
    """Custom header."""
