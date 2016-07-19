import logging
import argparse
from kafka import KafkaConsumer
from hvbenchapi.conf import logconf
import json

ARGS = {'kafka': "127.0.0.1"}

log = logging.getLogger(__name__)

def main():

    parser = argparse.ArgumentParser(description="Netdata plugin.")

    parser.add_argument('frequency', help="netdata update frequency.")
    parser.add_argument('-v', '--verbose', help="Enable debug log.", dest='verbose', action='store_true')
    parser.add_argument('-k', '--kafka', help="Address of the kafka host.", default=ARGS['kafka'])

    cmdargs = parser.parse_args()

    if cmdargs.verbose:
        logging.basicConfig(level=logging.DEBUG, **logconf)
    else:
        logging.basicConfig(level=logging.INFO, **logconf)

    consumer = KafkaConsumer('hvbench', 'hvmonitor',
                             bootstrap_servers="%s:9092" % cmdargs.kafka)

    for msg in consumer:

        jmsg = json.loads(str(msg.value, 'ASCII'))

        print(jmsg)
        print(str(msg.topic))

    log.info("Quitting..")

if __name__ == "__main__":
    main()
