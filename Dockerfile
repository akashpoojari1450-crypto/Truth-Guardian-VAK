FROM python:3.10

WORKDIR /code

# Copy requirements first for faster building
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of your code (app.py, inference.py, etc.)
COPY . .

# Start the server on Port 8000
CMD ["python", "app.py"]
