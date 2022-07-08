import os
import json
import numpy as np



class Yelp(object):
    """
    https://www.yelp.com/dataset/documentation/main/
    """

    def __init__(self, dataset_path):
        self.review_json_list = []
        self.user_json_list = []
        self.business_json_list = []
        # with open(
        #     os.path.join(dataset_path, "yelp_academic_dataset_review.json"), "rb"
        # ) as f:
        #     for line in f:
        #         self.review_json_list.append(json.loads(line))
        with open(
            os.path.join(dataset_path, "yelp_academic_dataset_user.json"), "rb"
        ) as f:
            for line in f:
                self.user_json_list.append(json.loads(line))
        # with open(
        #     os.path.join(dataset_path, "yelp_academic_dataset_business.json"), "rb"
        # ) as f:
        #     for line in f:
        #         self.business_json_list.append(json.loads(line))


if __name__ == "__main__":
    yelp = Yelp("/Users/xfjiang/workspace/dataset/yelp")
    review_counts = []
    for user_json in yelp.user_json_list:
        review_counts.append(int(user_json["review_count"]))
    review_counts = np.array(review_counts)
    print("min review count: {}".format(np.min(review_counts)))                                 # 0
    print("maximum review count: {}".format(np.max(review_counts)))                             # 17473
    print("mean review count: {}".format(np.mean(review_counts)))                               # 23
    print("median review count: {}".format(np.median(review_counts)))                           # 5
    print("num of users with num of reviews >= 5: {}".format((review_counts >= 5).sum()))       # 1087094
    print("num of users with num of reviews >= 10: {}".format((review_counts >= 10).sum()))     # 726519
    print("num of users with num of reviews >= 20: {}".format((review_counts >= 20).sum()))     # 436498
    print("num of users with num of reviews >= 100: {}".format((review_counts >= 100).sum()))   # 91774
