# Scrape and trade

## Using WSL

### [Initial setup](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)

### [Setup GIT](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git)

### [Bash Prompt](https://github.com/ohmybash/oh-my-bash)

## Setup python env

### [Pyenv](https://github.com/pyenv/pyenv)

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

```bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Create virtualenv

```bash
pyenv install
python -m venv venv
source venv/bin/activate
pip install
```

## Run on startup

```bash
sudo crontab -e
```

```bash
@reboot /home/dharma/develop/experimental/python/scrape/venv/bin/python /home/dharma/develop/experimental/python/scrape/scrape.py 
```