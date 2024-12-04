import io
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from PIL import Image

from gather import get_user_info

JPG = ".jpg"

def scatter(username):
    films = pd.read_json(io.StringIO(get_user_info(username).text))

    sns.scatterplot(x="Year", y="Average Rating", hue="Primary Language", data=films)
    plt.legend(bbox_to_anchor=(1,1))
    plt.savefig(username + "-Year-AverageRating-PrimaryLanguage" + JPG, bbox_inches='tight')

    Image.open(username + "-Year-AverageRating-PrimaryLanguage" + JPG).show()