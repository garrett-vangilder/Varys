# Varys
_Varys is intended for research purposes exclusively._

## Who is Varys?
Varys is the [master of whisperers](https://iceandfire.fandom.com/wiki/Varys). He is known for his league of little birds who keep their ears to the ground and are capable of learning secrets that are not intended for the public. 

## What is Varys/this tool? 
This tool can be used to query for personal identifying information (or other formatted data) from a publicly accessible website. The only thing Varys needs is a regex and a domain.

## Installation

### Prerequisites for MacOS
```bash
# Install brew, this will be used for OS level package management https://brew.sh/
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install python
brew install python

# Install poetry https://python-poetry.org/docs/
curl -sSL https://install.python-poetry.org | python3 -

# run command w/ poetry
poetry run python main.py --domain=$domain --regex=$regex --route_list='./config/default.txt' --verbose
```
## How to


### Basic Usage
```bash
# url regex
https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)

## Example call 
poetry run python main.py --domain=$domain --regex='https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'

# phone number regex
\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*

## Example call 
poetry run python main.py --domain=$domain --regex='\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*'

```

### Commonly used regexs

This is not a definitive list, however a good place to start when looking around.

```bash
# URL regex
https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)

## Example call 
poetry run python main.py --domain=$domain --regex='https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'

# Phone number regex
\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*

## Example call 
poetry run python main.py --domain=$domain --regex='\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*'

# Email address regex
[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+

## Example call
poetry run python main.py --domain=$domain --regex='[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+'
```

