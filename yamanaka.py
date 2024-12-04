import sys

sys.dont_write_bytecode = True

import argparse

from stats import scatter

parser = argparse.ArgumentParser(description="Whats up", formatter_class=argparse.RawTextHelpFormatter)

# REQUIRED
#todo: add check for if user actually exists
parser.add_argument("user", help="Letterboxd username")

args = parser.parse_args()

scatter(args.user)