import os
import argparse
import numpy as np
import pandas as pd
import json
import nltk
import matplotlib.pyplot as plt


class Amazon(object):
    """
    http://jmcauley.ucsd.edu/data/amazon/links.html
    """

    def __init__(self, path, log_dir):
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
        self.log_dir = log_dir

    def get_info(self):
        # 1. basic statistics
        stat = pd.DataFrame(
            index=np.arange(0, 1),
            columns=[
                "num_user",
                "num_item",
                "num_rating(review)",
                "avg_review_per_item",
                "total_words",
                "avg_words_per_review",
                "empty_review",
            ],
        )
        num_user = len(self.user_ids)
        num_item = len(self.item_ids)
        num_rating = len(self.data)
        avg_review_per_item = float(num_rating) / num_item
        text_review = self.data["text_review"]
        total_words = sum([len(nltk.word_tokenize(text)) for text in text_review])
        avg_words_per_review = float(float(total_words) / num_rating)
        empty_review = (text_review == "").sum()
        stat.loc[0] = [
            num_user,
            num_item,
            num_rating,
            avg_review_per_item,
            total_words,
            avg_words_per_review,
            empty_review,
        ]
        stat.to_csv(os.path.join(self.log_dir, "stat.csv"))

        # 2. histogram: num of reviews w.r.t. item
        cnts = [len(reviews) for reviews in self.item_id2doc.values()]
        plt.hist(cnts, bins=list(range(100)))
        plt.savefig(os.path.join(self.log_dir, "hist.png"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default="", type=str)
    parser.add_argument("--log_dir", default="log", type=str)
    args = parser.parse_args()
    
    if not os.path.exists(args.log_dir):
        os.makedirs(args.log_dir)
    dataset = Amazon(args.path, args.log_dir)
    dataset.get_info()
