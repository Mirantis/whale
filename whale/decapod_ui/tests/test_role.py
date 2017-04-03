"""
-------------
Role UI tests
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


@pytest.mark.idempotent_id('458f3541-5b4f-42be-92d4-8cc6f8cc6aa6')
def test_create_role(role_steps, ui_role_steps):
    """**Scenario:** Role may be created in UI.

    **Steps:**

    #. Create role via UI
    #. Find role by name via API

    **Teardown:**

    #. Delete role using API
    """
    role_name = ui_role_steps.create_role()
    role_steps.get_role_by_name(role_name)
