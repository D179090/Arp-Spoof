# Arp-Spoof
This is a repository with the current version of the Arp-Spoof program for python
#### Supported platforms:
* Linux
* Windows(not tested)
# How to use?
* On l=Linux:
```bash
python3 -m venv $folder-project
source $folder-project/bin/activate
pip3 install requirements.txt
sudo python3 Arp-Spoof.py <victim's IP address> <router ip address>
sudo python3 Arp-Spoof.py <router ip address> <victim's IP address>
```
* On Windows
  Install Python 3
  ```Powershell
  python3 -m venv $foler-project
  cd "$folder-project/Scripts"
  activate
  python3 Arp-Spoof.py <victim's IP address> <router ip address>
  python3 Arp-Spoof.py <router ip address> <victim's IP address>
  ```
