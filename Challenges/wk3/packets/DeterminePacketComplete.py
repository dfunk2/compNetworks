#(expected_complete, expected_result)
#expected_result = (boolean, multiple strings)
test_data = (
    (b'\x00\x05hello', (True, (b'\x00\x05hello', b''))),
    (b'\x00\x05hello\x00\x03', (True, (b'\x00\x05hello', b'\x00\x03'))),
    (b'\x00\x05hello\x00\x03and\x00\x09bb', (True, (b'\x00\x05hello', b'\x00\x03and\x00\x09bb'))),
    (b'\x00\x00', (True, (b'\x00\x00',b''))),
    (b'\x00\x05hell', (False, None)),
    (b'\x00\x05', (False, None)),
    (b'\x00', (False, None)),
    (b'', (False, None)),
)

def packet_complete(data):
    # IMPLEMENT ME
    messageLen = len(data[2:])
    print(messageLen)

    if len(data) < 2:
        return False
    if messageLen >= data[1]:
        return True
    else: 
        return False

#receives data and returns a complete packet including the message length and any remaining bytes after that packet
def packet_extract(data):
    headerLen = len(data[:2])
    unknown_messageLen = len(data[2:])
    
    if unknown_messageLen > data[1]:
        totalLen = headerLen + data[1]
    else:
        totalLen = headerLen + data[1]

    return (data[:totalLen], data[totalLen:])

for data, (expected_complete, expected_result) in test_data:
    
    print(f"{'='*40}\nData: {data}\n{'-'*40}")

    complete = packet_complete(data)

    print(f"Expected: {expected_complete}")
    print(f"     Got: {complete}")

    #boolean comparison, tells us that the string we got is completed or not
    assert(complete == expected_complete)

    #if we return true from packet_complete 
    if complete:
        result = packet_extract(data)
        print(f"Expected: {expected_result}")
        print(f"     Got: {result}")
        assert(result == expected_result)
