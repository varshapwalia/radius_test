# Radius
radius contains all url endpoints for application

## Setup Guide

1. `sudo pip install virtualenv`
2. `virtualenv venv`
3. `source venv/bin/activate`
4. `python app.py`

## How to use

1. Clone the whole project
2. Install the required packages
3. Follow setup instructions
4. Start creating your application
5. Change `.env` file according to the requirements

## .env
`export APP_SETTINGS="config.DevelopmentConfig"`

Note: Also install the required packages from requirements.txt

## Upgrade 
pip install -r requirements.txt --upgrade

## Structure

1. Controllers for APIs
2. Models for Database structuring
3. Scripts for custom jobs and intiating projects.
4. Workers for cron and queing based jobs
5. Staticd for files, Custom CSS an JS
6. Templates for Html pages.
7. Procfile and runtime.txt for server enviroment and deployent
8. requirements.txt keeps the track of required packages.

## Ways To Improve the Project

1. Saving results in database on query for history
2. Scheduling api calls to auto update the database with new issues
3. Tracking the bugs and fixes times-dates.
4. Scaling it for multi purpose git manager.
5. We can utilize it as a debugger platform data showcase as well.
6. Also not just numbers but the actual details of the issues.
7. Pagination system eating up so much time for server calls.

## Challanges Faced and Issues
1. Pagination system of git.
2. Was not able to reduce time on API call further.

## SAMPLE
https://github.com/facebook/react
{'24hrs_to_7days': 34, 'beyond_7days': 500, 'total': 540, 'within_24hrs': 6}
