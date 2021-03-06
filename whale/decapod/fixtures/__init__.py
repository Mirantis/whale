"""
----------------
Decapod fixtures
----------------
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


from .clusters import *  # noqa
from .decapod import *  # noqa
from .executions import *  # noqa
from .playbooks import *  # noqa
from .playbook_configs import *  # noqa
from .roles import *  # noqa
from .users import *  # noqa
from .servers import *  # noqa

__all__ = sorted([  # sort for documentation
    'get_decapod_client',
    'decapod_client',

    'get_playbook_steps',
    'playbook_steps',

    'get_playbook_config_steps',
    'playbook_config_steps',
    'playbook_config_deploy',
    'cleanup_playbook_configs',

    'get_execution_steps',
    'execution_steps',

    'get_role_steps',
    'role_steps',
    'role',
    'cleanup_roles',

    'get_user_steps',
    'user_steps',
    'user',
    'cleanup_users',

    'get_cluster_steps',
    'cluster_steps',
    'delete_cluster',
    'cluster',
    'deploy_cluster',
    'cleanup_clusters',

    'get_server_steps',
    'server_steps',
])
