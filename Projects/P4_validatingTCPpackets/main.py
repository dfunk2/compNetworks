#write program that validates a tcp packet by ensuring it has not been corrupted in transit.
#This program simulates a receiving computer validating that the data being sent to it is not corrupted.
import re

#splitAddr reads all 10 txt files and splits their address content into source and destination IP addresses
def splitAddr():
    addr = [[] for _ in range(10)]

    for i in range(10):
        with open(f"tcp_addrs_{i}.txt", "r") as file:
            content = file.read()
            #split content by source and destination
            splitContent = re.split(' ', content)
            splitContent = [new_line.strip() for new_line in splitContent]
            addr[i] = splitContent
    
    return addr

#addr_bytestrings converts source and destination IP addresses into bytestrings 
def addr_bytestrings(addr):
    addr_bytes = [[] for _ in range(10)]
    for i, IP_addr in enumerate(addr):
        j = i
        for j, source_dest in enumerate(IP_addr):
            clean_addr = source_dest.replace(".", "")
            IPaddr_byte = clean_addr.encode('utf-8')
            addr_bytes[i].append(IPaddr_byte)
            #print("addr ", IPaddr, "addr in bytes ", IPaddr_byte)
    print(addr_bytes)

addr = splitAddr()
addr_bytestrings(addr)
# splitAddr()