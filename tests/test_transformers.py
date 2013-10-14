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
from qcond import MergeTransformer, SliceTransformer
from qcond.helpers import itemsMatch
from qcond.transformers.base import Transformer
from qcond.transformers.merge import DNode, print_tree


class TestTransformer(TestCase):
    def test_run(self):
        transformer = Transformer()
        self.assertRaises(NotImplementedError, transformer.run, [])


class TestMergeTransformer(TestCase):
    def setUp(self):
        Logr.configure(logging.DEBUG)
        self.merge = MergeTransformer()

    def test_apartment_23(self):
        self.assertSequenceEqual(self.merge.run([
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
            'dont trust the apartment 23',
            'dont trust the apt 23',
            'apt 23',
            'apartment 23'
        ])

    def test_legend_of_korra(self):
        self.assertSequenceEqual(self.merge.run([
            "The Legend of Korra",
            "The Last Airbender The Legend of Korra",
            "Avatar: The Legend of Korra",
            "Legend of Korra",
            "La Leggenda Di Korra"
        ]), [
            'the',
            'the korra',
            'avatar the legend of korra',
            'la leggenda di korra',
            'legend of korra'
        ])

    def test_merge_is_order_independent(self):
        root_one = [
            self._create_chain(['avatar', 'the', 'legend', 'of', 'korra']),
            self._create_chain(['la', 'leggenda', 'di', 'korra']),
            self._create_chain(['the', 'last', 'airbender', 'the', 'legend', 'of', 'korra'])
        ]

        self._create_chain(['legend', 'of', 'korra'], root_one[-1])

        root_one.append(self._create_chain(['legend', 'of', 'korra']))

        result_one = self.merge.merge(root_one)

        Logr.debug("-----------------------------------------------------------------")

        root_two = [
            self._create_chain(['the', 'legend', 'of', 'korra']),
        ]

        self._create_chain(['last', 'airbender', 'the', 'legend', 'of', 'korra'], root_two[-1])

        root_two += [
            self._create_chain(['legend', 'of', 'korra']),
            self._create_chain(['la', 'leggenda', 'di', 'korra']),
            self._create_chain(['avatar', 'the', 'legend', 'of', 'korra'])
        ]

        result_two = self.merge.merge(root_two)

        Logr.debug("=================================================================")

        assert itemsMatch(
            self._get_chain_values(result_one),
            self._get_chain_values(result_two)
        )

    def test_merge(self):
        pass

    def _get_chain_values(self, node_or_nodes):
        if type(node_or_nodes) is list:
            results = []
            for node in node_or_nodes:
                results += self._get_chain_values(node)
            return results

        node = node_or_nodes

        if node.right:
            return self._get_chain_values(node.right)

        score, value, original_value = node.full_value()

        return [value]

    def _create_chain(self, words, root=None):
        if not root:
            root = DNode(words[0], None)
            words = words[1:]

        last_node = root
        while len(words):
            word = words.pop(0)

            node = DNode(word, last_node)
            last_node.right.append(node)

            last_node = node

        return root




class TestSliceTransformer(TestCase):
    def setUp(self):
        self.slice = SliceTransformer()

    def test_apartment_23(self):
        self.assertSequenceEqual(self.slice.run([
            "Don't Trust the B---- in Apartment 23",
            "Apartment 23",
            "Apt 23",
            "Don't Trust the B in Apt 23",
            "Don't Trust the B- in Apt 23",
            "Don't Trust the Bitch in Apartment 23",
            "Don't Trust the Bitch in Apt 23",
            "Dont Trust the Bitch in Apartment 23"
        ]), [
            "Don't Trust the B in Apt 23",
            'Dont Trust the Bitch in Apartment 23',
            'Apartment 23',
            'Apt 23'
        ])

    def test_legend_of_korra(self):
        self.assertSequenceEqual(self.slice.run([
            "The Legend of Korra",
            "The Last Airbender The Legend of Korra",
            "Avatar: The Legend of Korra",
            "Legend of Korra",
            "La Leggenda Di Korra"
        ]), [
            'Legend of Korra',
            'La Leggenda Di Korra'
        ])
