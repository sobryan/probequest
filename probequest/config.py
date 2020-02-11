#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ProbeQuest configuration.
"""

from enum import Enum
from re import compile as rcompile, IGNORECASE


class Mode(Enum):
    """
    Enumeration of the different operational modes
    supported by this software.
    """

    RAW = "raw"
    PNL = "pnl"

    def __str__(self):
        return self.value


class Config:
    """
    Configuration object.
    """

    interface = None

    essid_filters = None
    essid_regex = None
    ignore_case = False

    mac_exclusions = None
    mac_filters = None

    output_file = None

    mode = Mode.RAW
    fake = False
    debug = False

    def generate_frame_filter(self):
        """
        Generates and returns the frame filter according to the different
        options set of the current 'Config' object.
        """

        frame_filter = "type mgt subtype probe-req"

        if self.mac_exclusions is not None:
            frame_filter += " and not ("

            for i, station in enumerate(self.mac_exclusions):
                if i == 0:
                    frame_filter += "ether src host {s_mac}".format(
                        s_mac=station)
                else:
                    frame_filter += "|| ether src host {s_mac}".format(
                        s_mac=station)

            frame_filter += ")"

        if self.mac_filters is not None:
            frame_filter += " and ("

            for i, station in enumerate(self.mac_filters):
                if i == 0:
                    frame_filter += "ether src host {s_mac}".format(
                        s_mac=station)
                else:
                    frame_filter += "|| ether src host {s_mac}".format(
                        s_mac=station)

            frame_filter += ")"

        return frame_filter

    def complile_essid_regex(self):
        """
        Returns the compiled version of the ESSID regex.
        """

        if self.essid_regex is not None:
            if self.ignore_case:
                return rcompile(
                    self.essid_regex,
                    IGNORECASE
                )

            return rcompile(self.essid_regex)

        return None
