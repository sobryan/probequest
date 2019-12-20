"""
Packet sniffer module.
"""

from scapy.scapypipes import SniffSource


class PacketSniffer(SniffSource):
    """
    Wrapper around the 'SniffSource' Scapy pipe module.
    """

    def __init__(self, config):
        self.config = config

        frame_filter = self.config.generate_frame_filter()

        if self.config.debug:
            print("[!] Frame filter: {frame_filter}".format(
                frame_filter=frame_filter))

        SniffSource.__init__(
            self,
            iface=self.config.interface,
            filter=frame_filter
        )
