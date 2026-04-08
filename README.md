---
title: Truth Guardian VAK
emoji: 🔱
colorFrom: blue
colorTo: red
sdk: docker
app_port: 7860
pinned: false
tags:
  - openenv
  - pytorch
---

# 🔱 Truth Guardian (VAK-∞)
### Team Vakratunda | SIT Valachil Node

A scam detection and OTP verification system for the Meta PyTorch OpenEnv Hackathon.

## Features
- OTP Verification with Bank HQ Simulation
- Behavioral DNA Scanning
- Scam Detection via Keyword Heuristics
- FastAPI Endpoints for OpenEnv
- Gradio UI Interface

## API Endpoints
- `/reset` - Reset environment
- `/step` - Step execution  
- `/health` - Health check
- `/` - API status

## Local Development
```bash
pip install -r requirements.txt
python app.py
```
