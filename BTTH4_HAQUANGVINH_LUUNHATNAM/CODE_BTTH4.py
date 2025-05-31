import pyshark

# Đường dẫn đến file pcapng
pcap_file = 'test.pcapng'  # thay bằng đường dẫn file của bạn
packet_limit = 10  # Giới hạn số packet để tránh chạy lâu

# Mở file và đọc gói tin
capture = pyshark.FileCapture(pcap_file, keep_packets=False)

print(f"\n Đang phân tích tối đa {packet_limit} gói tin...\n")

for i, packet in enumerate(capture):
    if i >= packet_limit:
        break

    print(f" GÓI TIN #{i+1}")

    # Tầng 2 - Data Link Layer (Ethernet)
    
    print("Tầng 2: ")
    if 'eth' in packet:
        eth = packet.eth
        print(f"   Ethernet:")
        print(f"     • MAC nguồn     : {eth.src}")
        print(f"     • MAC đích      : {eth.dst}")
        print(f"     • Loại Ethernet : {eth.type}")

    # Tầng 3 - Network Layer (IPv4 hoặc IPv6)
    print("Tầng 3: ")
    if 'ip' in packet:
        ip = packet.ip
        print(f"   IPv4:")
        print(f"     • IP nguồn       : {ip.src}")
        print(f"     • IP đích        : {ip.dst}")
        print(f"     • TTL            : {ip.ttl}")
        print(f"     • Protocol       : {ip.proto}")

    elif 'ipv6' in packet:
        ipv6 = packet.ipv6
        print(f"   IPv6:")
        print(f"     • IP nguồn       : {ipv6.src}")
        print(f"     • IP đích        : {ipv6.dst}")
        print(f"     • Next Header    : {ipv6.nxt}")

    print("-" * 50)

# Đóng capture sau khi hoàn tất
capture.close()
