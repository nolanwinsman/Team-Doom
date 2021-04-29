This project consists of three main files

Doom.py

Load_In_Data.py

graph-data.py

test.py

graph-data.py depends on a lot having completed 

If you just want to see a demonstration of the code

the scenario can be changed in the load_in_data.py default_data class. This is where most variables are changed. 
Towards the bottom is the skip_learning and skip_evaluation booleans. Both of these cannot be the same value. 

For a user attempting to do learning for the first time, they need to run doom.py with skip_learning False and
skip_evaluation True. The num loops variable towards the top is the number of training cycles that will be completed.
After training is complete the user needs to rename the folders of the pth files so they're the same number at the end of each folder

Then swap the booleans and make sure the variables in load_in_data.py point to the correct folders and pth files.
