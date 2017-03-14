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

from decapodlib import exceptions
from hamcrest import assert_that, empty, equal_to, is_not, none  # noqa H301
from stepler import base
from stepler.third_party import waiter


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

    @staticmethod
    def get_resource_by_field(field_value, getter, field_name='name',
                              check=True):
        """Step to retrieve resource by field.

        Args:
            field_value (str): field value that is used to identify resource
            getter (obj): method to get resources
            field_name (str): field name that is used to identify resource
            check (bool): flag whether to check step or not

        Returns:
            resource (dict): model of resource

        Raises:
            AssertionError: if check failed
        """
        for resource in getter():
            if resource['data'][field_name] == field_value:
                break
        else:
            resource = None

        if check:
            assert_that(resource, is_not(none()))

        return resource

    @staticmethod
    def check_resource_presence(resource_id, getter, must_present=True,
                                timeout=0):
        """Step to check that resource is present.

        Args:
            resource_id (str): resource id
            getter (obj): method to get resource
            must_present (bool): flag whether resource should be present or not
            timeout (int): seconds to wait a result of check

        Raises:
            TimeoutExpired: if check failed after timeout
                exception
        """
        def _check_resource_presence():
            try:
                resource = getter(resource_id)
            except exceptions.DecapodAPIError:
                is_present = False
            else:
                is_present = True if resource['time_deleted'] == 0 else False

            return waiter.expect_that(is_present, equal_to(must_present))

        waiter.wait(_check_resource_presence, timeout_seconds=timeout)
