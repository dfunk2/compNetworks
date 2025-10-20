import socket
import time
#Goal of program is to connect to NIST and get number of seconds since 1/1/1900;
#then print out system time from the clock on my computer
def nist_seconds_since_1900():
    client = socket.socket()
    server = ('time.nist.gov', 37)
    client.connect(server)

    #receive data and close socket
    data = client.recv(4)
    client.close()

    #decode the data
    byte_int = int.from_bytes(data, 'big')

    return byte_int

def system_seconds_since_1900():
    # The time server returns the number of seconds since 1900, but Unix
    # systems return the number of seconds since 1970. This function
    # computes the number of seconds since 1900 on the system.

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta
    return seconds_since_1900_epoch

print("NIST time:    ", nist_seconds_since_1900())
print("System time:  ", system_seconds_since_1900())