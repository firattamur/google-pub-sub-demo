# Google Pub/Sub Demo

This repository contains a simple demo of Google Pub/Sub. Google Pub/Sub is a fully-managed real-time messaging service that allows you to send and receive messages between independent applications. It is a great tool for building distributed systems and microservices.

## Prerequisites

- Google Cloud SDK
- Python 3.9+

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/google-pubsub-demo.git
cd google-pubsub-demo
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up Google Cloud SDK:

Follow the instructions [here](https://cloud.google.com/sdk/docs/quickstarts) to install and initialize the Google Cloud SDK.

4. Set up Google Pub/Sub:

Follow the instructions [here](https://cloud.google.com/pubsub/docs/quickstart-console) to create a topic and subscription.

## Running the Demo

- Make sure you have created Google Service Account credentials and downloaded the JSON file. See [here](https://cloud.google.com/docs/authentication/production) for more information. 

- Make sure you add roles `Pub/Sub Publisher` and `Pub/Sub Subscriber` to your service account.

- Before running the demo, please edit variables in `config.py` to match your project, topic, and subscription.

```python
project_id = "your-project-id"
topic_id = "your-topic-id"
subscription_id = "your-subscription-id"
credentials_json_path = "your-credentials-file-path"
```

1. Start the subscriber:

```bash
python src/subscriber.py
```

2. Start the publisher and enter a message:

```bash
python src/publisher.py
```

```bash
Enter a message: Hello World!
```

3. Check the subscriber terminal to see the message.

```bash
Received message: Hello World!
```

You should see messages being published and received in the console.




