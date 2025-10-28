#This program simulates a receiving computer validating that the tcp packet is not corrupted.
import re

#splitAddr() reads all 10 txt files and splits their address content into source and destination IP addresses
def split_addr():
    addr = [[] for _ in range(10)]

    for i in range(10):
        with open(f"tcp_data/tcp_addrs_{i}.txt", "r") as file:
            content = file.read()
            #split content by source and destination
            splitContent = re.split(' ', content)
            splitContent = [new_line.strip() for new_line in splitContent]
            addr[i] = splitContent
    
    return addr

#addr_bytestring() converts source and destination IP addresses into bytestrings 
def addr_bytestring(addr):
    byte_str = [[] for _ in range(10)]
    for i, IP_addr in enumerate(addr):
        for source_dest in IP_addr:
            split_strs = source_dest.split('.')    #198.51.100.77 --> ['198', '51', '100', '77']
            as_int = tuple(map(int, split_strs))    #(198, 51, 100, 77)
            as_bytes = [k.to_bytes(1, 'big') for k in as_int]   
            addr_concat = (b''.join(as_bytes))
            byte_str[i].append(addr_concat)
    return byte_str

#function to generate IP pseudo header in bytes
def create_pseudo_header(byte_list):
    #source+dest+z+P+TCPLen
    pseudo_header = []

    for i, addr in enumerate(byte_list):
        source_bytes, dest_bytes = addr
        zero = b'\x00'
        protocol = b'\x06'
        with open(f"tcp_data/tcp_data_{i}.dat", "rb") as fp:
            tcp_data = fp.read()
            tcp_len = len(tcp_data)
            tcp_len_bytes = tcp_len.to_bytes(1, 'big')
        header = source_bytes + dest_bytes + zero + protocol + tcp_len_bytes
        pseudo_header.append(header)
    return pseudo_header


# function to build a new version of tcp data and 
    # function to concatenate the pseudo header 
# function to compute checksum from concatenation
# function to extract checksum and compare two checksums

addr = split_addr()
byte_str = addr_bytestring(addr)
headers = create_pseudo_header(byte_str)
#debugging!
for h in headers:
    print(h.hex())
