# Inventory Management REST API

A simple RESTful inventory management service built using FastAPI.

## Features

- Add new products
- View all products
- Retrieve product by ID
- Update product details
- Delete product
- Input validation using Pydantic
- Automatic API documentation via Swagger

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Run Locally

```bash
git clone <your_repo_url>
cd inventory-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

Visit http://127.0.0.1:8000/docs
