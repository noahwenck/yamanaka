import sys

sys.dont_write_bytecode = True

import argparse
import asyncio
import gather
from stats import scatter, bar
import list_stats

parser = argparse.ArgumentParser(description="Create some stats.", formatter_class=argparse.RawTextHelpFormatter)
#todo: add check for if user actually exists
parser.add_argument("user", help="Letterboxd username")
args = parser.parse_args()

print("\nGathering Letterboxd data, this may take a while (up to several minutes)\n")

# Todo: cleanup / allow choice of what to do
user_films = gather.get_user_info(args.user).text

scatter(args.user, user_films)

bar(args.user,user_films, "Director")
bar(args.user, user_films, "Spoken Language")
bar(args.user, user_films, "Country")
bar(args.user, user_films, "Genre")
bar(args.user, user_films, "Studio")

asyncio.run(list_stats.compute_watched_from_official_lists(args.user, user_films))