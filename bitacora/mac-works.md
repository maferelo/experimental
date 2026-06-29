
We started installing some tools to make our development environment more efficient and user-friendly. Here are the tools we installed:

- Docker
- Bash prompt (starship) remember to add the line to your .zshrc or .bashrc file
    eval "$(starship init zsh)"
- Ollama

with this site 

https://www.canirun.ai/

we found that llama3.1:8b and qwen3.5:9b
and a couple more the mlx variant for example

can be run on the m1

with ollama interface in the mac app we can download the models and a couple more 

the idea is to test them to see if they work or do something and see how different from the paid one claude from adsk

installed devcontainer extension

install node nvm

https://nodejs.org/en/download

when installing npm packages

npm approve-scripts --allow-scripts-pending    
npm approve-scripts --all

brew install awscli

also create iam user with credentials to the cli

aws configure

if you get an error The image manifest, config or layer media type for the source image [...] is not supported then please go to Docker Desktop -> Settings -> General and make sure that "Use containerd for pulling and storing images checkbox" is NOT checked. Thank you Muhammad T. for this pro tip..

uv python package manager

curl -LsSf https://astral.sh/uv/install.sh | sh
