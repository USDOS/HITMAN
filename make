.PHONY: install test lint format docs clean

install:
    pip install -r requirements.txt
    pip install -e .[dev]

test:
    pytest tests/

lint:
    flake8
    black --check .

format:
    black .

docs:
    cd docs && make html

clean:
    rm -rf venv/
    rm -rf .pytest_cache/
    rm -rf .coverage
    rm -rf htmlcov/
    rm -rf dist/
    rm -rf build/
    rm -rf *.egg-info/
    rm -rf docs/_build/