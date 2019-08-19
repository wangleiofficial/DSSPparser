"""
TODO: cmd line pdbToxssp
"""
import argparse
from DSSPparser import pdbToxssp, inputCollection, outputCollection


def main():
    parser = argparse.ArgumentParser(description='cmd line pdbToxssp')
    parser.add_argument('input', dest='input', type=str, help='input context')
    parser.add_argument("--informat", type=str, dest='infortmat', help='input format', choices=inputCollection)
    parser.add_argument("--outformat", type=str, dest='outformat', help='output format', choices=outputCollection)
    args = parser.parse_args()
    pdbToxssp(args.input, inputF=args.infortmat, outputF=args.outformat)


if __name__ == '__main__':
    main()
