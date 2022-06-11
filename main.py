from UnsplashApi import Connect, os

term = str(input("Please enter a search term.\n"))

# Connection
session = Connect(term)

# Data Response, Setting Variables & Error catching if out of credits for api calls
session.start()


# Logic to return maxiumum of 3 images randomly from results
session.filter_results()

# Create Save Folder or Ignores if it already exists
session.save_path()

# Download logic + Naming file with numeric ascending numbers
session.download_images(session.filtered_list)


# Opens folder where download jpegs are
os.system("cmd /c start {}".format(os.getcwd() + "/DownloadFolder"))

# Prints total images returned from Search & remaining Api Calls for the hour
session.summary()