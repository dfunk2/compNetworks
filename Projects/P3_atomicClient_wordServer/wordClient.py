#read data from a packet: first determine if packet is complete, extract, and print

import sys
import socket

# How many bytes is the word length?
WORD_LEN_SIZE = 2

def usage():
    print("usage: wordclient.py server port", file=sys.stderr)

packet_buffer = b''

def get_next_word_packet(s):
    """
    Return the next word packet from the stream.

    The word packet consists of the encoded word length followed by the
    UTF-8-encoded word.

    Returns None if there are no more words, i.e. the server has hung
    up.
    """

    #goal is to start at the beginning of a packet every iteration
    global packet_buffer
    packet_buffer += s.recv(4096)

    #empty packet
    if packet_buffer == b'':
        return 
    
    #No header
    if len(packet_buffer) < WORD_LEN_SIZE:
        print("not enough data to know length of word")
        return 
    
    #parse packet
    wordLen = int.from_bytes(packet_buffer[:WORD_LEN_SIZE], "big")

    while len(packet_buffer) >= WORD_LEN_SIZE + wordLen:
        
        print( packet_buffer[:WORD_LEN_SIZE + wordLen])

        full_packet = packet_buffer[:WORD_LEN_SIZE + wordLen]

        #slice off the packet we just read
        packet_buffer = packet_buffer[WORD_LEN_SIZE + wordLen:]

        return full_packet

    

def extract_word(word_packet):
    """
    Extract a word from a word packet.

    word_packet: a word packet consisting of the encoded word length
    followed by the UTF-8 word.

    Returns the word decoded as a string.
    """
    get_string = word_packet[WORD_LEN_SIZE:]
    byte_string = get_string.decode('utf-8')
    
    return byte_string


# Do not modify:

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        usage()
        return 1

    s = socket.socket()
    s.connect((host, port))

    print("Getting words:")

    while True:
        word_packet = get_next_word_packet(s)

        if word_packet is None:
            break

        word = extract_word(word_packet)

        print(f"    {word}")

    s.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))