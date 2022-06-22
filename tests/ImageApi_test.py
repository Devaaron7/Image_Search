import os
import urllib.request
import random
import requests

class Connect:

    def __init__(self, search_item) -> None:

        self.search_term = {"search": search_item}

        url_image_fetch = "https://search-unsplash-image.herokuapp.com/fetch-data"

        remaining_image_calls = "https://search-unsplash-image.herokuapp.com/fetch-limit"

        self.api_call_images = requests.post(url_image_fetch, json = search_item)

        self.api_call_limit = requests.post(remaining_image_calls, json = search_item)
        
        self.filtered_list = []

        self.dl_list_to_return = []


    def start(self):

        self.json_response_limit = self.api_call_limit.json()

        if self.json_response_limit["X-Ratelimit-Remaining"] == 0:
            return "The Api Request limit was exceeded - Please try again in 60 minutes"
        
        
        self.json_response_images = self.api_call_images.json()

        if len(self.json_response_images["results"]) == 0:

            return "No results from your current search term. Please try another term"
        else:

            self.limit_results = self.json_response_limit["X-Ratelimit-Remaining"]
            self.image_results = self.json_response_images["results"]

        
             
    

    def filter_results(self):

        if len(self.image_results) >= 3:
            img_index_choices = list(range(0, len(self.image_results)))
            for chosen_items_a in random.sample(img_index_choices, 3):
                self.filtered_list.append(self.image_results[chosen_items_a])

        if len(self.image_results) > 0 and len(self.image_results) < 3:
            for chosen_items_b in self.image_results:
                self.filtered_list.append(chosen_items_b)



    def download_images(self, final_list):
        
        self.file_num = 1
        for items in final_list:

            download_route = "https://search-unsplash-image.herokuapp.com/fetch-download"
            
            download_port = items["links"]["download_location"]

            download_link = requests.post(download_route, json = download_port)
            
            if download_link.text == "Rate Limit Exceeded":
                return "The Api Request limit was exceeded - Please try again in 60 minutes"
            
            elif "500" in download_link.text:
                return "The Api Request limit was exceeded - Please try again in 60 minutes"

            else:
                links = download_link.json()

                self.dl_list_to_return.append(links)
