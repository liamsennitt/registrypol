# RegistryPol

[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/LiamSennitt/registrypol/Build/main)](https://github.com/LiamSennitt/registrypol/actions?query=workflow%3Abuild+branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/registrypol)](https://pypi.org/project/registrypol/)
[![GitHub](https://img.shields.io/github/license/LiamSennitt/registrypol)](LICENSE)

The `registrypol` module allows you to easily parse and create Windows Registry Policy files in Python.

## Installation

To install the `registrypol` module via pip, run the command:

```console
$ pip install registrypol
```

## Usage

Start by importing the `registrypol` module.

```python
>>> import registrypol
```

The function `registrypol.load`, loads an registry policy file.

```python
>>> with open('registry.pol', 'rb') as file:
...     registrypol.load(file)
```

In addition to loading an existing registry policy, policies created using the relevant Values can be dumped to a file using the `registrypol.dump` function.

```python
>>> with open('registry.pol', 'wb') as file:
...     registrypol.dump(policy, file)
```

### RegistryValue

To create a registry value as part of an registry policy, a `registrypol.values.RegistryValue` must be created.

```python
>>> from registrypol.values import RegistryValue

>>> value = RegistryValue(
...     key='Software\Policies\Microsoft\Windows\Control Panel\Desktop',
...     value='ScreenSaverIsSecure',
...     type='REG_SZ',
...     size=4,
...     data=b'\x01\x00\x00\x00'
... )
```

### RegistryPolicy

To create an registry policy one or more registry values must be created as described above.

These values can then be used to create an `registrypol.policy.RegistryPolicy`.

```python
>>> from registrypol.policy import RegistryPolicy

>>> policy = RegistryPolicy(
...     values=[
...         value
...     ]
... )
```
