import argparse
import logging
import os

from googleapiclient import discovery

log = logging.getLogger(__name__)


parser = argparse.ArgumentParser(description="Control a google cloud instance.")
parser.add_argument('--debug', '-d', dest='debug', action='store_true', help="Debug mode")
parser.add_argument('--project', '-p', dest='project', help="instance project id")
parser.add_argument('--zone', '-z', dest='zone', help="instance zone")
parser.add_argument('--instance', '-i', dest='instance', help="instance name")


def restart_instance(project, zone, instance):
    compute = discovery.build('compute', 'v1')
    compute.instances().stop(project=project, zone=zone, instance=instance).execute()
    stopped = False
    while not stopped:
        list = compute.instances().list(project=project, zone=zone, instance=instance).execute()['items']
        instance = next((x for x in list if x['name'] == instance), None)
        if instance['status'] == "TERMINATED":
            stopped = True
    return compute.instances().start(project=project, zone=zone, instance=instance).execute()


if __name__ == "__main__":
    args = parser.parse_args()

    level = logging.INFO
    if args.debug:
        level = logging.DEBUG
    logging.basicConfig(format='%(asctime)s %(message)s', level=level)

    restart_instance(args.project or os.environ['gc_project'], args.zone or os.environ['gc_zone'], args.instance or os.environ['gc_instance'])
