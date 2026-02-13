#!/usr/bin/env python3

from alchemy.elements import create_fire, create_earth


def lead_to_gold():
    return ("Lead transmuted to gold using", create_fire())


def stone_to_gem():
    return ("Stone transmuted to gem using", create_earth())
