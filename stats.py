import io
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from PIL import Image

from gather import get_user_info

JPG = ".jpg"

def scatter(username, user_films):
    """
    Generates a scatter plot of films for a specified user.

    Parameters:
    username (str): The username to fetch film data for.
    """
    films = pd.read_json(io.StringIO(user_films))

    sns.scatterplot(x="Year", y="Average Rating", hue="Primary Language", data=films)
    plt.legend(bbox_to_anchor=(1,1))
    plt.savefig(username + "-Year-AverageRating-PrimaryLanguage" + JPG, bbox_inches='tight')

    Image.open(username + "-Year-AverageRating-PrimaryLanguage" + JPG).show()
    plt.clf()

def bar(username, user_films, category):
    """
    Generates a bar chart for the given category of films for a specified user.

    Parameters:
    username (str): The username to fetch film data for.
    category (str): The category to analyze and plot (e.g., 'Director').
    """
    films = pd.read_json(io.StringIO(user_films))

    films[category] = films[category].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    films_exploded = films.explode(category)
    director_counts = films_exploded[category].value_counts()
    director_counts = director_counts[director_counts > 1]
    director_counts.sort_values(ascending=False, inplace=True)

    sns.barplot(x=director_counts.index, y=director_counts.values)
    plt.xlabel(category)
    plt.ylabel("Number of Films")
    plt.xticks(rotation=45, ha='right')
    plt.legend([],[], frameon=False)
    plt.savefig(username + "-" + category + JPG, bbox_inches='tight')

    Image.open(username + "-" + category + JPG).show()
    plt.clf()