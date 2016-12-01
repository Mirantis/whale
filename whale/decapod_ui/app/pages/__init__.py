"""
-------------
Decapod pages
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

from .base import PageBase
from .clusters import PageClusters
from .configurations import PageConfigurations
from .executions import PageExecutions
from .login import PageLogin
from .playbooks import PagePlaybooks
from .servers import PageServers


pages = [
    PageBase,
    PageClusters,
    PageConfigurations,
    PageExecutions,
    PageLogin,
    PagePlaybooks,
    PageServers,
]
