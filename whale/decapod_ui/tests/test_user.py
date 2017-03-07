"""
-------------
User UI tests
-------------
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


@pytest.mark.idempotent_id('3476fac7-3415-4d99-92fd-41725a183044')
def test_create_user(role, user_steps, ui_user_steps):
    """**Scenario:** User may be created in UI.

    **Steps:**

    #. Create user via UI
    #. Find user by name via API

    **Teardown:**

    #. Delete user via API
    """
    user_login = ui_user_steps.create_user(role['data']['name'])
    user_steps.get_user_id(user_login)
