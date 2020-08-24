# This file is part of Octopus Sensing <https://octopus-sensing.nastaran-saffar.me/>
# Copyright © Nastaran Saffaryazdi 2020
#
# Octopus Sensing is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
#  either version 3 of the License, or (at your option) any later version.
#
# Octopus Sensing is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Foobar.
# If not, see <https://www.gnu.org/licenses/>.

import multiprocessing


class Device(multiprocessing.Process):
    '''All devices should inherit from Device class.'''

    def __init__(self, name=None, output_path="output"):
        super().__init__()
        self.device_name = name
        self.message_queue = None
        self.subject_id = None
        self.stimulus_id = None
        self.output_path = output_path
        self.name = name

    def run(self):
        self._run()

    def _run(self):
        '''The subclass shouldn't implement 'run', but '_run' instead.'''
        raise NotImplementedError()

    def set_queue(self, queue):
        '''
        Sets message queue for the device

        @param queue: a queue that will be used for message passing
        '''
        self.message_queue = queue
