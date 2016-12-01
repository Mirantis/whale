"""
----------------------------------------
Predefined UI components for page or tab
----------------------------------------
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

from whale import config


class Spinner(ui.UI):
    """Spinner to wait loading."""

    timeout = config.ACTION_TIMEOUT


class Modal(ui.Block):
    """Spinner to wait loading."""

    timeout = config.ACTION_TIMEOUT


@ui.register_ui(
    modal=Modal(By.CLASS_NAME, 'modal-backdrop'),
    spinner=Spinner(By.CLASS_NAME, 'spinner'))
class InitiatedUI(ui.Container):
    """Predefined UI components for page or tab."""
