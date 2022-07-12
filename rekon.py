import sys
import os
from time import *
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
import argparse
from colorama import Fore, Back, Style
import subprocess


def exec(cmd): #Prevent OS command injection
	args = []
	if cmd.find(" ") != -1:
		for i in range(len(cmd.split(" "))):
			args.append(cmd.split(" ")[i])
	return subprocess.call(args)


def parse(path, fields):
	out = input("Output file > ")
	if fields == "http":
		os.system("shodan parse --fields ip_str,port --separator , "+path+" | sed '/^[[:space:]]*$/d' | sort -u > "+out+".tmp")
		os.system("cat "+out+".tmp | sed 's/,/:/' | httpx -o "+out+" -silent > /dev/null")
		os.system("rm "+out+".tmp && rm "+path)
		print (Fore.GREEN + "[+] Your data has been saved !")
		return 1
	os.system("shodan parse --fields "+fields+" --separator , "+path+" | sed '/^[[:space:]]*$/d' | sort -u > "+out)
	os.system("cat "+out+"| sed 's/;/\\n/g' > /tmp/tmp")
	os.system("mv /tmp/tmp "+out)
	os.system("rm "+path)
	print (Fore.GREEN + "[+] Your data has been saved !")

print("*"*50)
cprint(figlet_format('REKON', font='slant'))
print("Created by @JhonD0e")
print("*"*50)
sleep(0.2)
parser = argparse.ArgumentParser()
parser.add_argument('--cli', help='interactive mode', action='store_true')
if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)
args = parser.parse_args()
if args.cli:
	menu = "\nWhat's your initial information ? :\n\t1- Organization's name\n\t2- Domain name\n\t3- SSL Certificates\n"
	for char in menu:
		sleep(0.005)
		sys.stdout.write(char)
		sys.stdout.flush()
	mode = input(">")
	add = ""
	if mode == "1":
		info = input("Org name > ")
		type = "org"
	elif mode == "2":
		info = input("Domain name > ")
		type = "hostname"
	elif mode == "3":
		info = input("SSL Certificates > ")
		type = "ssl"
		add = "200"
	print (Fore.BLUE + "[*] Checking shodan infos...")
	if (str(os.system("shodan info | grep Error")).find("Error") == -1):
		print (Fore.GREEN + "[+] Valid API key found !")
		print (Fore.BLUE + "[*] Download data from Shodan..." + Fore.WHITE)
		os.system("shodan download /tmp/{}.tmp {}:'{}' {} --limit 1000000".format(info, type, info, add))
		print (Fore.GREEN + "[+] Data has been downloaded successfully !")
		print (Fore.WHITE + "What do you want to get ? :\n\t1- Domains\n\t2- IPs list\n\t3- IPs/Ports list\n\t4- HTTP/HTTPS servers")
		data = input(">")
		if data == "1":
			parse("/tmp/{}.tmp.json.gz".format(info), "domains")
		elif data == "2":
			parse("/tmp/{}.tmp.json.gz".format(info), "ip_str")
		elif data == "3":
			parse("/tmp/{}.tmp.json.gz".format(info), "ip_str,port")
		elif data == "4":
			parse("/tmp/{}.tmp.json.gz".format(info), "http")
	else:
		print (Fore.RED + "[-] Please set your api key via : 'shodan init {API_KEY}' ")
