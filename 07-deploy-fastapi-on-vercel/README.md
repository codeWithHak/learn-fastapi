# FastAPI Vercel Deployment Starter

Quick guide to deploy FastAPI apps on Vercel.

## Setup

1. Create `vercel.json` file
2. Create `requirements.txt` file
3. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

## Deploy

**First time:**
```bash
vercel login
vercel .
```

**Production:**
```bash
vercel --prod
```

**Redeploy:**
```bash
vercel
```