HAVE FUN!

# Floaty - potato - frontend

Let make this API amazing folks!

## Git Rules

When everyone is working, everyone is working on branches. Not the MASTER.
When you finish work and request pull request into master.
Pull request needs to be reviewed by a team member.
It will be approved by a team member.
Once it is approved, it will be merged into master.
RULES
Noone is allowed to push directly into master.
Noone is working on the master.
3 Branches (Feature, Development and Master) Work in Feature and push to Development once approved. Confirm Development is working and Push to Master once approved.When everyone is working, everyone is working on branches. Not the MASTER.
When you finish work and request pull request into master.
Pull request needs to be reviewed by a team member.
It will be approved by a team member.
Once it is approved, it will be merged into master.
RULES
Noone is allowed to push directly into master.
Noone is working on the master.
3 Branches (Feature, Development and Master) Work in Feature and push to Development once approved. Confirm Development is working and Push to Master once approved.

## Getting started and what you need to do after pulling

TO GET STARTED:
1 - CREATE VIRTUAL ENVIRONMENT AND ACTIVATE IT
virtualenv env
source env/bin/activate
2 - INSTALL REQURIEMENTS
pip install -r requirements.txt
3 - MIGRATE DATABASE
./manage.py migrate
4 - CREATE SUPERUSER
./manage.py createsuperuser
5 - LOAD DATA FIXTURES
type the following command into your terminal
./manage.py loaddata movies.json
6 - RUN THE SERVER
./manage.py runserver

You can then see an example of the API endpoints at:
localhost:8000/api/movies/
localhost:8000/api/providers/
localhost:8000/api/genres/
localhost:8000/api/classifications/
