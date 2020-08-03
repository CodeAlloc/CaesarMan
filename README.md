# CaesarMan
CaesarMan is a tool that encypts/decrypts Caesar based Ciphers.

  
# Main Features:
  - Decryption of data using a Brute Force mode
  - Usage of an "intelligent" mode to Brute Force the cipher more effectively, if written in English Language

### Installation

CaesarMan requires Python 3+.
To use it as a tool, Download the release zip, unpack it. and use CaesarMan .py via python3 shell:

```sh
$ python3 CaesarMan.py
```
or in Linux or MacOS, install the tool on path as follows:
```sh
$ git clone https://www.github.com/chmuhammadsohaib/CaesarMan
$ cd CaesarMan
$ chmod +x CaesarMan.py
```

and afterward use the tool by typing ./CaesarMan.py .

### Brute Force & Intelligent Mode
You can simply brute force to crack a Caesar Cipher using this tool. Intelligent mode brute forces by a technique we analyzed using a statistical model, to lessen the possible original text output, in order to make brute forcing a lot more efficient. Intelligent mode, however, is availabe only for Pure English Language.

