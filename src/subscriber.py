from google.cloud import pubsub_v1
from google.cloud.pubsub_v1.subscriber.futures import Future
from google.cloud.pubsub_v1.subscriber.message import Message
from auth import credentials
from config import project_id, subscription_name


subscription_name = f"projects/{project_id}/subscriptions/{subscription_name}"


def callback(message: Message) -> None:
    print("Received message: {}".format(message.data))

    message.ack()


def listen_for_messages() -> None:
    print("Listening for messages on: {}".format(subscription_name))

    subscriber: pubsub_v1.SubscriberClient = pubsub_v1.SubscriberClient(
        credentials=credentials
    )

    with subscriber:
        future: Future = subscriber.subscribe(subscription_name, callback)

        try:
            future.result()

        except TimeoutError:
            future.cancel()
            future.result()

        except KeyboardInterrupt:
            future.cancel()


if __name__ == "__main__":
    listen_for_messages()
