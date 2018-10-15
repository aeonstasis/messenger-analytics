import enum
import json
import sys
from collections import Counter, namedtuple
from enum import Enum


@enum.unique
class ReactionType(Enum):
    """Types of Facebook Messenger reaction emojis.

    Arguments:
        Enum {string} -- escaped strings and corresponding reaction type
    """
    ANGRY = "\u00f0\u009f\u0098\u00a0"
    DISLIKE = "\u00f0\u009f\u0091\u008e"
    HAHA = "\u00f0\u009f\u0098\u0086"
    LIKE = "\u00f0\u009f\u0091\u008d"
    LOVE = "\u00f0\u009f\u0098\u008d"
    SAD = "\u00f0\u009f\u0098\u00a2"
    WOW = "\u00f0\u009f\u0098\u00ae"


@enum.unique
class MessageType(Enum):
    """Type of message.

    Arguments:
        Enum {int} -- enumerate type of message.
    """
    TEXT = enum.auto()
    STICKER = enum.auto()
    PHOTO = enum.auto()
    PLAN = enum.auto()


# Associates a reaction type with the name of the person that reacted
Reaction = namedtuple('Reaction', ['actor', 'reaction_type'])


class Message:
    def __init__(self, sender, timestamp_ms, content, reactions, message_type):
        self._sender = sender
        self._timestamp_ms = timestamp_ms
        self._content = content
        self._reactions = reactions
        self._message_type = message_type

    @property
    def sender(self):
        return self._sender

    @property
    def timestamp_ms(self):
        return self._timestamp_ms

    @property
    def content(self):
        return self._content

    @property
    def reactions(self):
        return self._reactions

    @property
    def message_type(self):
        return self._message_type

    @staticmethod
    def make_message(raw_message):
        # Handle corner case of deactivated / deleted account
        sender = raw_message.get("sender_name", "Facebook User")
        timestamp_ms = raw_message["timestamp_ms"]
        content = raw_message.get("content", "")
        reactions = []
        for reaction in raw_message.get("reactions", []):
            try:
                reactions.append(
                    Reaction(reaction["actor"], ReactionType(reaction["reaction"])))
            except ValueError:
                # Possible corner case if non-standard reacts are used
                continue

        # Parse message type
        if "plan" in raw_message:
            message_type = MessageType.PLAN
        elif "photos" in raw_message:
            message_type = MessageType.PHOTO
        elif "sticker" in raw_message:
            message_type = MessageType.STICKER
        else:
            message_type = MessageType.TEXT

        return Message(sender, timestamp_ms, content, reactions, message_type)


class MessageThread:
    """Wraps a `message.json` file generated from the Facebook Messenger
    data download, calculating aggregated statistics.
    """

    def __init__(self, path):
        """Constructs a MessageThread, calculating read-only attributes.

        Arguments:
            path {Path} -- path object pointing to a `message.json`
        """
        with open(path, 'r') as f:
            message_thread = json.load(f)
        self._participants = message_thread.get("participants", "Just You")
        self._messages = [Message.make_message(raw_message) for
                          raw_message in message_thread["messages"]]
        self._title = message_thread["title"]

    @property
    def participants(self):
        """Return list of participants in the conversation thread.

        Returns:
            list[string] -- list of participants
        """
        return self._participants

    @property
    def messages(self):
        """Return list of Message objects from the raw messages.

        Returns:
            list[Message] -- parsed messages
        """
        return self._messages

    @property
    def title(self):
        """Name of the thread.

        Name of the group chat if three or more participants,
        name of the other person otherwise.

        Returns:
            string -- name of the thread
        """
        return self._title

    def timestamp_range(self):
        """Assumes messages are chronologically ordered."""
        return [self._messages[-1].timestamp_ms, self._messages[0].timestamp_ms]

    def message_counts(self):
        """Returns map of unique sender to number of messages."""
        return Counter(message.sender for message in self._messages)
