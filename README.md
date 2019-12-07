# anagram-lambda

## Usage
```bash
$ python3 main.py lead
(['dale', 'deal', 'lade', 'leda'], '0.04341745376586914s')
```

## Lambda usage
```bash
curl <LAMBDA-URL> -X POST -H "Content-Type: application/json" -d '{"word":"dog"}'
```

## Unit test
```bash
$ python3 -m unittest test.py
```
