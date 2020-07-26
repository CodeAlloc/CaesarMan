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
### Intelligent Mode
Intelligent mode uses the vowels inclusion in almost every word of english language to make decipher efficient. There are exceptions as well, which are regularly updated in exceptions.nhx file.

## Contribute
You can contribute either by sending pull requests with improved code, or also by sending pull requests with updated exceptions.nhx file (by adding more English Words which don't have a vowel).
