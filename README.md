# Redes2 BlockChain Communication

This project template is made using python 3.8.12-slim image and the following frameworks:
- FastAPI;
- Pydantic;

## Prerequisites

* Python 3.8 installed in your computer;
* Virtualenv installed; or
* Docker installed

## 💻 Steps

### To run with Docker:
* Clone this repository;
* Run the following command to build the image: `docker build -t redes2-bc-comm .`;
* Run the following command to run the image: `docker run -p 8080:8080 -e "BASE_URL=https://blockchain-uff.herokuapp.com" -t redes2-bc-comm -d --rm`

### To run locally in your machine:
* Clone this repository;
* Create a python virtual env with the following command: `virtualenv venv`
* Activate the virtualenv:
  * If you're running Windows: `.\venv\Scripts\activate`
  * If you're running Linux: `source venv/bin/activate`
* Create a .env file and add the following to it: `BASE_URL="https://blockchain-uff.herokuapp.com"`
* Install all the dependencies with: `pip install -r requirements.txt`
* Run the entrypoint with: `sh entrypoint.sh`

## After Installed
* You can check the endpoints, its payloads and authorizations in the following page: `http://localhost:8080/docs`

And thats all :)