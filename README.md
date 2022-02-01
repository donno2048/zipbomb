# zipbomb

Create zipbombs using python

Based on [David Fifield's project](https://www.bamsoftware.com/hacks/zipbomb/)

## Installation

### From PyPI

```sh
pip3 install zipbomb
```

### From GitHub

```sh
pip3 install git+https://github.com/donno2048/zipbomb
```

## Usage

```sh
$ zipbomb -h
usage: zipbomb [-h] [-o OUTPUT] [-n NUM_FILES] [-s COMPRESSED_SIZE]

Create a zip bomb

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file [default: bomb.zip]
  -n NUM_FILES, --num-files NUM_FILES
                        number of files in the zip [default: 100]
  -s COMPRESSED_SIZE, --compressed-size COMPRESSED_SIZE
                        compressed size of each file (in Kb) [default: 1000]

```
