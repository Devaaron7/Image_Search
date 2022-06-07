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
        #breakpoint()
        self.api_call_limit = self.api_call.headers["X-Ratelimit-Remaining"]
        json_response = self.api_call.json()
        self.image_results = json_response["results"]
        
            # print("The Json didn't receive the expected data from the API ( We're probably out of credits )")
            # print("\nNumber of calls left for the hour: " + self.api_call_limit)
            # quit()
    
    def filter_results(self):
        #self.filtered_list = []

        if len(self.image_results) >= 3:
            img_index_choices = list(range(0, len(self.image_results)))
            for chosen_items_a in random.sample(img_index_choices, 3):
                self.filtered_list.append(self.image_results[chosen_items_a])

        elif len(self.image_results) > 0 and len(self.image_results) < 3:
            for chosen_items_b in self.image_results:
                self.filtered_list.append(chosen_items_b)

        else:
            raise ValueError("Search term didn't return any items. Please search a different term.")


    def download_images(self, final_list):
        self.file_num = 1
        #breakpoint()
        for items in final_list:
            dl = items["links"]["download_location"]
            r = requests.get(dl, headers=config.client_id, stream = True)
            breakpoint()
            

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


# #Connection
# url = "https://api.unsplash.com/search/photos?"
# search = {"query": term}
# auth = {"Authorization": "Client-ID {}".format(config.client_id)}


# # Data Response & Setting Variables 
# api_call = requests.get(url, params = search, headers=auth)
# #breakpoint()
# api_call_limit = api_call.headers["X-Ratelimit-Remaining"]

# # Error catching if out of credits for api calls
# try:
#     json_response = api_call.json()
# except:
#     print("The Json didn't receive the expected data from the API ( We're probably out of credits )")
#     print("\nNumber of calls left for the hour: " + api_call_limit)
#     quit()

# image_results = json_response["results"]


# Logic to return maxiumum of 3 images randomly from results
# filtered_results = []

# if len(image_results) >= 3:
#     img_index_choices = list(range(0, len(image_results)))
#     for chosen_items_a in random.sample(img_index_choices, 3):
#         filtered_results.append(image_results[chosen_items_a])
# elif len(image_results) > 0 and len(image_results) < 3:
#     for chosen_items_b in image_results:
#         filtered_results.append(chosen_items_b)
# else:
#     raise ValueError("Search term didn't return any items. Please search a different term.")


#Download logic + Naming file with numeric ascending numbers
# n = 1
# for items in filtered_results:
#     dl = items["links"]["download_location"]
#     r = requests.get(dl, headers=auth, stream = True)

#     if r.text == "Rate Limit Exceeded":
#         raise ValueError("The Api Request limit was exceeded - Please try again in 60 minutes")
#     else:
#         links = r.json()
#         urllib.request.urlretrieve(links["url"], "./bin/image_{}.jpg".format(n))
#         n += 1

#Opens folder where download jpegs are
# os.system("cmd /c start {}".format(os.getcwd() + "/bin"))

# print("Total Number of items found for this search: " + str(len(image_results)))
# print("\nNumber of calls left for the hour: " + api_call_limit)
# input("Press any button to end...")