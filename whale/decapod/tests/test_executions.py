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
def test_deploy_cluster_add_osd_monitor_telegraf(deploy_cluster,
                                                 server_steps,
                                                 playbook_config_steps,
                                                 execution_steps):
    """**Scenario:** Deploy Ceph cluster, add OSD and monitor hosts, Telegraf.

    **Setup:**

    #. Deploy cluster

    **Steps:**

    #. Get all servers
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

    **Teardown:**

    #. Delete cluster via "purge_cluster" playbook execution.
    """
    all_server_ids = server_steps.get_server_ids()

    osd_server_id, monitor_server_id = server_steps.get_server_ids(
        vacant_only=True)[:2]

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=deploy_cluster['id'],
        playbook_id=config.PLAYBOOK_ADD_OSD,
        server_ids=[osd_server_id])

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=deploy_cluster['id'],
        playbook_id=config.PLAYBOOK_ADD_MONITOR,
        server_ids=[monitor_server_id])

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=deploy_cluster['id'],
        playbook_id=config.PLAYBOOK_TELEGRAF_INTEGRATION,
        server_ids=all_server_ids)

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=deploy_cluster['id'],
        playbook_id=config.PLAYBOOK_TELEGRAF_REMOVAL,
        server_ids=all_server_ids)

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=deploy_cluster['id'],
        playbook_id=config.PLAYBOOK_REMOVE_MONITOR,
        server_ids=[monitor_server_id])

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=deploy_cluster['id'],
        playbook_id=config.PLAYBOOK_REMOVE_OSD,
        server_ids=[osd_server_id])

    execution_steps.create_execution(playbook_config['id'])


@pytest.mark.idempotent_id('d8f0b507-2185-4800-b431-f196be1c17b3')
@pytest.mark.parametrize('playbook_config_deploy',
                         [{config.OSD_COLLOCATED_JOURNALS: True,
                           config.CEPH_REST_API: True}], indirect=True)
def test_deploy_cluster_integrate_cinder_upgrade_ceph(deploy_cluster,
                                                      playbook_config_steps,
                                                      execution_steps):
    """**Scenario:** Deploy Ceph cluster with Cinder integration, upgrade Ceph.

    **Setup:**

    #. Deploy cluster with OSD collocated journals and Ceph RestAPI

    **Steps:**

    #. Create new configuration, using the cluster and "Cinder Integration"
       playbook with "Cinder with Ceph backend", "Glance with Ceph backend"
       and "Nova with Ceph backend"
    #. Execute created configuration
    #. Create new configuration, using the cluster and "Upgrade Ceph" playbook
       with force time sync on Ceph nodes
    #. Execute created configuration

    **Teardown:**

    #. Delete cluster via "purge_cluster" playbook execution.
    """
    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=deploy_cluster['id'],
        playbook_id=config.PLAYBOOK_CINDER_INTEGRATON,
        hints={config.CINDER_CEPH_BACKEND: True,
               config.GLANCE_CEPH_BACKEND: True,
               config.NOVA_CEPH_BACKEND: True})

    execution_steps.create_execution(playbook_config['id'])

    playbook_config = playbook_config_steps.create_playbook_config(
        cluster_id=deploy_cluster['id'],
        playbook_id=config.PLAYBOOK_UPGRADE_CEPH,
        hints={config.FORCE_TIME_SYNC: True})

    execution_steps.create_execution(playbook_config['id'])
