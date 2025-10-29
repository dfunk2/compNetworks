#This program simulates a receiving computer validating that a tcp packet is not corrupted.
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

#function to generate IP pseudo header in bytes (pseudo-header: source+dest+z+P+TCPLen)
def create_pseudo_header(byte_str):
    pseudo_header = []
    for i, addr in enumerate(byte_str):
        source_bytes, dest_bytes = addr
        zero = b'\x00'
        protocol = b'\x06'
        with open(f"tcp_data/tcp_data_{i}.dat", "rb") as fp:
            tcp_data = fp.read()
            tcp_len = len(tcp_data)
            tcp_len_bytes = tcp_len.to_bytes(2, 'big')
        header = source_bytes + dest_bytes + zero + protocol + tcp_len_bytes
        pseudo_header.append(header)
    return pseudo_header


# function extracts checksum in TCP header and rebuilds tcp header/data with checksum set to zero
def modify_checksum():
    tcp_zero_cksums = []
    org_cksum_decs = []
    for i in range(10):
        with open(f'tcp_data/tcp_data_{i}.dat', 'rb') as fp:
            tcp_data = fp.read()
            org_cksum = tcp_data[16:18]
            org_cksum_dec= (int.from_bytes(org_cksum, "big"))
            tcp_zero_cksum = (tcp_data[:16] + b'\x00\x00' + tcp_data[18:])
            
            tcp_zero_cksums.append(tcp_zero_cksum)
            org_cksum_decs.append(org_cksum_dec)
    return org_cksum_decs, tcp_zero_cksums


# function to compute checksum from concatenation
#get the 16 bit value ones complement sum of the words in the header and payload. MUST BE EVEN
def compute_checksum(pseudo_header, tcp_zero_cksums):
    cksum_list = []
    for i in range(10):
        if len(tcp_zero_cksums) % 2 == 1:
           tcp_zero_cksums += b'\x00'

        data = pseudo_header[i] + tcp_zero_cksums[i]        # concat the IP pseudo header + tcp header and payload  
        offset = 0
        total = 0
        while offset < len(data):
            word = (int.from_bytes(data[offset:offset +2], "big"))
            total += word
            total = (total & 0xffff) + (total >> 16)    # carry arount
            offset += 2

        cksum = ((~total) & 0xffff)         # ones complement
        cksum_list.append(cksum)
    return cksum_list

# function to compare two checksums
def compare_cksums(cksum_list, org_cksum_dec):
    for i in range(10):
        if cksum_list[i] == org_cksum_dec[i]:
            print('PASS')
        else:
            print('FAIL')


#driver code
addr = split_addr()
byte_str = addr_bytestring(addr)
pseudo_header = create_pseudo_header(byte_str)
org_cksum_decs, tcp_zero_cksums = modify_checksum()

cksum_list = compute_checksum(pseudo_header, tcp_zero_cksums)
compare_cksums(cksum_list, org_cksum_decs)

#debugging!
# for h in headers:
#     print(h.hex())

# print(f"checksums:{ org_cksum_decs}")
# # , tcp header: {tcp_zero_cksum}"
# for i, cks in enumerate(cksum_list):
#     print(f"index {i}:", cks)