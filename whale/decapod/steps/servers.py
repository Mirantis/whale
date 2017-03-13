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

from decapodlib import exceptions
from hamcrest import (assert_that, equal_to, is_not, empty,
                      has_entries)  # noqa H301
from stepler.third_party import steps_checker
from stepler.third_party import waiter

from whale import base

__all__ = [
    'ServerSteps'
]


class ServerSteps(base.BaseSteps):
    """Server steps."""

    @steps_checker.step
    def create_server(self, server_id, host, username, check=True, **kwargs):
        """Step to create new server.

            Args:
                server_id (str): server id
                host (str): hostname of the server
                username (str): name of the user for Ansible on this server
                check (bool): flag whether to check step or not
                **kwargs: any other attribute provided will be passed to server

            Returns:
                json: model of new server

            Raises:
                TimeoutExpired|AssertionError: if check was
                triggered to an error
        """
        server = self._client.create_server(server_id=server_id,
                                            host=host,
                                            username=username,
                                            **kwargs)
        if check:
            self.check_server_presence(server_id)
            server = self.get_server(server_id)
            assert_that(server_id, equal_to(server['id']))
            assert_that(host, equal_to(server['data']['name']))
            assert_that(username, equal_to(server['data']['username']))
        return server

    @steps_checker.step
    def delete_server(self, server, check=True, **kwargs):
        """Step to delete server.

        Args:
            decapod_server_id (str): decapod server id
            check (bool): flag whether to check step or not
            **kwargs: any other attribute provided will be passed to server

        Raises:
            TimeoutExpired: if check failed
        """
        server_id = self.get_id(server)
        self._client.delete_server(server_id, **kwargs)
        if check:
            self.check_server_presence(server_id, must_present=False)

    @steps_checker.step
    def check_server_presence(self,
                              server_id,
                              must_present=True,
                              timeout=60):
        """Step to check server presence.

        Args:
            server_id (str): decapod server id
            must_present (bool): flag whether server should present or not
            timeout (int): seconds to wait a result of check

        Raises:
            TimeoutExpired: if check failed after timeout
        """

        def _check_server_presence():
            try:
                server = self._client.get_server(server_id)
                if server['time_deleted'] == 0:
                    is_present = True
                else:
                    is_present = False
            except exceptions.DecapodAPIError:
                is_present = False

            return waiter.expect_that(is_present, equal_to(must_present))

        waiter.wait(_check_server_presence, timeout_seconds=timeout)

    @steps_checker.step
    def get_servers(self, check=True):
        """Step to get servers.

        Args:
            check (bool, optional): flag whether to check step or not

        Returns:
            servers (list): list of servers

        Raises:
            AssertionError: if check failed
        """
        servers = self._client.get_servers()['items']
        if check:
            assert_that(servers, is_not(empty()))
        return servers

    @steps_checker.step
    def update_server(self, server, new_data, check=True):
        """Step to update server.

        Args:
            server (dict|str): server or its ID
            new_data (dict): new data for server
            check (bool, optional): flag whether to check step or not

        Returns:
            server(dict): dict of updated server

        Raises:
            AssertionError: if check failed
        """
        server_id = self.get_id(server)
        server = self.get_server(server_id)
        server['data'].update(new_data)
        self._client.put_server(server)
        if check:
            server = self.get_server(server)
            assert_that(server['data'], has_entries(new_data))
        return server

    @steps_checker.step
    def get_server(self, server, check=True):
        """Step to get server.

        Args:
            server (dict|str): server or its ID
            check (bool, optional): flag whether to check step or not

        Returns:
            server (dict): dict of server

        Raises:
            AssertionError: if check failed
        """
        server_id = self.get_id(server)
        server = self._client.get_server(server_id)
        if check:
            assert_that(server_id, equal_to(server['id']))
        return server
