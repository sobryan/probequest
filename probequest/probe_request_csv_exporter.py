"""
Probe request CSV exporter module.
"""

from csv import writer

from scapy.pipetool import Sink


class CSVExporter(Sink):
    """
    A probe request CSV exporting sink.
    """

    def __init__(self, config, name=None):
        Sink.__init__(self, name=name)

        self.csv_file = config.output_file
        self.csv_writer = None

    def start(self):
        if self.csv_file is not None:
            self.csv_writer = writer(self.csv_file, delimiter=";")

    def stop(self):
        if self.csv_file is not None:
            self.csv_file.close()

    def push(self, msg):
        self.csv_writer.writerow([
            msg.timestamp,
            msg.s_mac,
            msg.s_mac_oui,
            msg.essid
        ])
