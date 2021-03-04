from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app

import hashlib

client = TestClient(app)
TOKENDATA={"access_token":"","token_type":""}
USERNAME = "test5"
PASSWORD = "password"
MAILADDRESS = "test@test.test"
EDITOR = True


def test_create_user():

  response=client.post(
    "/users",
    json={"username": USERNAME,"password": PASSWORD,"mailaddress": MAILADDRESS,"editor": EDITOR}
  )

  assert response.status_code==200
  assert response.json()=={
    "userid": 13,
    "username": USERNAME,
    "password": hashlib.sha256(PASSWORD.encode()).hexdigest(),
    "mailaddress": MAILADDRESS,
    "editor": EDITOR
  }