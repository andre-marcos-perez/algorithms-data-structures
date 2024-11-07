# Algorithms & Data Structures

> Repository to practice the implementation of algorithms and data structures 

## Setup

### Python

The project is a Python application. The dependencies are listed on the 
[requirements](requirements.txt) file. Install them using the following command:

> **Note**: It is highly recommended working with any Python virtual environment. We 
> recommend the built-in `venv` module.

```shell
pip3 install -r requirements.txt
```

### Git hooks

The project uses pre-commit hooks to ensure code quality (code format, linter, etc.). 
Install them using the following command:

```shell
chmod +x bin/install-git-hooks.sh
./bin/install-git-hooks.sh
```