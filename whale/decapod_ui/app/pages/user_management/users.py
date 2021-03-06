"""
----------
Users page
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

from pom import ui
from selenium.webdriver.common.by import By

from whale.decapod_ui.app.pages import base
from whale.decapod_ui.app import ui as _ui


@ui.register_ui(
    label_login=ui.UI(By.CSS_SELECTOR, "div.name"),
    maximize_icon=ui.UI(
        By.XPATH, './/span[@class="glyphicon glyphicon-triangle-right"]'),
    minimize_icon=ui.UI(
        By.XPATH, './/span[@class="glyphicon glyphicon-triangle-bottom"]'))
class RowUser(ui.Row):
    """Row of user."""


class ListUsers(ui.List):
    """List of users."""

    row_cls = RowUser
    row_xpath = './/div[contains(@class, "box")]'


@ui.register_ui(
    field_login=ui.TextField(By.ID, 'user_login'),
    field_full_name=ui.TextField(By.ID, 'user_name'),
    field_email=ui.TextField(By.ID, 'user_email'),
    combobox_role=_ui.ComboBox(By.ID, 'user_role'))
class FormCreateUser(_ui.Form):
    """Form to create user."""


class FormUserDetails(FormCreateUser):
    """Form to change user details."""

    submit_locator = By.CSS_SELECTOR, 'button.btn.btn-primary.pull-right'
    cancel_locator = By.CSS_SELECTOR, 'button.btn.btn-danger'


@ui.register_ui(
    button_create_user=ui.Button(
        By.CSS_SELECTOR, "div.main-button > button.btn-primary"),
    form_create_user=FormCreateUser(By.CSS_SELECTOR, "div.modal-content"),
    list_users=ListUsers(By.CSS_SELECTOR, "div.col-xs-12"),
    form_user_details=FormUserDetails(By.CSS_SELECTOR, "div.box.open"),
    form_confirm_user_deletion=_ui.FormConfirm(
        By.XPATH,
        './/div[@class="modal-content" and contains(.//*, "Delete user")]'))
class PageUsers(base.PageBase):
    """Page for users."""

    url = "/admin/users"
    page_header_value = "User"
