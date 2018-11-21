#!/bin/bash

export VENV='/home/mike/workspace/venv'

# Web Server Commands
alias npmrun='npm run dev'
alias webstart='python manage.py runserver'

# Django Database Migration Commands
alias makemigrations='python manage.py makemigrations'
alias migrate='python manage.py migrate'
alias showmigrations='python manage.py showmigrations'

# Database
alias enterdb='sudo -i -u postgres'
alias xmcp2db='sudo -i -u postgres psql -d xmcp2'

# Log Directory
export LOG_DIR='/home/mike/workspace/xMCp2/logs'

source $VENV/bin/activate
