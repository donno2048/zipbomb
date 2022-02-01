from argparse import ArgumentParser
from . import make_zip
def main():
    args = ArgumentParser(description="Create a zip bomb")
    args.add_argument("-o", "--output", default="bomb.zip", help="output file")
    args.add_argument("-n", "--num-files", type=int, default=100, help="number of files in the zip")
    args.add_argument("-s", "--compressed-size", type=int, default=1000, help="compressed size of each file (in Kb)")
    args = args.parse_args()
    with open(args.output, "wb") as f: make_zip(f, args.num_files, args.compressed_size)
if __name__ == "__main__": main()
