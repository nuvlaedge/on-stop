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
    logging.info('Starting NuvlaBox deep cleanup')

    info = docker_client.info()

    swarm_info = info.get('Swarm', {})

    node_id = swarm_info.get('NodeID')

    local_node_state = swarm_info.get('LocalNodeState', 'inactive')

    is_swarm_enabled = True if node_id and local_node_state != "inactive" else False

    remote_managers = [rm.get('NodeID') for rm in swarm_info.get('RemoteManagers', [])]
    i_am_manager = True if node_id in remote_managers else False

    if i_am_manager:
        cluster_nodes = docker_client.nodes.list()

        # remove label
        label = 'nuvlabox'
        node = docker_client.nodes.get(node_id)
        node_spec = node.attrs['Spec']
        node_labels = node_spec.get('Labels', {})
        node_labels.pop(label)
        node_spec['Labels'] = node_labels
        logging.info(f'Removing node label {label} from this node ({node_id})')
        node.update(node_spec)

        # if len(cluster_nodes) > 1:




    # if manager:
    # check if node has nuvlabox label and remove that label


    # if in cluster mode, manager, and last node, also get rid of the ack and DG services/networks (also the traefik service) + nbmosquitto service as well

