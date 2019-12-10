#! /bin/bash

zipfile="function.zip"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

# pull latest code
git pull origin master

# remove old function.zip and create a new one
if [ -f ${zipfile} ]; then rm $zipfile ; fi
zip ${zipfile} main.py words.txt

if [ -f "terraform/${zipfile}" ]; then rm "terraform/${zipfile}" ; fi
cp ${zipfile} terraform/${zipfile}

cd terraform
terraform init
terraform apply -input=false -auto-approve
