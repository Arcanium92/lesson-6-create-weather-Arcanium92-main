# CSC160_L6_Create <br>
You have been tasked with creating a Python program that tells the user the weather baseed on the zip code they enter. But first, a few quick notes: <br>
-Your assignment should be completed in Visual Studio on your machine, not in GitHub. <br>
-You will only be using GitHub to get the URL for your repository. That is the URL in the address bar right now! <br>

To begin the assignment, open the Create6.py file in IDLE. <br>
For an example output, open the ExampleOutput.txt file <br>

## Program Descriptions <br>
-The user is welcomed to the program and asked to input the Zip code they would like to view the weather for. <br>
-If the user puts in a string that is not a valid zip code, the program should prompt them to try again. (Just check that the user has entered a string of five integers. It does not have to be an acutal zip code.) <br>
Once the user submits their Zip code the program should display the weather information in an organized format. <br>
Finally, the program should ask them if they are done, or would like to view weather for a different area. If the user is done the program may terminate, otherwise the program should repeat. <br>

## Program Requirements
-This program must be organized into functions. Two of them have been provided for you, but you must create an additional function that checks the zip code the user inputs to verify its validity. <br>
-The two functions that are already defined for you should be finished with a combination of the provided components and your own code. <br>
-Your program must pull live weather data from the Open Weather api. To do this you will need your API Key from openweathermap.org. If you have not already, go to the website and create an account. You will find your API key in your account. <br>
**-You should not hard code in your api key when uploading to github. It is fine to hard code while testing, but when you submit you should update your program so that the user can paste in their API key before they enter their zip code.**<br>
-The user should only have to enter an API key once each time they start the program, even if they are viewing weather for multiple areas.<br>
-Your main program should only get the API key from the user and call functions. All other process should be placed into functions that are called by the main program. The main program should be 11 lines at most. <br>

## Tips
-You should not edit the code in either of the components that you have been provided. <br>
-The two functions that have been defined should not have their parameters altered. You should build the rest of your program in a way that allows you to pass the appropriate arguments to the functions when called. <br>
-This assignment builds on almost everything we have covered so far. Take it slow and focus on getting one piece functioning at a time. You've got this! <br>
