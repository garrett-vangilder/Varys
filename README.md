# Varys
_Varys is intended for research purposes exclusively._

## Who is Varys?
Varys is the [master of whisperers](https://iceandfire.fandom.com/wiki/Varys). He is known for his league of little birds who keep their ears to the ground and are capable of learning secrets that are not intended for the public. 

## What is Varys/this tool? 
This tool can be used to query for personal identifying information (or other formatted data) from a publicly accessible website. The only thing Varys needs is a regex and a domain.

## Installation

### Prerequisites for MacOS

This project integrates with [Poetry](https://python-poetry.org/) for dependency management. It is possible to install
dependencies without poetry for this project, however we're suggesting poetry to provide a cleaner encapsulation for Varys'
virtual environment.

```bash
# Install brew, this will be used for OS level package management https://brew.sh/
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install python
brew install python

# [OPTIONAL] Install poetry https://python-poetry.org/docs/
curl -sSL https://install.python-poetry.org | python3 -

# [OPTIONAL] Configure your python virtual environment, I find that having the venv in the project directory to be useful
poetry config virtualenvs.in-project true 

# [OPTIONAL] Install dependencies
poetry install --no-root
```

## How to
Varys can be executed with a plethora of configurations 

| Arguments         | Short Flag | Long Flag     | Description                                      | Example                                          | Default Value        |
|:------------------|:-----------|:--------------|:-------------------------------------------------|:-------------------------------------------------|:---------------------|
| help              | -h         | --help        | Prints helper text associated with the program   |                                                  | off                  |
| domain (required) | -d         | --domain=     | Target domain for route enumeration and scraping | google.com                                       | N/A                  |
| regex (required)  | -r         | --regex=      | Target regex for scraping                        | [a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+ | N/A                  |
| route list        | -rl        | --route_list= | Dictionary of routes to enumerate/crawl          | ./path/to/txt/file                               | ./config/default.txt |
| verbose logging   | -v         | --verbose     | Will print info level logs to standard out       |                                                  | off                  |
| output directory  | -o         | --output=     | Target output directory for Varys payload (JSON) | /tmp/                                            | ./                   |
| insecure protocol | -i         | --insecure    | Flag to toggle insecure v. secure http protocol  |                                                  | off                  |



### Basic Usage
```bash
# Example call to query for domains, notice this will not print to stdout
poetry run python main.py --domain=$domain --regex='https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'

# Will print to stdout
poetry run python main.py --domain=$domain --regex='https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)' --verbose

# Will perform http request instead of https
poetry run python main.py --domain=$domain --regex='https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)' --insecure

# Will output findings to tmp directory
poetry run python main.py --domain=$domain --regex='https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)' --output='/tmp/'
```

### Commonly used regexs and use cases

This is not a definitive list, however a good place to start when looking around.

```bash
# URL regex
https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)

# Example call looking for URLs
poetry run python main.py --domain=$domain --regex='https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'

# Phone number regex
\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*

# Example call looking for phone numbers
poetry run python main.py --domain=$domain --regex='\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*'

# Email address regex
[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+

# Example call looking for email addresses
poetry run python main.py --domain=$domain --regex='[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+'

# Regex for Apache webservers
(?i)apache\/\d+\.\d+\.\d+

# Example call looking for Apache webservers
poetry run python main.py --domain=$domain --regex='(?i)apache\/\d+\.\d+\.\d+'

# Regex for Apache webservers
(?i)apache\/\d+\.\d+\.\d+

# Example call looking for Apache webservers
poetry run python main.py --domain=$domain --regex='(?i)apache\/\d+\.\d+\.\d+'

# Regex for nginx webservers
(?i)nginx.*$

# Example call looking for nginx webservers
poetry run python main.py --domain=$domain --regex='(?i)nginx.*$'
```

