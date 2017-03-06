"""
-------------
Servers steps
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

from hamcrest import (assert_that, empty, equal_to, has_entries,
                      is_not)  # noqa H301
from stepler.third_party import steps_checker

from whale import base

__all__ = [
    'ServerSteps'
]


class ServerSteps(base.BaseSteps):
    """Server steps."""

    @steps_checker.step
    def create_server(self, server_id, server_ip, username, check=True,
                      **kwargs):
        """Step to create new server.

        Args:
            server_id (str): server id
            server_ip (str): server ip
            username (str): name of the user for Ansible on this server
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            server (dict): model of new server

        Raises:
            TimeoutExpired|AssertionError: if check was triggered to an error
        """
        # self._client.create_server method returns empty dict ({}).
        server = self._client.create_server(server_id=server_id,
                                            host=server_ip,
                                            username=username,
                                            **kwargs)

        if check:
            self.check_resource_presence(server_id, self._client.get_server,
                                         timeout=60)
            server = self.get_server(server_id)
            assert_that(server['id'], equal_to(server_id))
            assert_that(server['data']['ip'], equal_to(server_ip))
            assert_that(server['data']['username'], equal_to(username))

        return server or self.get_server(server_id)

    @steps_checker.step
    def delete_server(self, server_id, check=True, **kwargs):
        """Step to delete server.

        Args:
            server_id (str): server id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Raises:
            TimeoutExpired: if check failed
        """
        self._client.delete_server(server_id, **kwargs)

        if check:
            self.check_resource_presence(server_id, self._client.get_server,
                                         must_present=False, timeout=60)

    @steps_checker.step
    def get_servers(self, check=True, **kwargs):
        """Step to get servers.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            servers (list): list of servers

        Raises:
            AssertionError: if check failed
        """
        servers = self._client.get_servers(**kwargs)['items']

        if check:
            assert_that(servers, is_not(empty()))

        return servers

    @steps_checker.step
    def update_server(self, server, new_data, check=True, **kwargs):
        """Step to update server.

        Args:
            server (dict|str): server or its ID
            new_data (dict): new data for server
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            server (dict): dict of updated server

        Raises:
            AssertionError: if check failed
        """
        if not isinstance(server, dict):
            server = self.get_server(server)

        server['data'].update(new_data)

        server = self._client.put_server(server, **kwargs)

        if check:
            assert_that(server['data'], has_entries(new_data))

        return server

    @steps_checker.step
    def get_server_ids(self, check=True):
        """Step to get ids of all servers.

        Args:
            check (bool, optional): flag whether to check step or not

        Returns:
            list: all server ids
        """
        server_ids = [s['id'] for s in self.get_servers(check=check)]
        if check:
            assert_that(server_ids, is_not(empty()))
        return server_ids

    @steps_checker.step
    def get_server(self, server_id, check=True, **kwargs):
        """Step to get server.

        Args:
            server_id (str): server id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            server (dict): dict of server

        Raises:
            AssertionError: if check failed
        """
        server = self._client.get_server(server_id, **kwargs)

        if check:
            assert_that(server['id'], equal_to(server_id))

        return server
