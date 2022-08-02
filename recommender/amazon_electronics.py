import json


class AmazonDatasetIf(object):
    """
    http://jmcauley.ucsd.edu/data/amazon/links.html
    """

    def __init__(self, file_path):
        self.user_id_list = []
        self.item_id_list = []
        self.text_review_list = []
        self.rating_list = []
        self.user_ids = set()
        self.item_ids = set()
        with open(file_path, "rb") as f:
            for line in f:
                js = json.loads(line)
                user_id = str(js["reviewerID"])
                item_id = str(js["asin"])
                self.user_ids.add(user_id)
                self.item_ids.add(item_id)
                self.user_id_list.append(user_id)
                self.item_id_list.append(item_id)
                self.text_review_list.append(str(js["reviewText"]))
                self.rating_list.append(float(js["overall"]))


class AmazonElectronics(AmazonDatasetIf):
    """
    http://jmcauley.ucsd.edu/data/amazon/links.html
    """

    def __init__(self, file_path):
        super(AmazonElectronics, self).__init__(file_path)
        print("number of user: {}".format(len(self.user_ids)))  # 192403
        print("number of item: {}".format(len(self.item_ids)))  # 63001
        print("number of rating: {}".format(len(self.rating_list)))  # 1689188


class AmazonVideoGames(AmazonDatasetIf):
    """
    http://jmcauley.ucsd.edu/data/amazon/links.html
    """

    def __init__(self, file_path):
        super(AmazonVideoGames, self).__init__(file_path)
        print("number of user: {}".format(len(self.user_ids)))  # 24303
        print("number of item: {}".format(len(self.item_ids)))  # 10672
        print("number of rating: {}".format(len(self.rating_list)))  # 231780


class AmazonGourmetFoods(AmazonDatasetIf):
    """
    http://jmcauley.ucsd.edu/data/amazon/links.html
    """

    def __init__(self, file_path):
        super(AmazonGourmetFoods, self).__init__(file_path)
        print("number of user: {}".format(len(self.user_ids)))  # 14681
        print("number of item: {}".format(len(self.item_ids)))  # 8713
        print("number of rating: {}".format(len(self.rating_list)))  # 151254


if __name__ == "__main__":
    amazon_electronics_dataset = AmazonElectronics(
        "/Users/xfjiang/workspace/dataset/reviews_Electronics_5.json"
    )
    amazon_video_games_dataset = AmazonVideoGames(
        "/Users/xfjiang/workspace/dataset/reviews_Video_Games_5.json"
    )
    amazon_video_games_dataset = AmazonGourmetFoods(
        "/Users/xfjiang/workspace/dataset/reviews_Grocery_and_Gourmet_Food_5.json"
    )
