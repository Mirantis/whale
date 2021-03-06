"""
-------------------------------------------
Decapod UI steps for playbook configuration
-------------------------------------------
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

import json

from hamcrest import assert_that, has_entries  # noqa H301
from stepler.third_party import steps_checker
from stepler.third_party import utils
from stepler.third_party import waiter

from whale import config
from whale.decapod_ui.steps import base


class ConfigurationSteps(base.BaseSteps):
    """Playbook configuration steps."""

    def _page_configurations(self):
        """Open configurations page if it isn't opened."""
        self.app.page_base.header.link_configurations.click()
        return self.app.page_configurations

    @steps_checker.step
    def create_deploy_configuration(self,
                                    playbook_name,
                                    cluster_name,
                                    servers,
                                    name=None,
                                    check=True):
        """Step to create playbook configuration.

        Args:
            playbook_name (str): playbook name of configuration
            cluster_name (str): cluster name of configuration
            servers (list): list of servers of configuration
            name (str, optional): name of configuration
            check (bool, optional): flag whether to check step or not

        Returns:
            str: configuration name

        Raises:
            Exception: if configuration is not present on page
        """
        name = name or next(utils.generate_ids())

        page = self._page_configurations()

        page.button_create_configuration.click()

        page.form_create_configuration.field_name.value = name
        page.form_create_configuration.combobox_cluster.value = cluster_name
        page.form_create_configuration.next(modal_absent=False)

        page.form_playbook_configuration.radiobutton_playbooks.row(
            playbook_name).radiobutton.click()
        page.form_playbook_configuration.next(modal_absent=False)

        page.form_playbook_parameters.field_monitors_count.value = len(servers)
        page.form_playbook_parameters.next(modal_absent=False)

        for server in servers:
            page.form_playbook_servers.checkbox_servers.row(
                server['data']['name']).checkbox_server.click()
        page.form_playbook_servers.submit(modal_absent=False)

        if check:
            page.list_configurations.row(name).wait_for_presence()

        return name

    @steps_checker.step
    def update_configuration(self, config_name, new_config_data, check=True):
        """Step to update playbook configuration.

        Args:
            config_name (str): playbook config name
            new_config_data (dict): new data for the configuration
            check (bool, optional): flag whether to check step or not

        Raises:
            AssertionError: if check failed
        """
        page = self._page_configurations()

        page.list_configurations.row(config_name).maximize_icon.click()
        page.list_configurations.row(config_name).button_edit_config.click()

        with page.form_update_configuration as form:
            config_dict = json.loads(form.field_playbook_config.value)
            config_dict.update(new_config_data)
            form.field_playbook_config.value = json.dumps(config_dict)
            form.submit(modal_absent=False)

        if check:
            page.list_configurations.row(
                config_name).button_view_config.click()
            with page.form_update_configuration as form:
                config_dict = json.loads(form.field_playbook_config.value)
                assert_that(config_dict['global_vars']['cluster'],
                            assert_that(config_dict,
                                        has_entries(new_config_data)))
                form.cancel(modal_absent=False)

    @steps_checker.step
    def delete_configuration(self, config_name, check=True):
        """Step to delete playbook configuration.

        Args:
            config_name (str): playbook configuration name
            check (bool, optional): flag whether to check step or not

        Raises:
            Exception: if configuration is present on page
        """
        page = self._page_configurations()

        page.list_configurations.row(config_name).maximize_icon.click()
        page.list_configurations.row(config_name).button_delete_config.click()
        page.form_confirm_config_deletion.submit(modal_absent=False)

        if check:
            page.list_configurations.row(config_name).wait_for_absence()

    @steps_checker.step
    def create_execution(self, config_name, check=True):
        """Step to create execution.

        Args:
            config_name (str, optional): name of configuration
            check (bool, optional): flag whether to check step or not

        Returns:
            str: configuration name

        Raises:
            TimeoutExpired: if check failed after timeout
        """
        page = self._page_configurations()

        page.list_configurations.row(config_name).maximize_icon.click()
        page.list_configurations.row(config_name).button_execute_config.click()

        if check:
            waiter.wait(
                lambda: (self.app.current_page.page_header_value ==
                         self.app.page_executions.page_header_value),
                timeout_seconds=config.PAGE_FORWARDING_TIMEOUT)
