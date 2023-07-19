## Setting up the Development Environment
### Installing poetry
To install poetry, execute the following command based on your operating system:
mac, linex, windows(bash)
```
curl -sSL https://install.python-poetry.org | python3 -
```
### Starting the Virtual Environment
Navigate to the "api" directory:
```
cd api
```
Set up the virtual environment:
```
poetry install
```
Activate the virtual environment
```
poetry shell
```
### Adding Libraries with poetry

To add a new package/library, use the following command:
```
poetry run <package> 
```
After adding or modifying packages, update the tock file:
```
poetry lock
```

## start API

set Yutube API Key
```zsh
export DEVELOPER_KEY="API_KEY"
```
start the server
```zsh
uvicorn main:app --reload
```
After starting the API, please access the following URL.\
http://127.0.0.1:8000/docs


### Note: If there are any additional corrections needed, please let me know, and I'll be glad to make the changes!