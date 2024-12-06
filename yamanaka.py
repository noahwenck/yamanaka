import sys

sys.dont_write_bytecode = True

import argparse

from stats import scatter
from stats import bar

parser = argparse.ArgumentParser(description="Whats up", formatter_class=argparse.RawTextHelpFormatter)
#todo: add check for if user actually exists
parser.add_argument("user", help="Letterboxd username")
args = parser.parse_args()

scatter(args.user)

bar(args.user, "Director")
bar(args.user, "Spoken Language")
bar(args.user, "Country")
bar(args.user, "Genre")
bar(args.user, "Studio")