# Youtube-CSV-Data
Python scripts that retrieve a specific channel's data using Youtube Data API v3 and converts into a CSV file to be used for data science or ML-related tasks.


1- Make sure all the libraries (BS4, Pandas, etc.) are installed

2- Run the vidlinks.py file in the terminal. (python vidlinks.py)

This file grabs at most 30 videos links (still figuring out how to get scrape more) and saves it in a .csv file to be used later by the videodata.py file.
-A link of the channel has to be assigned to "channels".
-Then, you write the name you want for the .csv file that'll be created.

3- Before running the second script, edit the DEVELOPER_KEY and type yours which could be found in the Developer Console.

4- Edit the "df" variable (LINE 87) to the same file that was generated after you ran vidlinks.py because it's what'll be read and used by the API to get the data.

5- Type a new file name (LINE 101)

6- Then, you run the videodata.py file just like before.`
