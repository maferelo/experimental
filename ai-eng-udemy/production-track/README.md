course link 

https://globant.udemy.com/course/generative-and-agentic-ai-in-production/learn/lecture/52441929#overview

course name 

AI Engineer Production Track: Deploy LLMs & Agents at Scale

# Week 1

# Day 1

sign up in vercel
https://vercel.com/dharma7/instant/Excf1Bd5V78p4GmbyRDKeW4ewHzk
https://vercel.com/new
created app .py
create vercel.json
create requirements.txt


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def instant():
    return "Live from production!"
```

install node
install vercel

```bash
npm install -g vercel
```

login vercel

```bash
vercel login
```

deploy vercel

```bash
vercel .
```

https://instant-ihzctfh1b-dharma7.vercel.app

add env var to vercel OPENAI_API_KEY
deploy vercel

# Day 2

npx create-next-app saas --ts --eslint --tailwind --no-src-dir --no-app

removed api folder

added pages folder with index.tsx and _app.tsx

added api folder with fastapi in index.py

added requirements.txt with fastapi and uvicorn and openai

modify views

vercel link

vercel env add OPENAI_API_KEY

vercel .

vercel --prod

## Day 2 Add real time streaming

add deps and modify api and pages

this to improve the styling and to make it more professional

## Day 3 Auth and Payments

added auth with clerk and even payments, can be switched to stripe anytime

## Day 4 Healthcare App

transform into healthcare app

npm install react-datepicker
npm install --save-dev @types/react-datepicker

## Day 5 AWS deployment

Change a bit how the folder structure works so we can create a docker image and deploy it to AWS

create normal account in AWS and create a new IAM user with programmatic access and attach the AdministratorAccess and a couple of other policies to it

ECR (Elastic Container Registry) is where we'll store our Docker image.

configure aws cli with the IAM user credentials

and push the docker image to ECR

create lamda function with the docker image and create an API Gateway to expose it

# Week 2

# Day 1

so basically it's a model that stores previous conversations(memory) and feeds them to the LLM so it can have a more coherent conversation with the user or per se remember the user and the context of the conversation

http://twin-frontend-8t3bvu0.s3-website-us-east-1.amazonaws.com

http://twin-frontend-8t3bvu0.s3-website-us-east-1.amazonaws.com/

https://6cmlyvtdze.execute-api.us-east-1.amazonaws.com/health
https://dvcmnka4ippha.cloudfront.net

# Day 4

# Destroy dev environment
./scripts/destroy.sh dev

# Destroy test environment
./scripts/destroy.sh test

# Destroy prod environment
./scripts/destroy.sh prod

to delete workspace

terraform workspace select default
terraform workspace delete dev  # or test, prod

we are missing the prod setup but that would require a custom domain so better later