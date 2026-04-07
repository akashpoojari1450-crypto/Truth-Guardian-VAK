FROM python:3.10

# 1. Set up user permissions
RUN useradd -m -u 1000 user
USER user

# 2. THE FIX: Explicitly set PYTHONPATH so it can find 'models.py' and 'server' folder
# ... (rest of your Dockerfile) ...

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONPATH=/home/user/app \
    PYTHONUNBUFFERED=1

WORKDIR $HOME/app
# ... (rest of your Dockerfile) ...
# 3. Install dependencies
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# 4. Copy all project files
COPY --chown=user . .

# 5. Final Launch Command
# Points to 'app' object inside 'server/app.py'
CMD ["python3", "-m", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
