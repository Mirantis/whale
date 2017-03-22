"""
---------------
Execution tests
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

import pytest

from whale import config


@pytest.mark.idempotent_id('a6173c5c-7208-4d92-9701-3aae79794671')
def test_deploy_cluster_add_osd_monitor_telegraf(cluster_steps,
                                                 server_steps,
                                                 playbook_config_steps,
                                                 execution_steps):
    """**Scenario:** Deploy Ceph cluster, add OSD and monitor hosts, Telegraf.

    **Steps:**

    #. Get available servers
    #. Create cluster
    #. Create new configuration, using the cluster and
       "Deploy Ceph cluster" playbook and 3 servers
    #. Execute created configuration
    #. Create new configuration, using the cluster and
       "Add OSD to Ceph cluster" playbook and 1 vacant server
    #. Execute created configuration
    #. Create new configuration, using the cluster and
       "Add monitor to the cluster" playbook and 1 vacant server
    #. Execute created configuration
    #. Create new configuration, using the cluster and
       "Telegraf Integration Plugin for Decapod" playbook and all used servers
    #. Execute created configuration
    #. Create new configuration, using the cluster and
       "Telegraf removal plugin for Decapod" playbook and all used servers
    #. Execute created configuration
    #. Create new configuration, using the cluster and
       "Remove monitor host from Ceph cluster" playbook and monitor server
    #. Execute created configuration
    #. Create new configuration, using the cluster and
       "Remove OSD host from Ceph cluster" playbook and OSD server
    #. Execute created configuration
    #. Create new configuration, using the cluster and
       "Purge cluster" playbook
    #. Execute created configuration
    #. Check the cluster is absent
    """
    all_server_ids = server_steps.get_server_ids()
    cluster_server_ids = all_server_ids[0:3]
    osd_server_id = all_server_ids[3]
    monitor_server_id = all_server_ids[4]

    cluster = cluster_steps.create_cluster()

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_DEPLOY_CLUSTER,
        server_ids=cluster_server_ids)

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_ADD_OSD,
        server_ids=[osd_server_id])

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_ADD_MONITOR,
        server_ids=[monitor_server_id])

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_TELEGRAF_INTEGRATION,
        server_ids=all_server_ids)

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_TELEGRAF_REMOVAL,
        server_ids=all_server_ids)

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_REMOVE_MONITOR,
        server_ids=[monitor_server_id])

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_REMOVE_OSD,
        server_ids=[osd_server_id])

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=cluster['id'],
        playbook_id=config.PLAYBOOK_PURGE_CLUSTER,
        server_ids=[])

    execution_steps.create_execution(playbook_config['id'])

    cluster_steps.check_cluster_presence(cluster['id'], must_present=False)
