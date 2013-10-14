# Copyright 2013 Dean Gardiner <gardiner91@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
from unittest import TestCase
from logr import Logr
from qcond import QueryCondenser


class TestQueryCondenser(TestCase):
    def setUp(self):
        Logr.configure(logging.DEBUG)

        self.qc = QueryCondenser()

    def test_eureka_seven(self):
        self.assertSequenceEqual(self.qc.distinct([
            'Eureka Seven',
            'Eureka Seven Ao',
            'Eureka Seven: Astral Ocean',
            'Eureka Seven: Ao',
            'Eureka Seven Astral Ocean'
        ]), [
            'eureka seven'
        ])

    def test_apartment_23(self):
        self.assertSequenceEqual(self.qc.distinct([
            "Don't Trust the B---- in Apartment 23",
            "Apartment 23",
            "Apt 23",
            "Don't Trust the B in Apt 23",
            "Don't Trust the B- in Apt 23",
            "Don't Trust the Bitch in Apartment 23",
            "Don't Trust the Bitch in Apt 23",
            "Dont Trust the Bitch in Apartment 23"
        ]), [
            'dont trust the',
            'apt 23',
            'apartment 23'
        ])

    def test_samurai_bride(self):
        self.assertSequenceEqual(self.qc.distinct([
            "Hyakka Ryouran: Samurai Girls",
            "Samurai Bride",
            "Hyakka Ryouran: Samurai Bride"
        ]), [
            'hyakka ryouran samurai',
            'samurai bride'
        ])

    def test_the_last_airbender(self):
        self.assertSequenceEqual(self.qc.distinct([
            "Avatar: The Last Airbender",
            "Avatar: The Legend of Aang",
            "The Last Airbender"
        ]), [
            'avatar the',
            'the last airbender'
        ])

    def test_the_legend_of_korra(self):
        self.assertSequenceEqual(self.qc.distinct([
            "The Legend of Korra",
            "The Last Airbender The Legend of Korra",
            "Avatar: The Legend of Korra",
            "Legend of Korra",
            "La Leggenda Di Korra"
        ]), [
            'the korra',
            'la leggenda di korra',
            'legend of korra'
        ])
