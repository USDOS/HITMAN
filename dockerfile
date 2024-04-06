FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the project files
COPY . .

# Install dev dependencies
RUN pip install -e .[dev]

# Set up pre-commit hooks
RUN pre-commit install

# Run tests
RUN pytest tests/

# Build documentation
RUN cd docs && make html

# Expose Flower port
EXPOSE 5555

# Set the entry point
ENTRYPOINT ["python", "run.py"]