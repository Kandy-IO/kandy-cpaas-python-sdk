# Get Started

In this quickstart, we will help you dip your toes in before you dive in. This guide will help you get started with the $KANDY$ Python SDK.

## Using the SDK

The library can be installed using PIP (python's package manager).

```bash
pip install cpaassdk
```

In your application, you simply need to import the library to be able to make use of it.

```python
# Instantiate the SDK.
from cpaassdk import Client

# Initialize
client = Client(config)
```

After you've created your client instance, you can begin playing around with it to learn its functionality and see how it fits in your application. The API reference documentation will help to explain the details of the available features.

## Configuration
Before starting, you need to learn following information from your CPaaS account, specifically from Developer Portal.

If you want to authenticate using CPaaS account's credentials, the configuration information required should be under:

+ `Home` -> `Personal Profile` (top right corner) -> `Details`
> + `Email` should be mapped to `email`
> + Your account password should be mapped to `password`
> + `Account client ID` should be mapped to `client_id`

Alternatively if you want to use your project's credentials, the configuration information required should be under:

+ `Projects` -> `{your project}` -> `Project info`/`Project secret`
> + `Private Project key` should be mapped to `client_id`
> + `Private Project secret` should be mapped to `client_secret`

Create a client instance by passing the configuration object to the modules client object as shown below.

```python
from cpasssdk import Client

# Initialize
client = Client({
  'client_id': '<private project key>',
  'client_secret': '<private project secret>',
  'base_url': 'https://$KANDYFQDN$'
})

# or

client = Client({
  'client_id': '<account client ID>',
  'email': '<account email>',
  'password': '<account password>',
  'base_url': 'https://$KANDYFQDN$'
})
```

## Usage

All modules can be accessed via the client instance, refer to [References](/developer/references/python) for details about all modules and it's methods. All method invocations follow the namespaced signature

`{client}.{module_name}.{method_name}(params)`

Example:

```python
client.conversation.create_message(params)
```

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