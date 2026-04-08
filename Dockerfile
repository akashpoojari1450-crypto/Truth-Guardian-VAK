FROM python:3.10
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONPATH=$HOME/app \
    PYTHONUNBUFFERED=1

WORKDIR $HOME/app
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt
COPY --chown=user . .

# Launch the app from the root
CMD ["python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
