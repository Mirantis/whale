"""
-------------
Clusters page
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

from pom import ui
from selenium.webdriver.common.by import By

from whale.decapod_ui.app.pages import base
from whale.decapod_ui.app import ui as _ui


@ui.register_ui(
    label_name=ui.UI(By.CSS_SELECTOR, "div.name"),
    edit_icon=ui.UI(By.XPATH, './/span[@class="glyphicon edit-icon"]'))
class RowCluster(ui.Row):
    """Row of cluster."""


class ListClusters(ui.List):
    """List of clusters."""

    row_cls = RowCluster
    row_xpath = './/div[contains(@class, "box")]'


@ui.register_ui(
    field_name=ui.TextField(By.NAME, 'cluster_name'))
class FormCreateCluster(_ui.Form):
    """Form to create cluster."""


@ui.register_ui(
    button_create_cluster=ui.Button(
        By.CSS_SELECTOR, "div.main-button > button.btn-primary"),
    form_create_cluster=FormCreateCluster(
        By.CSS_SELECTOR, "div.modal-content"),
    list_clusters=ListClusters(By.CSS_SELECTOR, "div.clusters.row"))
class PageClusters(base.PageBase):
    """Page to management clusters."""

    url = "/clusters"
    page_header_value = "Cluster"
