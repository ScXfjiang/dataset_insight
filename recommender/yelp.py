from cgitb import text
import os
import json
from tkinter import W
import numpy as np


class Yelp(object):
    """
    https://www.yelp.com/dataset/documentation/main/
    """

    def __init__(self, dataset_path):
        self.review_json_list = []
        self.user_json_list = []
        self.business_json_list = []
        with open(
            os.path.join(dataset_path, "yelp_academic_dataset_review.json"), "rb"
        ) as f:
            for line in f:
                self.review_json_list.append(json.loads(line))
        with open(
            os.path.join(dataset_path, "yelp_academic_dataset_user.json"), "rb"
        ) as f:
            for line in f:
                self.user_json_list.append(json.loads(line))
        with open(
            os.path.join(dataset_path, "yelp_academic_dataset_business.json"), "rb"
        ) as f:
            for line in f:
                self.business_json_list.append(json.loads(line))


if __name__ == "__main__":
    yelp = Yelp("/Users/xfjiang/workspace/dataset/yelp")
    if False:
        # number of ratings: 6990280
        num_review = len(yelp.review_json_list)
        # number of users: 1987897
        num_user = len(yelp.user_json_list)
        # number of businesses: 150346
        num_businee = len(yelp.business_json_list)

        pass

    if False:
        # text review: each text review has at least one character
        char_cnts = []
        for review_json in yelp.review_json_list:
            text_review = str(review_json["text"])
            char_cnts.append(int(len(text_review)))
        char_cnts = np.array(char_cnts)
        print("min char count: {}".format(np.min(char_cnts)))
        print("maximum char count: {}".format(np.max(char_cnts)))
        print("mean char count: {}".format(np.mean(char_cnts)))
        print("median char count: {}".format(np.median(char_cnts)))

        pass

    if False:
        # review counts from users
        review_counts = []
        for user_json in yelp.user_json_list:
            review_counts.append(int(user_json["review_count"]))
        review_counts = np.array(review_counts)
        print("min review count: {}".format(np.min(review_counts)))  # 0
        print("maximum review count: {}".format(np.max(review_counts)))  # 17473
        print("mean review count: {}".format(np.mean(review_counts)))  # 23
        print("median review count: {}".format(np.median(review_counts)))  # 5
        print(
            "num of users with num of reviews >= 5: {}".format(
                (review_counts >= 5).sum()
            )
        )  # 1087094
        print(
            "num of users with num of reviews >= 10: {}".format(
                (review_counts >= 10).sum()
            )
        )  # 726519
        print(
            "num of users with num of reviews >= 20: {}".format(
                (review_counts >= 20).sum()
            )
        )  # 436498
        print(
            "num of users with num of reviews >= 100: {}".format(
                (review_counts >= 100).sum()
            )
        )  # 91774

        pass

    pass
