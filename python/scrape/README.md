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
pip install -r requirements.txt
pip freeze >> requirements.txt
```

### Install as a service

```bash
cp scrape.service /etc/systemd/system
# Start on boot
sudo systemctl [enable|start|status|stop|restart] scrape.service
# Kill
sudo systemctl --user --signal=SIGKILL kill scrape.service

journalctl --follow -u scrape.service
```

## Run a basic webserver to check connections

```bash
docker run -it -d -p 80:80 --restart unless-stopped yeasy/simple-web:latest

# Check if the server is running
curl -v http://localhost
```

## Troubleshooting

- [Enable LAN connections on wsl to local network](https://github.com/microsoft/WSL/issues/4150)
- [Fix wsl LAN connections](https://askubuntu.com/questions/1347712/make-etc-resolv-conf-changes-permanent-in-wsl-2)
- [Enable systemctl in wsl](https://askubuntu.com/questions/1379425/system-has-not-been-booted-with-systemd-as-init-system-pid-1-cant-operate)

### Remove if other instances are running

```bash
ps aux | grpep python
sudo kill <id>
```


set +o noclobber


sudo wget https://github.com/electron/electron/releases/download/v33.0.2/chromedriver-v33.0.2-linux-x64.zip

https://patrikmojzis.medium.com/how-to-run-selenium-using-python-on-raspberry-pi-d3fe058f011




https://jwstanly.com/blog/article/Port+Forwarding+WSL+2+to+Your+LAN/






