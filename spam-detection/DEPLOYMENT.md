# 🚀 Deployment Guide

This guide covers deploying the Spam Detection Flask app to Vercel and alternative platforms.

## 📋 Prerequisites

- GitHub repository with your code pushed
- Account on the deployment platform (Vercel, Render, etc.)

---

## 🟢 Option 1: Deploy to Vercel (Free)

**Note:** Vercel can deploy Flask apps, but has some limitations with Flask sessions. If you need full session support, consider Render (Option 2).

### Steps:

1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Add improved UI and deployment config"
   git push origin main
   ```

2. **Go to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Sign up/Login with GitHub

3. **Import Project**
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect the Python/Flask setup

4. **Configure Build Settings**
   - **Framework Preset:** Other
   - **Root Directory:** `spam-detection` (or leave blank if root)
   - **Build Command:** (leave empty - Vercel handles it)
   - **Output Directory:** (leave empty)
   - **Install Command:** `pip install -r requirements.txt`

5. **Environment Variables** (if needed)
   - Add `FLASK_APP=app.py` (though vercel.json should handle this)

6. **Deploy!**
   - Click "Deploy"
   - Wait for build to complete
   - Your app will be live at `your-project.vercel.app`

### Important Notes for Vercel:
- ⚠️ **Flask sessions** may not work perfectly on Vercel's serverless functions
- The app will work, but session history might reset between requests
- Consider using client-side storage (localStorage) as an alternative

---

## 🔵 Option 2: Deploy to Render (Free - Recommended for Flask)

**Render is better suited for Flask apps with full session support.**

### Steps:

1. **Push your code to GitHub** (if not already done)

2. **Go to Render**
   - Visit [render.com](https://render.com)
   - Sign up/Login with GitHub

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

4. **Configure Service**
   - **Name:** spam-detection (or your choice)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py` (or `gunicorn app:app` for production)
   - **Plan:** Free (768 MB RAM)

5. **Environment Variables** (optional)
   - Add `FLASK_ENV=production`
   - Add `FLASK_APP=app.py`

6. **Deploy!**
   - Click "Create Web Service"
   - Render will build and deploy your app
   - Your app will be live at `your-project.onrender.com`

### Render Advantages:
- ✅ Full Flask session support
- ✅ Persistent storage
- ✅ Better for Python/Flask apps
- ✅ Free tier available

---

## 🟡 Option 3: Deploy to Railway (Free Trial)

1. Visit [railway.app](https://railway.app)
2. Sign up with GitHub
3. Create new project → Deploy from GitHub repo
4. Railway auto-detects Python and deploys

---

## 🔧 Production Improvements (Before Deploying)

For better production deployment, consider:

1. **Update secret key** in `app.py`:
   ```python
   import os
   app.secret_key = os.environ.get('SECRET_KEY', 'generate-a-random-key-here')
   ```

2. **Use Gunicorn** (for Render/Railway):
   ```bash
   pip install gunicorn
   ```
   Update Procfile:
   ```
   web: gunicorn app:app --bind 0.0.0.0:$PORT
   ```

3. **Add error handling** for production

---

## 📝 Files Created for Deployment

- `vercel.json` - Vercel configuration
- `Procfile` - For Render/Railway deployment
- `.gitignore` - Updated to exclude unnecessary files

---

## ✅ Quick Checklist

- [ ] Code pushed to GitHub
- [ ] Model files (.pkl) are included in repository
- [ ] requirements.txt is up to date
- [ ] Tested locally before deploying
- [ ] Updated secret key for production (if needed)

---

## 🐛 Troubleshooting

### Vercel Issues:
- If deployment fails, check build logs in Vercel dashboard
- Ensure all dependencies are in `requirements.txt`
- Model files must be in the repository

### Render Issues:
- Check build logs in Render dashboard
- Ensure Procfile is correct
- Verify Python version compatibility

---

**Need help?** Check the platform documentation or open an issue on GitHub.
