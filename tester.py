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
from time import sleep
from logr import Logr
import sys
from qcond import QueryCondenser

TESTS = [
    [
        'Eureka Seven',
        'Eureka Seven Ao',
        'Eureka Seven: Astral Ocean',
        'Eureka Seven: Ao',
        'Eureka Seven Astral Ocean'
    ],
    [
        "Don't Trust the B---- in Apartment 23",
        "Apartment 23",
        "Apt 23",
        "Don't Trust the B in Apt 23",
        "Don't Trust the B- in Apt 23",
        "Don't Trust the Bitch in Apartment 23",
        "Don't Trust the Bitch in Apt 23",
        "Dont Trust the Bitch in Apartment 23"
    ],
    [
        "Hyakka Ryouran: Samurai Girls",
        "Samurai Bride",
        "Hyakka Ryouran: Samurai Bride"
    ],
    [
        "Avatar: The Last Airbender",
        "Avatar: The Legend of Aang",
        "The Last Airbender"
    ],
    [
        "The Legend of Korra",
        "The Last Airbender The Legend of Korra",
        "Avatar: The Legend of Korra",
        "Legend of Korra",
        "La Leggenda Di Korra"
    ]
]


def get_input(prompt, default=None):
    default_prompt = ' [%s]: ' % default if default else ''

    inp = raw_input(prompt + default_prompt)
    if inp == '':
        return default

    return inp


def try_int(value):
    try:
        return int(value)
    except:
        return None


def get_int(prompt, default=None, valid_func=None):
    result = None

    while not result or (valid_func and not valid_func(result)):
        result = try_int(get_input(prompt, default))

    return result

def get_param(n):
    if n >= len(sys.argv):
        return None

    return sys.argv[n]

if __name__ == '__main__':
    Logr.configure(logging.DEBUG)

    n = try_int(get_param(1)) or \
        get_int('Test number', 1, lambda x: 0 < x <= len(TESTS))

    qc = QueryCondenser()

    while n <= len(TESTS):
        result = qc.distinct(TESTS[n - 1])

        sleep(1)

        print '-' * 141
        for title in result:
            print title
        print '-' * 141

        if n < len(TESTS):
            raw_input('Press ENTER to continue')
        n += 1
