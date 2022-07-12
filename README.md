```
  _____  ______ _  ______  _   _ 
 |  __ \|  ____| |/ / __ \| \ | |
 | |__) | |__  | ' / |  | |  \| |
 |  _  /|  __| |  <| |  | | . ` |
 | | \ \| |____| . \ |__| | |\  |
 |_|  \_\______|_|\_\____/|_| \_|
```
                                 
# Install :

```sh
sh install.sh
```

Then, configure your shodan API key with :

```sh
shodan init {API_KEY}
```

# Usage : 

```sh
python3 rekon.py --cli
```


/!\ This version is vulnerable to os command injection, fix is coming 

## Credits :
- [shodan](https://shodan.io)
- [httpx](https://github.com/projectdiscovery/httpx)
