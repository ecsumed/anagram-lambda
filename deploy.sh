#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

# pull latest code
git pull origin master

# remove old function.zip and create a new one
rm function.zip
zip function.zip main.py words.txt


rm terraform/function.zip
cp function.zip terraform/function.zip

terraform apply terraform/main.tf
