#! /usr/bin/env zsh
export FLASK_APP=recycleML 
export FLASK_ENV=development
if [ -d "venv" ]; then
    source venv/bin/activate
    echo $'\nSourced Virtual Environment!\n'
else
    python3 -m venv venv
    source venv/bin/activate
    echo $'\nCreated & Sourced Virtual Environment!\n'
fi
cd ~/HackPHS/recycleML 
if [ -d "instance" ]; then
    echo $'\ndatabase is a-ok\n'
else
    flask init-db
fi
flask run
