# Get Started

In this quickstart, we will help you dip your toes in before you dive in. This guide will help you get started with the $KANDY$ Python SDK.

## Using the SDK

The library can be installed using PIP (python's package manager).

```bash
pip install cpaassdk
```

In your application, you simply need to import the library to be able to make use of it.

```python
// Instantiate the SDK.
from cpaassdk import Client

// Initialize
client = Client({
  'client_id': '<private project key>',
  'client_secret': '<private project secret>'
  'base_url': '$KANDYFQDN$'
})
```

After you've created your client instance, you can begin playing around with it to learn its functionality and see how it fits in your application. The API reference documentation will help to explain the details of the available features.

## Configuration

Create a client instance by passing the configuration object to the modules client object as shown below.

```python
from cpasssdk import Client

// Initialize
client = Client({
  'client_id': '<private project key>',
  'client_secret': '<private project secret>',
  'base_url': '$KANDYFQDN$'
})
```

The information required to be authenticated should be under:

+ `Projects` -> `{your project}` -> `Project info`/`Project secret`

> + `Private Project key` should be mapped to `client_id`
> + `Private Project secret` should be mapped to `client_secret`

## Usage

All modules can be accessed via the client instance. All method invocations follow the namespaced signature

`{client}.{module_name}.{method_name}(params)`

Example:

```python
response = client.twofactor.send_code({
  'destination_address': '+17147233172',
  'message': 'Your code is {code}'
})
```

<!-- need to add usage response and error response after testing. -->

## Default Error Response

### Format
```python
{
  'name': '<exception type>',
  'exception_id': '<exception id/code>',
  'message': '<exception message>'
}
```

### Example
```python
{
  'name': 'serviceException',
  'exception_id': 'SVC0002',
  'message': 'Invalid input value for message part address'
}
```