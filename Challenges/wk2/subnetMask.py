def subnetMask(IP_mask):
    network, host = ([], [])
    inverse_mask = ([])
    ip, mask = IP_mask
    #take inverse of mask
    for j in range(len(mask)): inverse_mask.append(~(mask[j]))

    #loop through length of list within tuple
    for i in range(len(ip)):
        #mask ip address to get network
        network.append(ip[i] & mask[i])
        #mask ip address from inverse of mask to get host
        host.append(ip[i] & inverse_mask[i])
    print('network: ', network, 'host: ', host)


subnetMask(([192, 168, 17, 2], [255, 0, 0, 0]))
subnetMask(([192, 168, 17, 2], [255, 255, 0, 0]))
subnetMask(([192, 168, 17, 2], [255, 255, 255, 0]))
subnetMask(([192, 168, 17, 2], [255, 192, 0, 0]))
subnetMask(([192, 168, 17, 2], [255, 255, 248, 0]))