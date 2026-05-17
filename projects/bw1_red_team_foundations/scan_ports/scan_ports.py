import logging
import socket
import sys
from datetime import datetime


def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def setup_logging():
    log_filename = "port_scan.log"
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("Starting session")
    logging.info("Log file created")


def get_service_name(port, protocol):
    """
    Ottieni il nome del servizio per un determinato porto e protocollo.

    Parameters:
    port (int): Il numero di porto.
    protocol (str): Il protocollo ('tcp' o 'udp').

    Returns:
    str: Il nome del servizio.
    """
    try:
        service_name = socket.getservbyport(port, protocol)
    except OSError:
        service_name = "Unknown"
    return service_name


def port_scan_tcp(target_ip, start_port, end_port, timeout):
    logging.info(
        f"Scanning TCP ports on host: {target_ip} from port {start_port} to {end_port}"
    )
    open_ports = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            try:
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    service_name = get_service_name(port, "tcp")
                    print(f"TCP Port {port} ({service_name}): OPEN")
                    logging.info(f"TCP Port {port} ({service_name}): OPEN")
                    open_ports.append((port, service_name))
            except socket.error as e:
                logging.error(f"Error scanning TCP port {port}: {e}")

    return open_ports


def port_scan_udp(target_ip, start_port, end_port, timeout):
    logging.info(
        f"Scanning UDP ports on host: {target_ip} from port {start_port} to {end_port}"
    )
    open_ports = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.settimeout(timeout)
            try:
                sock.sendto(b"", (target_ip, port))
                sock.recvfrom(1024)
            except socket.timeout:
                service_name = get_service_name(port, "udp")
                print(f"UDP Port {port} ({service_name}): OPEN or FILTERED")
                logging.info(f"UDP Port {port} ({service_name}): OPEN or FILTERED")
                open_ports.append((port, service_name))
            except socket.error as e:
                logging.error(f"Error scanning UDP port {port}: {e}")

    return open_ports


def main():
    setup_logging()

    if len(sys.argv) != 4:
        print("Usage: python script.py <target_ip> <port_range> <timeout>")
        print("Example: python script.py 192.168.1.1 20-80 1.0")
        logging.error("Invalid arguments provided")
        sys.exit(1)

    target_ip = sys.argv[1]
    port_range = sys.argv[2]
    try:
        timeout = float(sys.argv[3])
    except ValueError:
        print("Invalid timeout value. Please provide a valid number.")
        logging.error("Invalid timeout value")
        sys.exit(1)

    if not is_valid_ip(target_ip):
        print("Invalid IP address. Please provide a valid IP address.")
        logging.error(f"Invalid IP address: {target_ip}")
        sys.exit(1)

    try:
        start_port, end_port = map(int, port_range.split("-"))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("Invalid port range. Please provide a valid range (e.g., 20-80).")
        logging.error(f"Invalid port range: {port_range}")
        sys.exit(1)

    logging.info("Starting port scan")
    open_tcp_ports = port_scan_tcp(target_ip, start_port, end_port, timeout)
    open_udp_ports = port_scan_udp(target_ip, start_port, end_port, timeout)
    logging.info("Port scan completed\n\n")

    if not open_tcp_ports and not open_udp_ports:
        print("\nNo open ports found.")
        logging.info("No open ports found.\n\n")


if __name__ == "__main__":
    main()
