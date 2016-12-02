"""
---------------
Decapod fixtures
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

from decapodlib import client as decapodclient
import pytest

from whale import config


__all__ = [
    'decapod_client',
    'get_decapod_client',
]


@pytest.fixture(scope='session')
def get_decapod_client():
    """Callable session fixture to get decapod client.

    Returns:
        function: function to get decapod client
    """
    def _get_decapod_client():
        return decapodclient.V1Client(url=config.DECAPOD_URL,
                                      login=config.DECAPOD_LOGIN,
                                      password=config.DECAPOD_PASSWORD)
    return _get_decapod_client


@pytest.fixture
def decapod_client(get_decapod_client):
    """Function fixture to get decapod client.

    Args:
        get_decapod_client (function): function to get decapod client

    Returns:
        decapodclient.V1Client: instantiated decapod client
    """
    return get_decapod_client()
