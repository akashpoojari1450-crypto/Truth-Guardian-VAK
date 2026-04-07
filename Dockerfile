FROM python:3.10

# Set up user permissions
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONPATH=$HOME/app

WORKDIR $HOME/app

# Install dependencies first (for faster builds)
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy all code
COPY --chown=user . .

# 🔱 CRITICAL FIX: Ensure the server folder is readable and executable
RUN chmod -R 755 $HOME/app/server

# Match the entry point to your folder structure
# We use 'server.app:app' because app.py is INSIDE the server folder
CMD ["python3", "-m", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
