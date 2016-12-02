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

# Decapod

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
