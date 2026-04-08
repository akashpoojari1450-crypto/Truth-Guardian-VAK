FROM python:3.10

# Set up user
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONPATH=/home/user/app \
    PYTHONUNBUFFERED=1

WORKDIR $HOME/app

# Install dependencies
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy all files
COPY --chown=user . .

# 🔱 THE CRITICAL FIX: Explicitly call the app from the root
CMD ["python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
