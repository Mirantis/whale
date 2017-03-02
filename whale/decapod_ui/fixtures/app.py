"""
-----------------------------------------------------
Fixtures to run horizon, login, create demo user, etc
-----------------------------------------------------
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
from stepler.horizon.fixtures.auto_use import report_dir
from stepler.horizon.fixtures.auto_use import video_capture
from stepler.horizon.fixtures.auto_use import virtual_display

from whale.decapod_ui.app import Decapod
from whale.decapod_ui.steps import AuthSteps

from whale import config

__all__ = [
    'auth_steps',
    'decapod',
    'login',

    'video_capture',
    'virtual_display',
    'report_dir',
]


@pytest.yield_fixture
def decapod(video_capture):
    """Initial fixture to start."""
    app = Decapod(config.DECAPOD_WD_URL)
    yield app
    app.quit()


@pytest.fixture
def auth_steps(decapod):
    """Get auth steps to login or logout in decapod."""
    return AuthSteps(decapod)


@pytest.yield_fixture
def login(auth_steps):
    """Login to decapod.

    Majority of tests requires user login. Logs out after test.
    """
    auth_steps.login(config.DECAPOD_LOGIN, config.DECAPOD_PASSWORD)

    yield
    # reload page to be sure that modal form doesn't prevent to logout
    auth_steps.app.current_page.refresh()
    auth_steps.logout()
