Floaty - potato - frontend
When everyone is working, everyone is working on branches. Not the MASTER.
When you finish work and request pull request into master.
Pull request needs to be reviewed by a team member.
It will be approved by a team member.
Once it is approved, it will be merged into master.
RULES
Noone is allowed to push directly into master.
Noone is working on the master.
3 Branches (Feature, Development and Master) Work in Feature and push to Development once approved. Confirm Development is working and Push to Master once approved.

TO GET STARTED:
1 - INSTALL REQURIEMENTS
pip install -r requirements.txt
2 - MIGRATE DATABASE
./manage.py migrate
3 - CREATE SUPERUSER
./manage.py createsuperuser
4 - LOAD DATA FIXTURES
type the following command into your terminal
./manage.py loaddata movies.json
5 - RUN THE SERVER
./manage.py

You can then see an example of the API endpoints at:
localhost:8000/api/movies/
localhost:8000/api/providers/
localhost:8000/api/genres/
localhost:8000/api/classifications/

HAVE FUN!
