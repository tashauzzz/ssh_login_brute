# SSH Login Brute

A simple Python script that demonstrates **SSH brute-force password attempts** against a known username on a target host.  
⚠️ **Do not run against systems without explicit authorization.**

---

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

---

## Installation

```bash
git clone https://github.com/tashauzzz/ssh_login_brute.git
cd ssh_login_brute
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows PowerShell
pip install -r requirements.txt
