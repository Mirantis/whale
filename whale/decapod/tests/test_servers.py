"""
------------
Server tests
------------
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
from stepler.third_party import utils


@pytest.mark.idempotent_id('d7f68921-3b16-4c16-91ce-224ab8da03e0')
def test_delete_create_server(server_steps):
    """Check that server was deleted and created.

    **Steps:**

    #. Delete server
    #. Create server
    """
    server = server_steps.get_servers()[0]
    server_steps.delete_server(server['id'])
    server_steps.create_server(server_id=server['id'],
                               host=server['data']['ip'],
                               username=server['data']['username'])


@pytest.mark.idempotent_id('7474c3c8-e63c-4294-a27a-cc8c82200bd2')
def test_update_server(server_steps):
    """Check that server was updated.

    **Steps:**

    #. Update server
    """
    server = server_steps.get_servers()[0]
    origin_name = server['data']['name']
    new_name = next(utils.generate_ids())
    server_steps.update_server(server=server,
                               new_data={'name': new_name})
    server_steps.update_server(server=server,
                               new_data={'name': origin_name})


@pytest.mark.idempotent_id('884f5cda-febe-4043-943e-c8a5da94aa2c')
def test_get_server(server_steps):
    """Check that we got server.

    **Steps:**

    #. Get server
    """
    server = server_steps.get_servers()[0]
    server_steps.get_server(server)


@pytest.mark.idempotent_id('615471e0-7e04-44b0-802e-c7d4e6c4293a')
def test_list_servers(server_steps):
    """Check that we got list of servers.

    **Steps:**

    #. Get list of servers
    """
    server_steps.get_servers()
