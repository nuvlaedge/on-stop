#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" NuvlaBox On-Stop

To be executed on every stop or full shutdown of the NBE, in order to ensure a proper cleanup of dangling resources

"""

import docker
import logging
import socket
import sys

logging.basicConfig(format='%(levelname)s - %(module)s - L%(lineno)s: %(message)s', level='INFO')

docker_client = docker.from_env()
if len(sys.argv) > 1 and "paused".startswith(sys.argv[1].lower()):
    logging.info('Pausing myself...')
    try:
        myself = docker_client.containers.get(socket.gethostname())
    except docker.errors.NotFound:
        logging.error(f'Cannot find this container by hostname: {socket.gethostname()}. Cannot proceed')
        raise

    myself.pause()
else:
    pass

