![Screenshot from 2023-04-01 17-56-43](https://user-images.githubusercontent.com/47550032/229301599-92db89e7-7ef7-4fd7-9da5-a74e5aa009f9.png)

# Description
Simple tkinter based desktop app to concat (without any duplication) every csv file in the selected folde. The merged csv will be compared with the list of contacted sites and the visited urls will be deleted from the csv database
  
# Usage
* Open a terminal in the project and start the application with the merger.py file
* Add the following details in the application
    * ***Csvs Path*** - *The folder which contains your csv files*
    * ***Domain Header*** - *The column name of the URL's column name in the csvs*
    * ***DR Header*** - *The column name of the Domain Rating's cloumn name in the csvs*
    * ***Contacted Sites*** - *Excel sheet with the urls of the contacted sites*
    * ***Output Filename*** - *The name of the output file (without extensions)*
    * ***Output Path*** - *The path of the output file*

* Click to **Get my list!** button and check your merged and refactored csv file in the output folder


# System requirements
* Python 3.7 or greater is installed on the machine
* Tkinter library is available. If not do the following:
  * Windows: Open a terminal and execute, **python -m pip install tkinter**
  * Linux (Ubuntu): Open a terminal and execute, **sudo apt-get install python3-tk**
* Other requirements are installed to your computer. Execute the following command from the main folder of the script:
  * Windows: Open a terminal and execute, **python -m pip install -r requirements.txt**
  * Linux (Ubuntu): Open a terminal and execute, **python3 -m pip install -r requirements.txt**
 
