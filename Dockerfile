# Keep your current Python version
FROM python:3.10

# 1. Create a non-root user (Hugging Face standard)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# 2. Set the working directory to the user's home
WORKDIR $HOME/app

# 3. Copy requirements and install as the 'user'
# This avoids the "Running as root" warning
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# 4. Copy the rest of your application code
COPY --chown=user . .

# 5. Run the app on the standard port
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
