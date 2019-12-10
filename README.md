# anagram-lambda

## Installation
* Clone repo
* Install and configure aws-cli
* Install terraform > 0.12
* Run `deploy.sh`

## Usage
```bash
$ python3 main.py lead
(['dale', 'deal', 'lade', 'leda'], '0.04341745376586914s')
```

## Lambda
```bash
curl <LAMBDA-URL> -X POST -H "application/x-www-form-urlencoded" -d '{"word":"lead"}' -H "x-api-key: <API-KEY>"
```

## Unit test
```bash
$ python3 -m unittest test.py
```
