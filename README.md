## Tempora 

This repository contains the source for a website of Tempora publishing house. 

### Prerequisites

To run the website you have to install anaconda/miniconda and set up virtual environment: https://conda.io/docs/install/quick.html 

### Configuring 

0. Set up virtual environment: `conda create --name virtenv python=3.5`
1. Activate virtual environment: `source activate virtenv`
2. Install requirements: `pip install -r requirements`
3. Migrate user models first `python manage.py migrate users`
> make sure than you've created a migration for the userprofile app as soon as you may endup with annoying errors due to the conflict with default django auth models. 
4. Make db migrations and migrate: `python manage.py makemigrations` and `python manage.py migrate`
5. Load default user groups: `python manage.py loaddata users/fixtures/usergroups.json`
6. Configure translations for existing languages. For example: `python manage.py compilemessages -l en`

