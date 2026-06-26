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


