"""
-----------
Custom form
-----------
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

from whale import config


class Form(ui.Form):
    """Custom form."""

    timeout = config.ACTION_TIMEOUT

    submit_locator = By.CSS_SELECTOR, 'button#save'
    cancel_locator = By.CSS_SELECTOR, 'button#close'

    def _click_button_by_locator(self,
                                 locator,
                                 modal_absent=True,
                                 modal_timeout=None):
        """Find button by locator and click it."""
        button = ui.Button(*locator)
        button.container = self
        button.click()

        if modal_absent:
            self._modal.wait_for_absence(timeout=modal_timeout)

    @pom.timeit
    @ui.wait_for_presence
    def submit(self, modal_absent=True, modal_timeout=None):
        """Submit form."""
        self._click_button_by_locator(self.submit_locator,
                                      modal_absent,
                                      modal_timeout)

    @pom.timeit
    @ui.wait_for_presence
    def cancel(self, modal_absent=True):
        """Cancel form."""
        self._click_button_by_locator(self.cancel_locator,
                                      modal_absent)

    @property
    @pom.cache
    def _modal(self):
        container = self.container
        while True:
            ui = getattr(container, 'modal', None)
            if ui:
                return ui
            else:
                container = container.container


class FormNext(Form):
    """Form with next button."""

    next_locator = By.CSS_SELECTOR, 'button#next'

    @pom.timeit
    @ui.wait_for_presence
    def next(self, modal_absent=True, modal_timeout=None):
        """Go to the next form."""
        self._click_button_by_locator(self.next_locator,
                                      modal_absent,
                                      modal_timeout)


class FormConfirm(Form):
    """Form to confirm action."""

    submit_locator = By.CSS_SELECTOR, 'button.btn.btn-primary'
    cancel_locator = By.CSS_SELECTOR, 'button.btn.btn-default'
