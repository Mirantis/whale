"""
------
Config
------
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

import os

# If DECAPOD_URL is undefined, corresponding fixture raises exception.
# DECAPOD_URL absence doesn't raise exception here, because for docs generation
# and unittests launching this variable doesn't need.

# By default test environment includes 5 servers min. And 3 servers are enough
# to deploy CEPH cluster. Other servers may be used for additional services.
DEPLOY_SERVERS_COUNT = int(os.environ.get('DEPLOY_SERVERS_COUNT', 3))

# Credentials
DECAPOD_URL = os.environ.get('DECAPOD_URL')
DECAPOD_WD_URL = 'http://{}'.format(DECAPOD_URL)
DECAPOD_LOGIN = os.environ.get('DECAPOD_LOGIN', 'login')
DECAPOD_PASSWORD = os.environ.get('DECAPOD_PASSWORD', 'password')

# Playbooks
PLAYBOOK_DEPLOY_CLUSTER = 'cluster_deploy'
PLAYBOOK_PURGE_CLUSTER = 'purge_cluster'
PLAYBOOK_ADD_OSD = 'add_osd'
PLAYBOOK_REMOVE_OSD = 'remove_osd'
PLAYBOOK_ADD_MONITOR = 'add_mon'
PLAYBOOK_REMOVE_MONITOR = 'remove_mon'
PLAYBOOK_TELEGRAF_INTEGRATION = 'telegraf_integration'
PLAYBOOK_TELEGRAF_REMOVAL = 'purge_telegraf'
PLAYBOOK_CINDER_INTEGRATON = 'cinder_integration'
PLAYBOOK_UPGRADE_CEPH = 'upgrade_ceph'
PLAYBOOK_VERSION = 1

# Hint IDs
CINDER_CEPH_BACKEND = 'cinder'
GLANCE_CEPH_BACKEND = 'glance'
NOVA_CEPH_BACKEND = 'nova'
OSD_COLLOCATED_JOURNALS = 'collocation'
OSD_DMCRYPT = 'dmcrypt'
MONITORS_COUNT = 'mon_count'
CEPH_REST_API = 'rest_api'
FORCE_TIME_SYNC = 'sync_time'

# Executions
EXECUTION_COMPLETED_STATUS = 'completed'
EXECUTION_FAILED_STATUS = 'failed'
EXECUTION_COMPLETED_TIMEOUT = 15 * 60

# UI
BROWSER_WINDOW_SIZE = map(
    int, os.environ.get('BROWSER_WINDOW_SIZE', '1920,1080').split(','))
VIRTUAL_DISPLAY = os.environ.get('VIRTUAL_DISPLAY')
UI_TIMEOUT = 30
ACTION_TIMEOUT = 60
EVENT_TIMEOUT = 180
PAGE_FORWARDING_TIMEOUT = 60
PERMISSIONS_GROUP_API = 'api'
PERMISSIONS_GROUP_PLAYBOOK = 'playbook'
PERMISSION_CREATE_CLUSTER = 'create_cluster'
PERMISSION_CLUSTER_DEPLOY = 'cluster_deploy'
