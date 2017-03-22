"""
---------------
Execution steps
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

from hamcrest import assert_that, empty, equal_to, is_not, none  # noqa H301
from stepler.third_party import steps_checker
from stepler.third_party import waiter

from whale import base
from whale import config

__all__ = [
    'ExecutionSteps'
]


class ExecutionSteps(base.BaseSteps):
    """Execution steps."""

    @steps_checker.step
    def create_execution(self,
                         playbook_config_id,
                         playbook_config_version=config.PLAYBOOK_VERSION,
                         check=True,
                         **kwargs):
        """Step to create new playbook configuration model.

        Args:
            playbook_config_id (str): id of playbook config to use
            playbook_config_version (str): version of playbook config to use
            check (bool): flag whether to check step or not
             **kwargs: any suitable keyword arguments

        Returns:
            dict: model of new execution

        Raises:
            TimeoutExpired|AssertionError: if check failed
        """
        execution = self._client.create_execution(
            playbook_config_id, playbook_config_version, **kwargs)

        if check:
            self.check_resource_presence(execution['id'],
                                         self._client.get_execution)
            self.check_execution_status(execution['id'])

        return execution

    @steps_checker.step
    def get_executions(self, check=True, **kwargs):
        """Step to retrieve executions.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            list: list of executions

        Raises:
            AssertionError: if check failed
        """
        executions = self._client.get_executions(**kwargs)['items']

        if check:
            assert_that(executions, is_not(empty()))

        return executions

    @steps_checker.step
    def get_execution(self, execution_id, check=True, **kwargs):
        """Step to retrieve execution.

        Args:
            execution_id (str): execution id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: model of the execution

        Raises:
            AssertionError: if check failed
        """
        execution = self._client.get_execution(execution_id, **kwargs)

        if check:
            assert_that(execution['id'], equal_to(execution_id))

        return execution

    @steps_checker.step
    def get_last_execution_by_config_id(self,
                                        playbook_config_id,
                                        check=True,
                                        **kwargs):
        """Step to retrieve new execution by playbook config id.

        Args:
            playbook_config_id (str): playbook config id
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: model of the execution

        Raises:
            AssertionError: if check failed
        """
        for execution in self.get_executions(**kwargs):
            if (execution['data']['playbook_configuration']['id'] ==
                    playbook_config_id):
                break
        else:
            execution = None

        if check:
            assert_that(execution, is_not(none()))

        return execution

    @steps_checker.step
    def check_execution_status(self, execution_id,
                               status=config.EXECUTION_COMPLETED_STATUS,
                               failure_status=config.EXECUTION_FAILED_STATUS,
                               timeout=config.EXECUTION_COMPLETED_TIMEOUT):
        """Step to check execution status.

        Args:
            execution_id (str): execution id
            status (str): expected status to check
            failure_status (str): status to fail check
            timeout (int): seconds to wait a result of check

        Raises:
            TimeoutExpired|AssertionError: if check failed
        """
        def _check_execution_status():
            execution = self.get_execution(execution_id)
            actual_status = execution['data']['state'].lower()
            assert_that(actual_status, is_not(failure_status))
            return waiter.expect_that(actual_status, equal_to(status))

        waiter.wait(_check_execution_status, timeout_seconds=timeout)
