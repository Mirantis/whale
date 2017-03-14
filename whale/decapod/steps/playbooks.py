"""
--------------
Playbook steps
--------------
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

from whale import base

__all__ = [
    'PlaybookSteps'
]


class PlaybookSteps(base.BaseSteps):
    """Playbook steps."""

    def get_playbooks(self, check=True, **kwargs):
        """Step to get all available playbooks.

        Args:
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            list: list of all playbooks

        Raises:
            AssertionError: if check failed
        """
        playbooks = self._client.get_playbooks(**kwargs)['items']
        if check:
            assert_that(playbooks, is_not(empty()))
        return playbooks

    def get_playbook(self, playbook_id, check=True, **kwargs):
        """Step to get a playbook by its id.

        Args:
            playbook_id (str): id of playbook
            check (bool): flag whether to check step or not
            **kwargs: any suitable keyword arguments

        Returns:
            dict: playbook model

        Raises:
            AssertionError: if check failed
        """
        playbooks = self.get_playbooks(**kwargs)

        for playbook in playbooks:
            if playbook['id'] == playbook_id:
                break
        else:
            playbook = None

        if check:
            assert_that(playbook, is_not(none()))

        return playbook
