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

from pom.ui import base
from selenium.common import exceptions

# If DECAPOD_URL is undefined, corresponding fixture raises exception.
# DECAPOD_URL absence doesn't raise exception here, because for docs generation
# and unittests launching this variable doesn't need.

# Decapod credentials
DECAPOD_URL = os.environ.get('DECAPOD_URL')
DECAPOD_WD_URL = 'http://{}'.format(DECAPOD_URL)
DECAPOD_LOGIN = os.environ.get('DECAPOD_LOGIN', 'login')
DECAPOD_PASSWORD = os.environ.get('DECAPOD_PASSWORD', 'password')

# Decapod UI
BROWSER_WINDOW_SIZE = map(
    int, (os.environ.get('BROWSER_WINDOW_SIZE', ('1920,1080'))).split(','))

UI_TIMEOUT = 30
ACTION_TIMEOUT = 60
EVENT_TIMEOUT = 180

VIRTUAL_DISPLAY = os.environ.get('VIRTUAL_DISPLAY')

# TODO(agromov): If firefox can't get access to non-existing element,
# it raises exception:
# `WebDriverException: Message: can't access dead object`.
# Workaround: add WebDriverException to pom PRESENCE_ERRORS.
base.PRESENCE_ERRORS += (exceptions.WebDriverException, )

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

# execution
EXECUTION_CREATED_STATUS = 'created'
EXECUTION_STARTED_STATUS = 'started'
EXECUTION_COMPLETED_STATUS = 'completed'

EXECUTION_COMPLETED_TIMEOUT = 10 * 60

PAGE_FORWARDING_TIMEOUT = 60

PLAYBOOK_VERSION = 1
