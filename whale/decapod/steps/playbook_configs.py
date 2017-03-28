"""
----------------------------
Playbook configuration steps
----------------------------
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


from hamcrest import assert_that, has_entries, empty, equal_to, is_not  # noqa
from stepler.third_party import steps_checker
from stepler.third_party import utils

from whale import base

__all__ = [
    'PlaybookConfigSteps'
]


class PlaybookConfigSteps(base.BaseSteps):
    """Playbook Configuration steps."""

    @steps_checker.step
    def create_playbook_config(self, cluster_id, playbook_id, server_ids=None,
                               name=None, hints=None, check=True, **kwargs):
        """Step to create new playbook configuration model.

        Args:
            cluster_id (str): id of cluster
            playbook_id (str): id of playbook to use
            server_ids (list|None): list of all servers ids
            name (str|None): the name of the playbook config
            hints (dict|None): dict of included or excluded hint IDs
            check (bool): flag whether to check step or not
             **kwargs: any suitable keyword arguments

        Returns:
            dict: model of new playbook

        Raises:
            TimeoutExpired|AssertionError: if check was triggered to an error
        """
        server_ids = server_ids or []
        name = name or next(utils.generate_ids())
        hints = [{'id': h, 'value': v} for h, v in (hints or {}).items()]

        playbook_config = self._client.create_playbook_configuration(
            name, cluster_id, playbook_id, server_ids, hints=hints, **kwargs)

        if check:
            self.check_resource_presence(
                playbook_config['id'], self._client.get_playbook_configuration)
            assert_that(playbook_config['data']['name'], equal_to(name))
            assert_that(playbook_config['data']['cluster_id'],
                        equal_to(cluster_id))
            assert_that(playbook_config['data']['playbook_id'],
                        equal_to(playbook_id))

        return playbook_config

    @steps_checker.step
    def update_playbook_config(self, playbook_config, new_data, check=True,
                               **kwargs):
        """Step to update playbook configuration model.

        Args:
            playbook_config (dict|str): playbook config or its id
            new_data (dict): new data for playbook config
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: model of new playbook configuration

        Raises:
            AssertionError: if check was triggered to an error
        """
        if not isinstance(playbook_config, dict):
            playbook_config = self.get_playbook_config(playbook_config)

        playbook_config['data'].update(new_data)

        self._client.update_playbook_configuration(playbook_config, **kwargs)

        if check:
            assert_that(playbook_config['data'], has_entries(new_data))

        return playbook_config

    @steps_checker.step
    def get_playbook_configs(self, check=True, **kwargs):
        """Step to get list of all playbook configurations.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            list: list of all playbook configurations

        Raises:
            AssertionError: if check was triggered to an error
        """
        playbook_configurations = self._client.get_playbook_configurations(
            **kwargs)['items']

        if check:
            assert_that(playbook_configurations, is_not(empty()))

        return playbook_configurations

    @steps_checker.step
    def get_playbook_config(self, playbook_config_id, check=True, **kwargs):
        """Step to get a playbook config by its id.

        Args:
            playbook_config_id (str): id of playbook config
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: playbook config model

        Raises:
            AssertionError: if check was triggered to an error
        """
        playbook_configuration = self._client.get_playbook_configuration(
            playbook_config_id, **kwargs)

        if check:
            assert_that(playbook_configuration['id'], equal_to(
                playbook_config_id))

        return playbook_configuration

    @steps_checker.step
    def delete_playbook_config(self, playbook_config_id, check=True, **kwargs):
        """Step to delete playbook configuration.

        Args:
            playbook_config_id (str): playbook config id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Raises:
            TimeoutExpired: if check was triggered to an error
        """
        playbook_config = self._client.delete_playbook_configuration(
            playbook_config_id, **kwargs)

        if check:
            self.check_resource_presence(
                playbook_config['id'], self._client.get_playbook_configuration,
                must_present=False)
