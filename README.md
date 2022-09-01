# NuvlaEdge On-Stop

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/nuvlaedge/on-stop/graphs/commit-activity)
[![GitHub issues](https://img.shields.io/github/issues/nuvlaedge/on-stop?style=for-the-badge&logo=github&logoColor=white)](https://GitHub.com/nuvlaedge/on-stop/issues/)
[![Docker pulls](https://img.shields.io/docker/pulls/nuvlaedge/on-stop?style=for-the-badge&logo=Docker&logoColor=white)](https://cloud.docker.com/u/nuvlaedge/repository/docker/nuvlaedge/on-stop)
[![Docker image size](https://img.shields.io/docker/image-size/nuvladev/on-stop/main?logo=docker&logoColor=white&style=for-the-badge)](https://cloud.docker.com/u/nuvlaedge/repository/docker/nuvlaedge/on-stop)


![CI Build](https://github.com/nuvlaedge/on-stop/actions/workflows/main.yml/badge.svg)
![CI Release](https://github.com/nuvlaedge/on-stop/actions/workflows/release.yml/badge.svg)


**This repository contains the source code for the NuvlaEdge On-Stop - the microservice which is responsible for the [NuvlaEdge](https://sixsq.com/nuvlaedge) total cleanup after stopping or deleting the NBE**

This microservice is an integral component of the NuvlaEdge Engine.


---

## Build the NuvlaEdge On-Stop

This repository is already linked with GitHub Actions, so with every commit, a new Docker image is released.

**If you're developing and testing locally in your own machine**, simply run `docker build .` or even deploy the microservice via the local [compose files](docker-compose.yml) to have your changes built into a new Docker image, and saved into your local filesystem.

**If you're developing in a non-master branch**, please push your changes to the respective branch, and wait for the CI to finish the automated build. You'll find your Docker image in the [nuvladev](https://hub.docker.com/u/nuvladev) organization in Docker hub, names as _nuvladev/on-stop:\<branch\>_.

## Deploy the NuvlaEdge On-Stop

### Prerequisites

 - *Docker (version 18 or higher)*
 - *Docker Compose (version 1.23.2 or higher)*

### Launching the NuvlaEdge Agent

Simply run `docker-compose up --build`

## Contributing

This is an open-source project, so all community contributions are more than welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md)

## Copyright

Copyright &copy; 2021, SixSq SA
