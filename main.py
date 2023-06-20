import pickle
import pandas as pd
import re
from poster_url import get_poster_url

netflix_df = pd.read_pickle("models/netflix_shows_df.pkl")
netflix_similarities = pickle.load(open("models/netflix_similarities.pkl", "rb"))

amazon_prime_df = pd.read_pickle("models/amazon_prime_shows_df.pkl")
amazon_prime_similarities = pickle.load(open("models/amazon_prime_similarities.pkl", "rb"))

hulu_df = pd.read_pickle("models/hulu_shows_df.pkl")
hulu_similarities = pickle.load(open("models/hulu_similarities.pkl", "rb"))

hotstar_df = pd.read_pickle("models/hotstar_shows_df.pkl")
hotstar_similarities = pickle.load(open("models/hotstar_similarities.pkl", "rb"))




def recommend_show_netflix(title):
  title = re.sub(r"[^a-zA-Z1-9\s]", '', title, 0, re.MULTILINE)
  poster = get_poster_url(title)
  index = netflix_df[netflix_df["title"] == title].index[0]

  recommendation_list = {}
  for i in netflix_similarities[index]:
    name = netflix_df.iloc[i[0]]["title"]
    recommendation_list[name] = get_poster_url(name)

  return poster, recommendation_list



def recommend_show_amazon_prime(title):
  title = re.sub(r"[^a-zA-Z1-9\s]", '', title, 0, re.MULTILINE)
  poster = get_poster_url(title)
  index = amazon_prime_df[amazon_prime_df["title"] == title].index[0]

  recommendation_list = {}
  for i in amazon_prime_similarities[index]:
    name = amazon_prime_df.iloc[i[0]]["title"]
    recommendation_list[name] = get_poster_url(name)

  return poster, recommendation_list



def recommend_show_hulu(title):
  title = re.sub(r"[^a-zA-Z1-9\s]", '', title, 0, re.MULTILINE)
  poster = get_poster_url(title)
  index = hulu_df[hulu_df["title"] == title].index[0]

  recommendation_list = {}
  for i in hulu_similarities[index]:
    name = hulu_df.iloc[i[0]]["title"]
    recommendation_list[name] = get_poster_url(name)

  return poster, recommendation_list



def recommend_show_hotstar(title):
  title = re.sub(r"[^a-zA-Z1-9\s]", '', title, 0, re.MULTILINE)
  poster = get_poster_url(title)
  index = hotstar_df[hotstar_df["title"] == title].index[0]

  recommendation_list = {}
  for i in hotstar_similarities[index]:
    name = hotstar_df.iloc[i[0]]["title"]
    recommendation_list[name] = get_poster_url(name)

  return poster, recommendation_list