# TODO: find a better solution
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

import json
import numpy as np
import pandas as pd
import torchtext


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
        print("# of user: {}".format(num_user))
        num_item = len(self.item_ids)
        print("# of item: {}".format(num_item))
        num_rating = len(self.data)
        print("# of rating: {}".format(num_rating))
        text_review = self.data["text_review"]
        tokenizer = torchtext.data.get_tokenizer("basic_english")
        num_words = sum([len(tokenizer(text)) for text in text_review])
        print("#words: {}".format(num_words))
        print(
            "avg #word in each review: {}".format(float(float(num_words) / num_rating))
        )
        num_empty_review = (text_review == "").sum()
        print(
            "{} empty text reviews. ({:.2%})".format(
                num_empty_review, float(float(num_empty_review) / num_rating)
            )
        )

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
        x = np.count_nonzero(cnt_list >= 5)
        print(
            "{} (of {} items) have >= 5 text reviews. ({:.2%})".format(
                x, num_item, float(float(x) / num_item)
            )
        )
        x = np.count_nonzero(cnt_list >= 10)
        print(
            "{} (of {} items) have >= 10 text reviews. ({:.2%})".format(
                x, num_item, float(float(x) / num_item)
            )
        )
        x = np.count_nonzero(cnt_list >= 20)
        print(
            "{} (of {} items) have >= 20 text reviews. ({:.2%})".format(
                x, num_item, float(float(x) / num_item)
            )
        )
        x = np.count_nonzero(cnt_list >= 50)
        print(
            "{} (of {} items) have >= 50 text reviews. ({:.2%})".format(
                x, num_item, float(float(x) / num_item)
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
        x = np.count_nonzero(cnt_list >= 5)
        print(
            "{} (of {} users) have >= 5 text reviews. ({:.2%})".format(
                x, num_user, float(float(x) / num_user)
            )
        )
        x = np.count_nonzero(cnt_list >= 10)
        print(
            "{} (of {} users) have >= 10 text reviews. ({:.2%})".format(
                x, num_user, float(float(x) / num_user)
            )
        )
        x = np.count_nonzero(cnt_list >= 20)
        print(
            "{} (of {} users) have >= 20 text reviews. ({:.2%})".format(
                x, num_user, float(float(x) / num_user)
            )
        )
        x = np.count_nonzero(cnt_list >= 50)
        print(
            "{} (of {} users) have >= 50 text reviews. ({:.2%})".format(
                x, num_user, float(float(x) / num_user)
            )
        )

    def name(self):
        return type(self).__name__


class AmazonInstantVideo(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonInstantVideo, self).__init__(path)


class AmazonAppsForAndroid(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonAppsForAndroid, self).__init__(path)


class AmazonAutomotive(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonAutomotive, self).__init__(path)


class AmazonBaby(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonBaby, self).__init__(path)


class AmazonBeauty(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonBeauty, self).__init__(path)


class AmazonBooks(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonBooks, self).__init__(path)


class AmazonCDsAndVinyl(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonCDsAndVinyl, self).__init__(path)


class AmazonCellPhonesAndAccessories(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonCellPhonesAndAccessories, self).__init__(path)


class AmazonClothingShoesAndJewelry(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonClothingShoesAndJewelry, self).__init__(path)


class AmazonDigitalMusic(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonDigitalMusic, self).__init__(path)


class AmazonElectronics(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonElectronics, self).__init__(path)


class AmazonGroceryAndGourmetFoods(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonGroceryAndGourmetFoods, self).__init__(path)


class AmazonHealthAndPersonalCare(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonHealthAndPersonalCare, self).__init__(path)


class AmazonHomeAndKitchen(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonHomeAndKitchen, self).__init__(path)


class AmazonKindleStore(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonKindleStore, self).__init__(path)


class AmazonMoviesAndTV(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonMoviesAndTV, self).__init__(path)


class AmazonMusicalInstruments(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonMusicalInstruments, self).__init__(path)


class AmazonOfficeProducts(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonOfficeProducts, self).__init__(path)


class AmazonPatioLawnAndGarden(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonPatioLawnAndGarden, self).__init__(path)


class AmazonPetSupplies(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonPetSupplies, self).__init__(path)


class AmazonSportsAndOutdoors(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonSportsAndOutdoors, self).__init__(path)


class AmazonToolsAndHomeImprovement(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonToolsAndHomeImprovement, self).__init__(path)


class AmazonToysAndGames(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonToysAndGames, self).__init__(path)


class AmazonVideoGames(AmazonDatasetIf):
    def __init__(self, path):
        super(AmazonVideoGames, self).__init__(path)


amazon_dataset_path = "/Users/xfjiang/workspace/dataset/amazon"

if __name__ == "__main__":
    dataset = AmazonInstantVideo(
        os.path.join(amazon_dataset_path, "reviews_Amazon_Instant_Video_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonAppsForAndroid(
        os.path.join(amazon_dataset_path, "reviews_Apps_for_Android_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonAutomotive(
        os.path.join(amazon_dataset_path, "reviews_Automotive_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonBaby(os.path.join(amazon_dataset_path, "reviews_Baby_5.json"))
    dataset.info()
    print("\n\n")
    dataset = AmazonBeauty(os.path.join(amazon_dataset_path, "reviews_Beauty_5.json"))
    dataset.info()
    print("\n\n")
    dataset = AmazonBooks(os.path.join(amazon_dataset_path, "reviews_Books_5.json"))
    dataset.info()
    print("\n\n")
    dataset = AmazonCDsAndVinyl(
        os.path.join(amazon_dataset_path, "reviews_CDs_and_Vinyl_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonCellPhonesAndAccessories(
        os.path.join(amazon_dataset_path, "reviews_Cell_Phones_and_Accessories_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonClothingShoesAndJewelry(
        os.path.join(amazon_dataset_path, "reviews_Clothing_Shoes_and_Jewelry_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonDigitalMusic(
        os.path.join(amazon_dataset_path, "reviews_Digital_Music_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonElectronics(
        os.path.join(amazon_dataset_path, "reviews_Electronics_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonGroceryAndGourmetFoods(
        os.path.join(amazon_dataset_path, "reviews_Grocery_and_Gourmet_Food_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonHealthAndPersonalCare(
        os.path.join(amazon_dataset_path, "reviews_Health_and_Personal_Care_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonHomeAndKitchen(
        os.path.join(amazon_dataset_path, "reviews_Home_and_Kitchen_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonKindleStore(
        os.path.join(amazon_dataset_path, "reviews_Kindle_Store_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonMoviesAndTV(
        os.path.join(amazon_dataset_path, "reviews_Movies_and_TV_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonMusicalInstruments(
        os.path.join(amazon_dataset_path, "reviews_Musical_Instruments_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonOfficeProducts(
        os.path.join(amazon_dataset_path, "reviews_Office_Products_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonPatioLawnAndGarden(
        os.path.join(amazon_dataset_path, "reviews_Patio_Lawn_and_Garden_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonPetSupplies(
        os.path.join(amazon_dataset_path, "reviews_Pet_Supplies_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonSportsAndOutdoors(
        os.path.join(amazon_dataset_path, "reviews_Sports_and_Outdoors_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonToolsAndHomeImprovement(
        os.path.join(amazon_dataset_path, "reviews_Tools_and_Home_Improvement_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonToysAndGames(
        os.path.join(amazon_dataset_path, "reviews_Toys_and_Games_5.json")
    )
    dataset.info()
    print("\n\n")
    dataset = AmazonVideoGames(
        os.path.join(amazon_dataset_path, "reviews_Video_Games_5.json")
    )
    dataset.info()
    print("\n\n")
