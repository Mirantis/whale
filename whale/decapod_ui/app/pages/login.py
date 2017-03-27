"""
----------
Login page
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

import pom
from pom import ui
from selenium.webdriver.common.by import By

from whale.decapod_ui.app import ui as _ui


@ui.register_ui(field_username=ui.TextField(By.NAME, 'username'),
                field_password=ui.TextField(By.NAME, 'password'))
class FormLogin(_ui.Form):
    """Form to login user."""

    submit_locator = By.CSS_SELECTOR, '.btn.btn-primary'
    cancel_locator = By.CSS_SELECTOR, '.btn.cancel'


@ui.register_ui(
    form_login=FormLogin(By.CSS_SELECTOR, 'form'),
    label_alert_message=ui.UI(By.CSS_SELECTOR, 'div.alert-message'),
    label_error_message=ui.UI(By.CSS_SELECTOR, 'div.error'),
    modal=_ui.initiated_ui.Modal(By.CLASS_NAME, 'modal-backdrop'))
class PageLogin(pom.Page):
    """Page to login user."""

    url = "/login"
