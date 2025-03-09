# Software-Developer-Intern-Topo---Technical-Assessment
This is my submission for the software developer internship for topo. This README file will serve as a means for sharing my reflections as well as user guide for this project.
It will be split into 4 parts:
1. Overview
2. Setup instruction/ User guide
3. Testing instruction
4. Challenges and Assumptions

### Overview
* I first wrote out 4 parsers in python (a quick and simple language), one for each file
* Following the parsers, i wrote the test cases `test_parser.py` for the parsers
* Next, I spend some time going through the data parsed and designed the data model that I wil be using to store and unify them all, I also took this opportunity to plan on how I want to showcase the data in graphical format
* I then wrote the API using flask and its respective test cases
* Lastly I wrote a simple React-ts app to take in the data from the backend and showcase it graphically
* I then spend my last few hours on simple formatting of the frontend, css as well as componentizing some files to make them easier to follow.

![img](https://github.com/lyhthaddeus/Software-Developer-Intern-Topo---Technical-Assessment/blob/main/docs/AppFrontend.png)


### Setup Instruction / User guide
1. Fork and clone the repo to your device from [here](https://github.com/lyhthaddeus/Software-Developer-Intern-Topo---Technical-Assessment)
2. cd into the backend directory
3. run `pip install -r requirement.txt` to download all the library required
4. run `py app.py`
5. In a seperate terminal, cd to the frontend directory
6. run `npm install` to download all dependencies
7. run `npm start` to run the app
8. A window should open in localhost that would allow you to view the app.

> [!Warning]
> Due to the Time constraint of this assessment, I did not have time to smoke test the app on other os, thus I cannot be 100% gurantee that it will work as intended
> The app was written in and intended to run on Windows 11.

### Testing instruction
1. To test, cd to the backend
2. In the root directory of backend (`/backend/`) there will be the test file for the api (`test_api.py`)
3. run `py -m unittest test_api.py` to run unit testing on the api
4. cd to `backend/ingest/`
5. run `py -m unittest test_parser.py` to test the parsers

> [!Note]
> I was unsure on how to create dummy pdf files for unit testing of pdf parser, and thus it was not included.

### Assumptions and Challenges
#### Assumptions
The data given was in a mess, with some data not having a label on what exactly they are showing. An example of this
was the pdf file provided which just showed performance data without letting me
know which company membership data this belongs too. <br>
Only after doing some calculation from the pptx that I found the Total revenue for 2023 adds up to $10,400,000 on both ends.
Which points as a clue that they are both referring to the same company. <br>
<br>
However, the csv file was not as explicit in which company it belongs to, thus an assumption made that the data was for "FitPro" as
majority of the other data refered to that company as well<br>
<br>
Another assunmption made was that the data from the pptx are all derivatives from the csv/ pdf files. The assumption made was that this project
was meant to consolidate all the data for future proofing. Thus derivative data (such as 'total revenue' and 'average duration') was ommitted as
they can simply be calculated using the raw data.<br>
<br>
Following the previous assumption that the purpose of this excercise is to consolidate data into a centralised structure, I opted only to show some ways 
my json structure can be used to show simple relationships (like revenue against time, total revenue per location, etc) and didn't do any deeper data 
analysis on the dataset.<br>

#### Challenges
This is also my first time working with data from pdf and pptx. I am more used to csv and json from my other projects.
It was a slight learning curve having to learn the strtucture of pdf and pptx files and how to properly parse it.<br>
<br>
Understanding the task at hand given the messy data was also quite challenging. That resulted in me spending a lot more
time on the planning before I even sat down to code the app. Especially while this was during my exam period, I only had a few
days to properly code, unfortunately resulting in a rushed project and messy code. <br>

### Credits
* Color theme for frontend uses [catppuccin](https://catppuccin.com/)

### Json structure
```python
{
  "companies": [
    {
      "id": 1,
      "industry": "Sports and Leisure",
      "location": "North America",
      "name": "FitPro",
      "employees": [
        {
          "cashmoneh": 3500,
          "hired_date": "2020-01-15",
          "id": "E001",
          "name": "Alice",
          "role": "Personal Trainer"
        }
      ],
      
      "mebership_activity_data": [
        {
          "Activity": "Yoga Class",
          "Date": "2024-01-16",
          "Duration (Minutes)": "120",
          "Location": "Eastside",
          "Membership_ID": "M100",
          "Membership_Type": "Basic",
          "Revenue": "57.06"
        }
      ],
      "performance": {
        "2022_Q1": {
          "membershipsSold": 300,
          "revenue": 2100000
        }
      }
    },
    {
      "employees": [
        
        {
          "cashmoneh": 70000,
          "hired_date": "2023-04-15",
          "id": "E115",
          "name": "Quincy",
          "role": "Wellness Retreat Planner"
        }
      ],
      "id": 2,
      "industry": "Sports and Leisure",
      "location": "Europe",
      "name": "RecreaLife",
      "performance": {
        "2023_Q1": {
          "profit_margin": 10.0,
          "revenue": null
        },
        "2023_Q2": {
          "profit_margin": 11.5,
          "revenue": 22000000
        }
      }
    }]}
```
      


