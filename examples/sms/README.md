# SMS Starter Example

This is a simple sms application where a user can send an sms, subscribe sms notification and receive real-time sms events (inbound, outbound etc notification).

## Installation
1. Update the constants.py file with the appropriate credentials. Refer configuration section.
2. To install dependencies, run:
```bash
pipenv install
```
3. To start the server, run:
```bash
python sms.py
```

## Configuration
There are a few configuration variables (check `constants.py` file) to make the application simpler and help us focus on the key aspects a two-factor authentication system via SMS. Some of the variables are pre-filled and some are left blank which are left on the user to place appropriate values. All the variables are mandatory.

ENV KEY       | Description
------------- | -------------
CLIENT_ID     | Private project key
CLIENT_SECRET | Private project secret
BASE_URL      | URL of the CPaaS server to use
SENDER_NUMBER  | Phone number purchased in CPaaS portal (sender phone number)

## Usage
The application has a single simple page with 3 section:

### Section 1 - Send SMS
---
There are two fields in the form

1. Phone number - The phone number where the SMS is to be sent.
2. Message - A text message for the SMS

When clicked on `Send` button, an SMS is sent out where the `sender` phone number is the one add in `constants.py` file (SENDER_NUMBER) and `destination` is the one entered in the form.

### Section 2 - SMS notification subscription
---
This represents the subscription to SMS notification and can be found on the top right section. Here a Webhook host URL is to be added.

As incoming notifications are to be received by the local server, there is a requirement of a web server to be running and that web server to have a public IP address. So to use this it is recommended to install and use [ngrok](https://ngrok.com/).

#### How to use ngrok
Once `ngrok` is installed, run the following command
```bash
ngrok http 5000
```
5000 is the default `PORT` where the flask app runs. so you need to run the ngrok command mentioning the exact port.
Once `ngrok` starts forwarding the `localhost`, you would find a similar kind of message in your screen.

```bash
ngrok by @inconshreveable                                                                  (Ctrl+C to quit)

Session Status                online
Session Expires               7 hours, 58 minutes
Update                        update available (version 2.3.34, Ctrl-U to update)
Version                       2.3.28
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://29de1e3e.ngrok.io -> http://localhost:3001
Forwarding                    https://29de1e3e.ngrok.io -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```
After this the usage part of `ngrok` is done and we got out public domain, let's shift out attention to the notification subscription.

Copy the `forwarding` domain, for our case it is `https://29de1e3e.ngrok.io` from above and paste it to in the `Webhook host URL` input field in out `SMS starter app`.
Click `Subscribe` and a notification channel would be created with the above domain against the phone number that is described in the `.env` file (PHONE_NUMBER) and all the sms notifications would start coming in.

> Note: While entering the ngrok domain and subscribing, make sure that there is not forward slash at the end of the domain.

> **Correct** `https://29de1e3e.ngrok.io`

> **Incorrect** `https://29de1e3e.ngrok.io/`

### Section 3 - SMS Notification
This is the bottom half of the right section of the application. As in `section 2` we subscribed for all the SMS notification against the phone number described in the `constants.py` file (SENDER_NUMBER), whenever we send out an sms using the `Send SMS` section or get an sms to the phone number described in the `constants.py` file (SENDER_NUMBER), we would receive a notification and that notification would be printed out under the `SMS Notification` header

