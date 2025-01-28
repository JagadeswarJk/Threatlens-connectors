# -*- coding: utf-8 -*-
"""Threatlens AlienVault connector main module."""

from alienvault import AlienVault

if __name__ == "__main__":
    connector = AlienVault()
    connector.run()
