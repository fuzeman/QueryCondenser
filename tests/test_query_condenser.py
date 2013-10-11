import logging
from unittest import TestCase
from logr import Logr
from qcond import QueryCondenser


class TestQueryCondenser(TestCase):
    def setUp(self):
        Logr.configure(logging.DEBUG)

        self.qc = QueryCondenser()

    def test_distinct(self):
        self.assertSequenceEqual(self.qc.distinct([
            'Eureka Seven',
            'Eureka Seven Ao',
            'Eureka Seven: Astral Ocean',
            'Eureka Seven: Ao',
            'Eureka Seven Astral Ocean'
        ]), [
            'eureka seven'
        ])

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

        self.assertSequenceEqual(self.qc.distinct([
            "Hyakka Ryouran: Samurai Girls",
            "Samurai Bride",
            "Hyakka Ryouran: Samurai Bride"
        ]), [
            'hyakka ryouran samurai',
            'samurai bride'
        ])

        self.assertSequenceEqual(self.qc.distinct([
            "Avatar: The Last Airbender",
            "Avatar: The Legend of Aang",
            "The Last Airbender"
        ]), [
            'avatar the',
            'the last airbender'
        ])

        self.assertSequenceEqual(self.qc.distinct([
            "The Legend of Korra",
            "The Last Airbender The Legend of Korra",
            "Avatar: The Legend of Korra",
            "Legend of Korra",
            "La Leggenda Di Korra"
        ]), [
            'the korra',
            'legend of korra',
            'la leggenda di korra'
        ])
