# Setup and code guidelines

## Oracle VM instance setup

1. Create an instance on [Oracle Cloud](https://cloud.oracle.com/compute/instances/create).

2. Follow the [instrucions](https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/testingconnection.htm) to use the ssh key.

```bash
# Assing read-only permissions to the private key
chmod 400 <private_key_file>

# Connect to the VM
ssh -i <private_key_file> opc@<public_ip>
```

3. Enable internet access to the VM

Follow the [instructions](https://docs.oracle.com/en-us/iaas/developer-tutorials/tutorials/flask-on-ubuntu/01oci-ubuntu-flask-summary.htm) to configure iptables.

If using docker, forward the ports on your compose

```yaml
...
ports:
  - "0.0.0.0:80:80"
```

## Better bash prompt

Install [oh-my-bash](https://github.com/ohmybash/oh-my-bash) using:

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
```

## Install Docker on ubuntu

Please follow the [official instructions](https://docs.docker.com/engine/install/ubuntu/).

Check if the installation was successful:

```bash
systemctl status docker
```