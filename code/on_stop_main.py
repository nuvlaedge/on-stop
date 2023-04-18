#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" NuvlaEdge On-Stop

To be executed on every stop or full shutdown of the NBE, in order to ensure a
proper cleanup of dangling resources.

"""

from on_stop.on_stop import main

if __name__ == '__main__':
    main()
