# pyiptoasn

**pyiptoasn** is an APACHE licensed library written in Python providing an easy to use wrapper around https://iptoasn.com/.

## Installation:

From source use

		$ python setup.py install

or install from PyPi

		$ pip install pyiptoasn

## Documentation:

```python
>>> from pyiptoasn import IPLookup
>>> ip = IPLookup()
>>> ip.lookup('88.207.251.51')
{u'as_number': 6661, u'last_ip': u'88.207.255.255', u'as_description': u'EPT-LU Entreprise des P. et T. Luxembourg', u'first_ip': u'88.207.128.0', u'as_country_code': u'LU', u'announced': True}
```

## License:

```
Apache v2.0 License
Copyright 2017 Martin Simon

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
