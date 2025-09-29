#encode UTF-8
s = "Hi 🙂"
bytes_s = s.encode("utf-8")
print_bytes = lambda s: print(' '.join(f'{b:02x}' for b in s))
print_bytes(bytes_s) #prints hex values

#encode ascii
#ascii_bytes = s.encode("ascii")
    #output is error d/t emoji

#encode utf-16
utf_16_bytes = s.encode("utf-16")
print_bytes = lambda s: print(' '.join(f'{b:02x}' for b in s))
print_bytes(utf_16_bytes)
    #utf-8 output is less annd different values than utf-16

#encode16to8 = utf_16_bytes.decode("utf-8")
#print_bytes = lambda s: print(' '.join(f'{b:02x}' for b in s))
#print_bytes(encode16to8)
    #prints error that utf-8 cant decode byte 0xff in position 0

#decode utf-16 back to string
decode16to16 = utf_16_bytes.decode("utf-16")
print(decode16to16)
     #verified it works !


