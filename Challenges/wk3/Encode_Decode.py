def encode_data(message, value):
    byte = []
    str_bytes = message.encode('utf-8')
    int_bytes = value.to_bytes(2, "big")

    for b in int_bytes:
        print(f"big endian values that make up {value}: ", b)
    total_bytes = str_bytes + int_bytes
    print("concatenate message and integer in bytes:", total_bytes)

    byte.append(len(total_bytes))
    byte.append(str_bytes)
    byte.append(int_bytes)
   
    return byte


def decode_data(bytes):
    print("bytes:", bytes)
    decode = ()
    str = bytes[1].decode('utf-8')
    decode += (str,)
    int_value = int.from_bytes(bytes[2], "big")
    decode += (int_value,)
    
    print("tuple", decode)

bytes = encode_data("Hi", 3490)
decode_data(bytes)