from google.cloud import pubsub_v1
from google.cloud.pubsub_v1.publisher.futures import Future
from auth import credentials
from config import project_id, topic_name


publisher = pubsub_v1.PublisherClient(credentials=credentials)
publisher_topic_path = publisher.topic_path(project_id, topic_name)


def callback(future: Future) -> None:
    message_id = future.result()

    print(f"Published message with ID: {message_id}")


def get_message() -> str:
    message = input("Enter a message to publish: ")

    if not message:
        message = "Empty message"


def publish_message(message: str) -> None:
    message = message.encode("utf-8")
    future: Future = publisher.publish(publisher_topic_path, message)

    future.add_done_callback(callback)

    try:
        future.result()

    except TimeoutError:
        future.cancel()

    except KeyboardInterrupt:
        future.cancel()


if __name__ == "__main__":
    message: str = get_message()
    publish_message(message)
