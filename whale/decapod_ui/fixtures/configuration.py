"""
----------------------
Configuration fixtures
----------------------
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

import pytest

from whale.decapod_ui.steps import configuration


__all__ = [
    'ui_configuration_steps',
]


@pytest.fixture
def ui_configuration_steps(decapod, login):
    """Function fixture to get configuration steps.

    Args:
        decapod (Decapod): instantiated decapod web application
        login (None): should log in decapod before steps using

    Returns:
        ConfigurationSteps: instantiated configuration steps
    """
    return configuration.ConfigurationSteps(decapod)
