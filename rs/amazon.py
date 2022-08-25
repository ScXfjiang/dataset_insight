import json
import numpy as np
import pandas as pd


class AmazonDatasetIf(object):
    """
    http://jmcauley.ucsd.edu/data/amazon/links.html
    """

    def __init__(self, path):
        with open(path, "rb") as f:
            self.data = pd.DataFrame(
                index=np.arange(0, len(f.readlines())),
                columns=["user_id", "item_id", "rating", "text_review"],
            )
            f.seek(0)
            for idx, line in enumerate(f):
                js = json.loads(line)
                self.data.loc[idx] = [
                    str(js["reviewerID"]),
                    str(js["asin"]),
                    float(js["overall"]),
                    str(js["reviewText"]),
                ]
            self.user_ids = set(self.data["user_id"])
            self.item_ids = set(self.data["item_id"])
            self.item_id2doc = {}
            for item_id, group in self.data.groupby("item_id"):
                doc = list(group["text_review"])
                self.item_id2doc[item_id] = doc
            self.user_id2doc = {}
            for user_id, group in self.data.groupby("user_id"):
                doc = list(group["text_review"])
                self.user_id2doc[user_id] = doc


class AmazonElectronics(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonElectronics, self).__init__(path)
        print("number of user: {}".format(len(self.user_ids)))  # 192403
        print("number of item: {}".format(len(self.item_ids)))  # 63001


class AmazonVideoGames(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonVideoGames, self).__init__(path)
        print("number of user: {}".format(len(self.user_ids)))  # 24303
        print("number of item: {}".format(len(self.item_ids)))  # 10672


class AmazonGourmetFoods(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonGourmetFoods, self).__init__(path)

        print("*" * 20 + "Basic Statistics" + "*" * 20)
        num_user = len(self.user_ids)
        print("number of user: {}".format(num_user))  # 14681
        num_item = len(self.item_ids)
        print("number of item: {}".format(num_item))  # 8713
        num_rating = len(self.data)
        print("number of rating: {}".format(num_rating))  # 151254

        text_review = self.data["text_review"]
        print(type(text_review))
        

        print("*" * 20 + "Rating(Review) Statistics w.r.t. item" + "*" * 20)
        print(
            "average num of rating w.r.t. item: {}".format(
                float(float(num_rating) / num_item)
            )  # 17.4
        )

        print("*" * 20 + "Rating(Review) Statistics w.r.t. user" + "*" * 20)
        print(
            "average num of rating w.r.t. user: {}".format(
                float(float(num_rating) / num_user)
            )  # 10.3
        )


if __name__ == "__main__":
    # amazon_electronics_dataset = AmazonElectronics(
    #     "/home/people/22200056/workspace/dataset/reviews_Electronics_5.json"
    # )
    # amazon_video_games_dataset = AmazonVideoGames(
    #     "/home/people/22200056/workspace/dataset/reviews_Video_Games_5.json"
    # )
    amazon_video_games_dataset = AmazonGourmetFoods(
        "/home/people/22200056/workspace/dataset/reviews_Grocery_and_Gourmet_Food_5.json"
    )
