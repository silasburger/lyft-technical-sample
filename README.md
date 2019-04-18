# Lyft Technical Sample


## Getting Started

note - you should have python3 installed

1. clone the repository

2. cd into root project directory and initialize virtual environment
```bash
  $ python3 -m venv venv
```

3. active the virtual environment
```bash
  $ source venv/bin/activate
```

3. install dependencies
```bash
  $ pip3 install -r requirements.txt
```

4. set envirment variable to dev and run flask
```bash
  $ FLASK_ENV=dev flask run
```

5. go to the url mentioned in command line

## Run Tests

1. cd into the root project directory and run the following command
```bash
  $ python3 -m unittest test.py
```