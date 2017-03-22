"""
-------------------
Configurations page
-------------------
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
    button_execute_config=ui.Button(By.CSS_SELECTOR, 'button.btn.btn-success'),
    button_edit_config=ui.Button(
        By.XPATH, './/button[contains(@class, "btn-primary") and '
                  'contains(text(), "Edit")]'),
    button_view_config=ui.Button(
        By.XPATH, './/button[contains(@class, "btn-primary") and '
                  'contains(text(), "View")]'),
    button_delete_config=ui.Button(By.CSS_SELECTOR, 'button.btn.btn-danger'))
class RowConfiguration(ui.Row):
    """Row of configuration."""


class ListConfigurations(ui.List):
    """List of configurations."""

    row_cls = RowConfiguration
    row_xpath = './/div[contains(@class, "box")]'


@ui.register_ui(
    field_name=ui.TextField(By.ID, 'configuration_name'),
    combobox_cluster=_ui.ComboBox(By.ID, 'configuration_cluster'))
class FormCreateConfiguration(_ui.Form):
    """Form to create configuration."""

    submit_locator = By.CSS_SELECTOR, 'button#next'
    cancel_locator = By.CSS_SELECTOR, 'button#close'


@ui.register_ui(
    radiobutton=ui.Button(By.XPATH, './/input[@type="radio"]'))
class RowPlaybook(ui.Row):
    """Row of playbook."""


class ListPlaybooks(ui.List):
    """List of playbooks."""

    row_cls = RowPlaybook
    row_xpath = './/div[contains(@class, "grid-line")]'


@ui.register_ui(
    radiobutton_playbooks=ListPlaybooks(By.CSS_SELECTOR, 'div.col-xs-12.grid'))
class FormPlaybookConfiguration(_ui.Form):
    """Form to choose playbook for configuration."""

    submit_locator = By.CSS_SELECTOR, 'button#next'
    cancel_locator = By.CSS_SELECTOR, 'button#close'


@ui.register_ui(
    field_monitors_count=ui.TextField(By.XPATH, './/input[@id="mon_count"]'))
class FormPlaybookParameters(_ui.Form):
    """Form to choose playbook parameters."""

    submit_locator = By.CSS_SELECTOR, 'button#next'
    cancel_locator = By.CSS_SELECTOR, 'button#close'


@ui.register_ui(
    checkbox_server=ui.CheckBox(By.XPATH, './/input[@type="checkbox"]'))
class RowServer(ui.Row):
    """Row of playbook."""


class ListServers(ui.List):
    """List of playbooks."""

    row_cls = RowServer
    row_xpath = './/div[contains(@class, "grid-line")]'


@ui.register_ui(
    checkbox_servers=ListServers(By.CSS_SELECTOR, 'div.col-xs-12.grid'))
class FormPlaybookServers(_ui.Form):
    """Form to choose servers for playbook."""

    submit_locator = By.CSS_SELECTOR, 'button#save'
    cancel_locator = By.CSS_SELECTOR, 'button#close'


@ui.register_ui(
    field_playbook_config=ui.TextField(By.NAME, 'configuration'))
class FormUpdateConfiguration(_ui.Form):
    """Form to update configuration."""

    submit_locator = By.CSS_SELECTOR, 'button#save'
    cancel_locator = By.CSS_SELECTOR, 'button#close'


@ui.register_ui(
    button_create_configuration=ui.Button(
        By.CSS_SELECTOR, "div.main-button > button.btn-primary"),
    form_create_configuration=FormCreateConfiguration(By.CSS_SELECTOR,
                                                      "div.modal-content"),
    form_playbook_configuration=FormPlaybookConfiguration(By.CSS_SELECTOR,
                                                          "div.modal-content"),
    form_playbook_parameters=FormPlaybookParameters(By.CSS_SELECTOR,
                                                    "div.modal-content"),
    form_playbook_servers=FormPlaybookServers(By.CSS_SELECTOR,
                                              "div.modal-content"),
    form_update_configuration=FormUpdateConfiguration(By.CSS_SELECTOR,
                                                      "div.modal-content"),
    list_configurations=ListConfigurations(By.CSS_SELECTOR, "div.col-xs-12"))
class PageConfigurations(base.PageBase):
    """Page to management configurations."""

    url = "/configurations"

    page_header_value = "Configurations"
