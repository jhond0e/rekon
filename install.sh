#/bin/sh

apt install -y shodan, golang, python3, python3-pip
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
pip3 install -r requirements.txt
