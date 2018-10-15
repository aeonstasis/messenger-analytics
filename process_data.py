#!/usr/bin/env python3
import os
from collections import Counter

import click
import msgpack  # TODO: add cache saving and loading

import util


@click.command()
@click.option('--data-path',
              required=True,
              type=click.Path(writable=False),
              help="Path to messages subfolder inside downloaded data folder")
@click.option('-n', default=50, type=int, help="Number of friends to output")
@click.option('--output-path',
              default='./data/cache.bin',
              type=click.Path(writable=True),
              help="Path to where to save object cache")
def main(data_path, n, output_path):
    message_threads = []

    # Walk the downloaded data directory and construct MessageThread objects
    for root, dirs, files in os.walk(data_path):
        if dirs or "message.json" not in files:
            continue
        message_threads.append(util.MessageThread(
            os.path.join(root, "message.json")))

    click.echo("Total number of Messenger conversations: {}".format(
        len(message_threads)))

    # Print descending-sorted list of highest-event conversations
    click.echo("Displaying top {}".format(n))
    counter = Counter()
    for message_thread in message_threads:
        counter += message_thread.message_counts()
    most_common = counter.most_common(n)
    max_name_len = max(len(item[0]) for item in most_common)
    max_count_len = len(str(most_common[0][1]))
    for item in most_common:
        name, count = item[0], str(item[1])
        print('{} {} messages'.format(name.ljust(
            max_name_len), count.ljust(max_count_len)))


if __name__ == '__main__':
    main()  # pylint: disable=E1120
