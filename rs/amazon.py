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

    def info(self):
        print(self.name())
        print("*" * 20 + "Basic Statistics" + "*" * 20)
        num_user = len(self.user_ids)
        print("number of user: {}".format(num_user))
        num_item = len(self.item_ids)
        print("number of item: {}".format(num_item))
        num_rating = len(self.data)
        print("number of rating: {}".format(num_rating))
        text_review = self.data["text_review"]
        num_empty_review = (text_review == "").sum()
        print("{} empty text reviews".format(num_empty_review))

        print("*" * 20 + "Rating(Review) Statistics w.r.t. Item" + "*" * 20)
        print(
            "average num of rating w.r.t. item: {}".format(
                float(float(num_rating) / num_item)
            )
        )
        cnt_list = []
        for _, doc in self.item_id2doc.items():
            cnt_list.append(len(doc))
        cnt_list = np.array(cnt_list)
        print(
            "{} (of {} items) have >= 5 text reviews".format(
                np.count_nonzero(cnt_list >= 5), num_item
            )
        )
        print(
            "{} (of {} items) have >= 10 text reviews".format(
                np.count_nonzero(cnt_list >= 10), num_item
            )
        )
        print(
            "{} (of {} items) have >= 20 text reviews".format(
                np.count_nonzero(cnt_list >= 20), num_item
            )
        )

        print("*" * 20 + "Rating(Review) Statistics w.r.t. User" + "*" * 20)
        print(
            "average num of rating w.r.t. user: {}".format(
                float(float(num_rating) / num_user)
            )
        )
        cnt_list = []
        for _, doc in self.user_id2doc.items():
            cnt_list.append(len(doc))
        cnt_list = np.array(cnt_list)
        print(
            "{} (of {} users) have >= 5 text reviews".format(
                np.count_nonzero(cnt_list >= 5), num_user
            )
        )
        print(
            "{} (of {} users) have >= 10 text reviews".format(
                np.count_nonzero(cnt_list >= 5), num_user
            )
        )
        print(
            "{} (of {} users) have >= 20 text reviews".format(
                np.count_nonzero(cnt_list >= 5), num_user
            )
        )

    def name(self):
        return type(self).__name__


class AmazonGroceryAndGourmetFoods(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonGroceryAndGourmetFoods, self).__init__(path)


class AmazonVideoGames(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonVideoGames, self).__init__(path)


class AmazonElectronics(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonElectronics, self).__init__(path)


if __name__ == "__main__":
    amazon_foods = AmazonGroceryAndGourmetFoods(
        "/Users/xfjiang/workspace/dataset/reviews_Grocery_and_Gourmet_Food_5.json"
    )
    amazon_foods.info()
    amazon_video_games = AmazonVideoGames(
        "/Users/xfjiang/workspace/dataset/reviews_Video_Games_5.json"
    )
    amazon_video_games.info()
    amazon_electronics = AmazonElectronics(
        "/Users/xfjiang/workspace/dataset/reviews_Electronics_5.json"
    )
    amazon_electronics.info()
