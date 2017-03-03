"""
----
Base
----
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

from stepler import base


class BaseSteps(base.BaseSteps):
    """Base steps-class for whale tests.

    This class contains common steps for whale tests.
    """

    @staticmethod
    def get_id(obj):
        """Step to retrieve id from object.

        Args:
            obj: dict with `id` key, object with `id` field or another
                object which is consider to be id

        Returns:
            str: retrieved id

        Raises:
            ValueError: if obj is dict and it doesn't contain `id` field
        """
        if isinstance(obj, dict):
            try:
                return obj['id']
            except KeyError:
                raise ValueError(
                    "{!r} should be ID of object or dict with key 'id' "
                    "and its value.".format(obj))
        elif hasattr(obj, 'id'):
            return obj.id

        return obj
