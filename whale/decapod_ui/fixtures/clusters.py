"""
----------------
Cluster fixtures
----------------
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

from whale.decapod_ui.steps import ClusterSteps

__all__ = ['ui_cluster_steps']


@pytest.fixture
def ui_cluster_steps(decapod, login):
    """Function fixture to get cluster steps.

    Args:
        decapod (Decapod): instatiated decapod application
        login (None): user should log in before cluster actions

    Returns:
        ClusterSteps: instantiated cluster steps
    """
    return ClusterSteps(decapod)
