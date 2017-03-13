"""
---------------
Server fixtures
---------------
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

from whale.decapod import steps

__all__ = [
    'get_server_steps',
    'server_steps',
]


@pytest.fixture(scope="session")
def get_server_steps(get_decapod_client):
    """Callable session fixture to get servers steps.

    Args:
        get_decapod_client (function): function to get decapod client.

    Returns:
        function: function to get servers steps.
    """
    def _get_steps():
        return steps.ServerSteps(get_decapod_client())

    return _get_steps


@pytest.fixture
def server_steps(get_server_steps):
    """Function fixture to get server steps.

    Args:
        get_server_steps (function): function to get server steps

    Returns:
        ServerSteps: instantiated server steps
    """
    return get_server_steps()
