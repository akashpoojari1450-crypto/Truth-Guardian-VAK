FROM python:3.10

# Set up user permissions (prevents the 'root' error)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# Install dependencies
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy app code
COPY --chown=user . .

# IMPORTANT: Launch directly using python
CMD ["python3", "-m", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
