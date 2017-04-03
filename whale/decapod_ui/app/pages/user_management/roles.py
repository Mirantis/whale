"""
----------
Roles page
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
    button_edit=ui.Button(By.XPATH,
                          './/span[@class="glyphicon glyphicon-pencil"]'),
    button_delete=ui.Button(By.XPATH,
                            './/span[@class="glyphicon glyphicon-trash"]'))
class RolesRow(ui.Row):
    """Row with existing roles."""


class RolesHeader(_ui.Header):
    """Roles header"""

    cell_cls = RolesRow
    cell_xpath = './/div[@class="col-xs-2 name"]'


@ui.register_ui(
    header=RolesHeader(By.CSS_SELECTOR, 'div.grid-header'))
class RolesTable(ui.Table):
    """Table with roles"""


@ui.register_ui(
    field_role_name=ui.TextField(By.ID, 'role_name'))
class FormCreateRole(_ui.FormNext):
    """Form to create role."""


@ui.register_ui(
    checkbox_permissions_group=ui.CheckBox(By.XPATH,
                                           './/input[@type="checkbox"]'))
class RowPermissionsGroup(ui.Row):
    """Row of permissions group."""


class ListPermissionsGroups(ui.List):
    """List of permissions groups."""

    row_cls = RowPermissionsGroup
    row_xpath = './/div[@class="checkbox"]'


@ui.register_ui(
    checkbox_permissions_groups=ListPermissionsGroups(
        By.CSS_SELECTOR, 'div.permissions.long-content.grid'))
class FormRolePermissions(_ui.FormNext):
    """Form to change role permissions."""


@ui.register_ui(
    button_create_role=ui.Button(By.CSS_SELECTOR, "button.btn.btn-primary"),
    form_create_role=FormCreateRole(By.CSS_SELECTOR, "div.modal-content"),
    form_role_permissions=FormRolePermissions(By.CSS_SELECTOR,
                                              "div.modal-content"),
    table_roles=RolesTable(By.CSS_SELECTOR, "div.roles.grid.row"))
class PageRoles(base.PageBase):
    """Page to management roles."""

    url = "/admin/roles"
    page_header_value = "Role"
