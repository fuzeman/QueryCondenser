# QueryCondenser 
[![](https://travis-ci.org/fuzeman/QueryCondenser.png?branch=master)](https://travis-ci.org/fuzeman/Caper)
[![](https://coveralls.io/repos/fuzeman/QueryCondenser/badge.png?branch=master)](https://coveralls.io/r/fuzeman/Caper?branch=master)

Merge similar search queries to save network and service resources.

## Development

**Dependencies**

    Logr>=0.2.1

## Contributing

Pull requests, bug reports and enhancement requests are welcome.

Feel free to contact me if you have any questions.

## Contact

**IRC:** fuzeman on freenode  
**Email:** fuzeman91@gmail.com

## License

### Main license
*covers everything excluding the exceptions listed below*

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

### Exceptions

#### tests/compat.py

    #
    # 'safe_repr' and 'assertSequenceEqual' functions are
    # from the Python 2.7 unittest module
    #
    # ------ unittest license start ------
    #
    # Copyright (c) 1999-2003 Steve Purcell
    # Copyright (c) 2003-2010 Python Software Foundation
    # This module is free software, and you may redistribute it and/or modify
    # it under the same terms as Python itself, so long as this copyright message
    # and disclaimer are retained in their original form.
    #
    # IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
    # SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF
    # THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
    # DAMAGE.
    #
    # THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT
    # LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
    # PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS,
    # AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
    # SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
    #
    # ----- unittest license end -----