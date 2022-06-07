import os
import urllib.request
import random
import requests
import config

class Connect:

    def __init__(self, search_item) -> None:
        self.search_term = search_item
        self.url = "https://api.unsplash.com/search/photos?"
        self.search = {"query": self.search_term}
        self.auth = {"Authorization": "Client-ID {}".format(config.client_id)}
        self.filtered_list = []


    def start(self):
        self.api_call = requests.get(self.url, params = self.search, headers=self.auth)
        try:
            json_response = self.api_call.json()
            self.api_call_limit = self.api_call.headers["X-Ratelimit-Remaining"]
            self.image_results = json_response["results"]
        except:
            print("The Json didn't receive the expected data from the API ( We're probably out of credits )")
            print("\nNumber of calls left for the hour: " + self.api_call_limit)
            quit()
    
    def filter_results(self):

        if len(self.image_results) >= 3:
            img_index_choices = list(range(0, len(self.image_results)))
            for chosen_items_a in random.sample(img_index_choices, 3):
                self.filtered_list.append(self.image_results[chosen_items_a])

        elif len(self.image_results) > 0 and len(self.image_results) < 3:
            for chosen_items_b in self.image_results:
                self.filtered_list.append(chosen_items_b)

        else:
            raise ValueError("Search term didn't return any items. Please search a different term.")

    def save_path(self):
        bin_path = "./bin/"
        check = os.path.isdir(bin_path)
        if not check:
            os.makedirs(bin_path)
        else:
            pass


    def download_images(self, final_list):
        self.file_num = 1
        for items in final_list:
            
            dl = items["links"]["download_location"]
            r = requests.get(dl, headers=self.auth, stream = True)
            
            if r.text == "Rate Limit Exceeded":
                raise ValueError("The Api Request limit was exceeded - Please try again in 60 minutes")
            else:
                links = r.json()
                
                urllib.request.urlretrieve(links["url"], "./bin/image_{}.jpg".format(self.file_num))
                self.file_num  += 1

    def summary(self):
        print("Total Number of items found for this search: " + str(len(self.image_results)))
        print("\nNumber of calls left for the hour: " + self.api_call_limit)
        input("Press any button to end...")