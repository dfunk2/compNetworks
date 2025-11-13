import sys
import json
import math  # If you want to use math.inf for infinity

def ipv4_to_value(ipv4_addr):
    addr = ipv4_addr.split('.')
    addr_as_int = [int(n) for n in addr]
    val_of_addr = (addr_as_int[0] << 24 | addr_as_int[1] << 16 | addr_as_int[2] << 8 | addr_as_int[3])
    return val_of_addr

def get_subnet_mask_value(slash): 
        for i, char in enumerate(slash):
            if char == '/':
                num = int(slash[i+1:])
                #create the mask
                ip_bits = 32
                left_over = ip_bits - num
                as_one_bits = (1 << num) - 1
                subnet_mask_int = as_one_bits << left_over
                return subnet_mask_int
            
def ips_same_subnet(ip1, ip2, slash):
    val_of_addr1 = ipv4_to_value(ip1)
    val_of_addr2 = ipv4_to_value(ip2)
    mask_of_ip = get_subnet_mask_value(slash)

    network_num1 = val_of_addr1 & mask_of_ip
    network_num2 = val_of_addr2 & mask_of_ip

    if network_num1 == network_num2:
        return True
    else:
        return False
    
def find_router_for_ip(routers, ip):
    for router_ip, router_specs in routers.items():
        slash = router_specs["netmask"]

        same_subnet = ips_same_subnet(router_ip, ip, slash)
        if same_subnet:
            return router_ip
    return None


def dijkstras_shortest_path(routers, src_ip, dest_ip):
    #initialize 
    to_visit = set(routers.keys())
    dist_dict = {router_ip: math.inf for router_ip in routers} 
    parent_dict = {parent_router: None for parent_router in routers}

    src_router = find_router_for_ip(routers, src_ip)
    dest_router = find_router_for_ip(routers, dest_ip)
    dist_dict[src_router] = 0

    while len(to_visit) != 0:
        #find the current node/ip with smallest distance
        current_node = min(to_visit, key=lambda node: dist_dict[node])
        #pop current node from queue
        to_visit.remove(current_node)
    
        #iterate through neighbors of current node
        for neighbor_ip, conn_data in routers[current_node]["connections"].items():
            
            #if source and dest ips are on the same subnet no need to route
            same_subnet = ips_same_subnet(src_ip, dest_ip, conn_data["netmask"])
            if same_subnet:
                return []
            
            #check if you found a shorter path and add
            path_weight = dist_dict[current_node] + conn_data["ad"]
            if path_weight < dist_dict[neighbor_ip]:
                dist_dict[neighbor_ip] = path_weight
                parent_dict[neighbor_ip] = current_node
    
    #shortest path from src to dest router ips
    path = []
    curr_parent = dest_router
    while curr_parent is not None:
        path.append(curr_parent)
        curr_parent = parent_dict[curr_parent]
    path.reverse()
    return path
            
            

            
#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
