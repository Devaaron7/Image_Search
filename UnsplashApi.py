import os
import urllib.request
import random
import requests
import config

class Connect:

    def __init__(self, search_item) -> None:

        self.search_term = {"search": search_item}

        url_image_fetch = "http://127.0.0.1:5000/fetch-data"

        remaining_image_calls = "http://127.0.0.1:5000/fetch-limit"

        self.api_call_images = requests.post(url_image_fetch, json = search_item)

        self.api_call_limit = requests.post(remaining_image_calls, json = search_item)
        
        self.filtered_list = []


    def start(self):

        try:
            self.json_response_images = self.api_call_images.json()

            self.json_response_limit = self.api_call_limit.json()

            #breakpoint()

            self.limit_results = self.json_response_limit["X-Ratelimit-Remaining"]

            self.image_results = self.json_response_images["results"]
        except:
            print("The Json didn't receive the expected data from the API ( We're probably out of credits )")
            print("\nNumber of calls left for the hour: " + self.api_call_images_limit)
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

            download_route = "http://127.0.0.1:5000/fetch-data"
            
            download_port = items["links"]["download_location"]

            download_link = requests.post(download_route, json = download_port)


            image_request = requests.get(download_link, stream = True)
            
            if image_request.text == "Rate Limit Exceeded":
                raise ValueError("The Api Request limit was exceeded - Please try again in 60 minutes")
            else:
                links = image_request.json()
                
                urllib.request.urlretrieve(links["url"], "./bin/image_{}.jpg".format(self.file_num))
                self.file_num  += 1


    def summary(self):
        print("Total Number of items found for this search: " + str(len(self.image_results)))
        print("\nNumber of calls left for the hour: " + self.api_call_images_limit)
        input("Press any button to end...")