# SIMONE LA PORTA


def ip_and_subnet_info(cidr_input):
    """
    Simple function to obtain useful info about IP addresses.
    """
    # Split the input into IP address and CIDR notation
    ip_address, cidr_notation = cidr_input.split("/")
    cidr_notation = int(cidr_notation)

    # Split the IP address into octets
    ip_octets = list(map(int, ip_address.split(".")))

    # Determine the class of the IP address based on the first octet
    if 1 <= ip_octets[0] <= 127:
        ip_class = "A"
    elif 128 <= ip_octets[0] <= 191:
        ip_class = "B"
    elif 192 <= ip_octets[0] <= 223:
        ip_class = "C"
    elif 224 <= ip_octets[0] <= 239:
        ip_class = "D"
    else:
        ip_class = "E"

    # Calculate number of network and host bits
    network_bits = cidr_notation
    host_bits = 32 - network_bits

    # Calculate the total number of hosts
    total_hosts = 2**host_bits

    # Calculate the count of usable addresses (excluding network and broadcast)
    usable_addresses = total_hosts - 2  # Subtract 2 for network and broadcast addresses

    # Convert IP address to binary
    binary_ip = "".join([f"{octet:08b}" for octet in ip_octets])

    # Network address (binary)
    network_address_bin = binary_ip[:network_bits] + "0" * host_bits
    # Broadcast address (binary)
    broadcast_address_bin = binary_ip[:network_bits] + "1" * host_bits

    # Convert binary addresses back to decimal
    network_address = ".".join(
        [str(int(network_address_bin[i : i + 8], 2)) for i in range(0, 32, 8)]
    )
    broadcast_address = ".".join(
        [str(int(broadcast_address_bin[i : i + 8], 2)) for i in range(0, 32, 8)]
    )

    # Calculate the IP Gateway (first usable IP address)
    first_usable_ip_bin = (
        network_address_bin[:network_bits] + "0" * (host_bits - 1) + "1"
    )
    ip_gateway = ".".join(
        [str(int(first_usable_ip_bin[i : i + 8], 2)) for i in range(0, 32, 8)]
    )

    # Calculate the subnet mask
    subnet_mask_bin = "1" * network_bits + "0" * host_bits
    subnet_mask = ".".join(
        [str(int(subnet_mask_bin[i : i + 8], 2)) for i in range(0, 32, 8)]
    )
    subnet_mask_binary = ".".join([subnet_mask_bin[i : i + 8] for i in range(0, 32, 8)])
    binary_ip_address = ".".join([binary_ip[i : i + 8] for i in range(0, 32, 8)])

    # Calculate the range of possible IP addresses (including network and broadcast addresses)
    start_ip_address = network_address
    end_ip_address = broadcast_address

    # Calculate the range of possible host addresses (excluding network and broadcast addresses)
    start_host_address = ".".join(
        [str(int(network_address_bin[i : i + 8], 2)) for i in range(0, 32, 8)]
    )
    end_host_address = ".".join(
        [str(int(broadcast_address_bin[i : i + 8], 2)) for i in range(0, 32, 8)]
    )
    start_host_address_list = start_host_address.split(".")
    end_host_address_list = end_host_address.split(".")
    start_host_address_list[-1] = str(int(start_host_address_list[-1]) + 1)
    end_host_address_list[-1] = str(int(end_host_address_list[-1]) - 1)
    range_of_possible_host_addresses = (
        f"{'.'.join(start_host_address_list)} - {'.'.join(end_host_address_list)}"
    )

    # Print the results
    print(f"IP Class: {ip_class}")
    print(f"IP address (decimal): {ip_address}")
    print(f"IP address (binary): {binary_ip_address}")
    print(f"CIDR notation: /{cidr_notation}")
    print(f"Subnet Mask (decimal): {subnet_mask}")
    print(f"Subnet Mask (binary): {subnet_mask_binary}")
    print(f"Total octets: 4")
    print(f"Network octets: {network_bits // 8}")
    print(f"Host octets: {host_bits // 8}")

    print(f"Network address: {network_address}")
    print(f"Broadcast address: {broadcast_address}")
    print(f"IP Gateway: {ip_gateway}")
    print(f"Total number of host bits: {host_bits}")
    print(
        f"Total number of IP addresses (including network and broadcast): {total_hosts}"
    )
    print(f"Range of possible IP addresses: {start_ip_address} - {end_ip_address}")
    print(f"Number of possible hosts: {usable_addresses}")
    print(f"Range of Hosts: {range_of_possible_host_addresses}")


# Get user input in the form "0-255.0-255.0-255.0-255/xx"
cidr_input = input(
    "Enter the IP address with CIDR notation (e.g., 0-255.0-255.0-255.0-255/xx: "
)

ip_and_subnet_info(cidr_input)
