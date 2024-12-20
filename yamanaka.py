import sys

sys.dont_write_bytecode = True

import argparse
from stats import scatter
from stats import bar
from list_stats import compute_watched_from_official_lists

parser = argparse.ArgumentParser(description="Whats up", formatter_class=argparse.RawTextHelpFormatter)
#todo: add check for if user actually exists
parser.add_argument("user", help="Letterboxd username")
args = parser.parse_args()

# Todo: cleanup / allow choice of what to do
# Todo: store films locally (especially user films) between calls
scatter(args.user)

bar(args.user, "Director")
bar(args.user, "Spoken Language")
bar(args.user, "Country")
bar(args.user, "Genre")
bar(args.user, "Studio")

compute_watched_from_official_lists(args.user)