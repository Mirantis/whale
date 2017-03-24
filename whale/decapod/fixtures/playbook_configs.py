"""
-------------------------------
Playbook configuration fixtures
-------------------------------
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

from whale import config
from whale.decapod import steps

__all__ = [
    'get_playbook_config_steps',
    'playbook_config_steps',
    'playbook_config_deploy',
    'cleanup_playbook_configs',
]


@pytest.fixture(scope="session")
def get_playbook_config_steps(get_decapod_client):
    """Callable session fixture to get playbook configuration steps.

    Args:
        get_decapod_client (function): function to get decapod client

    Returns:
        function: function to get playbook configuration steps
    """
    def _get_steps():
        return steps.PlaybookConfigSteps(get_decapod_client())

    return _get_steps


@pytest.fixture
def playbook_config_steps(get_playbook_config_steps, cleanup_playbook_configs):
    """Function fixture to get playbook configuration steps.

    Args:
        get_playbook_config_steps (function): get playbook config steps
        cleanup_playbook_configs (function): function to cleanup
            playbook configs after test

    Yields:
        PlaybookConfigSteps: instantiated playbook config steps
    """
    _playbook_config_steps = get_playbook_config_steps()
    configs = _playbook_config_steps.get_playbook_configs(check=False)
    configs_ids_before = {conf['id'] for conf in configs}

    yield _playbook_config_steps

    cleanup_playbook_configs(_playbook_config_steps,
                             uncleanable_ids=configs_ids_before)


@pytest.fixture
def playbook_config_deploy(request,
                           cluster,
                           server_steps,
                           playbook_config_steps):
    """Function fixture to create playbook config before test.

    Args:
        request (obj): pytest SubRequest instance
        cluster (dict): model of cluster
        server_steps (fixture): fixture to get servers ids
        playbook_config_steps (obj): instantiated playbook config steps

    Returns:
        dict: model of new playbook configuration
    """
    options = {}
    include_hint_ids = getattr(request, 'param', [])
    if include_hint_ids:
        options['include_hint_ids'] = include_hint_ids

    playbook_id = config.PLAYBOOK_DEPLOY_CLUSTER
    server_ids = server_steps.get_server_ids()[0:config.DEPLOY_SERVERS_COUNT]
    return playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=playbook_id,
        server_ids=server_ids,
        **options)


@pytest.fixture(scope='session')
def cleanup_playbook_configs():
    """"Callable session fixture to cleanup playbook configs.

    Returns:
        function: function to cleanup playbook configs
    """
    def _cleanup_playbook_configs(_playbook_config_steps,
                                  uncleanable_ids=None):
        uncleanable_ids = uncleanable_ids or []
        for config in _playbook_config_steps.get_playbook_configs(check=False):
            if config['id'] not in uncleanable_ids:
                _playbook_config_steps.delete_playbook_config(config['id'])

    return _cleanup_playbook_configs
