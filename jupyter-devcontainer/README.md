# Jupyter Dev Container

A Docker Compose + VS Code Dev Container setup for running Jupyter notebooks (`.ipynb`).

## Contents

- `docker-compose.yml` — defines the `jupyter` service.
- `Dockerfile` — Python 3.12 image with JupyterLab and common data libraries.
- `requirements.txt` — pinned Python dependencies.
- `.devcontainer/devcontainer.json` — VS Code Dev Container config (Python + Jupyter extensions).
- `notebooks/example.ipynb` — sample notebook to verify the environment.

## Option A: Open in VS Code Dev Container (recommended)

1. Install the **Dev Containers** extension (`ms-vscode-remote.remote-containers`).
2. Open this folder in VS Code.
3. Run **Dev Containers: Reopen in Container** from the command palette.
4. Open `notebooks/example.ipynb` and run the cells. Select the `/usr/local/bin/python` kernel if prompted.

The dev container keeps the container alive (`sleep infinity`) so you can run notebooks directly inside VS Code.

## Option B: Run JupyterLab in the browser

```bash
docker compose build
docker compose run --rm --service-ports jupyter \
  jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=''
```

Then open http://localhost:8888 in your browser.

> Note: the `--NotebookApp.token=''` flag disables auth for local convenience only. Do not expose this port publicly.

## Customizing dependencies

Add packages to `requirements.txt`, then rebuild:

```bash
docker compose build
```
