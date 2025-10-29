
def addr_dec(addr):
    addr_bytes = addr.split('.')
    addr = [int(str) for str in addr_bytes] #   ["192", "168", "1", "2"]  

    result =  ((addr[0] << 24) | (addr[1] << 16) |          # 192 00000000 00000000 000000000  | 168 00000000 00000000 | # 1 00000000  | 2
               (addr[2] << 8) | addr[3])                    # 192 168 1 2
    print(result)

def dec_addr(dec):
    result = []
    result.append((dec >> 24) & 0xff)
    result.append((dec >> 16) & 0xff)
    result.append((dec >> 8) & 0xff)
    result.append((dec >> 0) & 0xff)
    addr = '.'.join(list(map(str, result)))
    print(addr)




addr_dec('192.168.1.2')
addr_dec('10.20.30.40')
addr_dec('127.0.0.1') 


dec_addr(3325256824)
dec_addr(3405803976)
dec_addr(3221225987)
