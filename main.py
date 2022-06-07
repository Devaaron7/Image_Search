from UnsplashApi import Connect


term = str(input("Please enter a search term.\n"))

# Connection
session = Connect(term)

# Data Response, Setting Variables & Error catching if out of credits for api calls
#breakpoint()
#breakpoint()
session.start()

# Logic to return maxiumum of 3 images randomly from results
session.filter_results()

#print(session.filtered_list)


# Download logic + Naming file with numeric ascending numbers
breakpoint()
session.download_images(session.filtered_list)


# Opens folder where download jpegs are
os.system("cmd /c start {}".format(os.getcwd() + "/bin"))

session.summary()
#