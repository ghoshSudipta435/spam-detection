"""
Entry point for Vercel serverless deployment
This file is used by Vercel to run the Flask app as a serverless function
"""
from app import app

# Export the app for Vercel
handler = app
