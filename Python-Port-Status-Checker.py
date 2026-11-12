
import socket

def check_port(target, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Enable blocking mode
        sock.setblocking(True)
        sock.settimeout(5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")

        elif result == 10061:
            print(f"[-] Port {port} is CLOSED")

        elif result == 10060:
            print(f"[!] Port {port} timed out")

        else:
            print(f"[!] Error code: {result}")
            print("[!] Connection status unknown")

        sock.close()

    except socket.gaierror:
        print("[!] Invalid IP address")

    except OSError as error:
        print("[!] Network error:", error)

print("=" * 40)
print("       PORT STATUS CHECKER")
print("=" * 40)

target = input("Enter Target IP: ")

try:
    port = int(input("Enter Port Number: "))

    if 1 <= port <= 65535:
        check_port(target, port)
    else:
        print("Invalid port number")

except ValueError:
    print("Enter a valid port number")

print("=" * 40)
print("       SCAN COMPLETED")
print("=" * 40)
