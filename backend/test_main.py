from fastapi import FastAPI
from fastapi.testclient import TestClient
from requests.models import encode_multipart_formdata


from main import app

import hashlib


client = TestClient(app)
TOKENDATA=None
USERNAME = "testdesu"
PASSWORD = "password"
HASSEDPASS=hashlib.sha256(PASSWORD.encode()).hexdigest()
MAILADDRESS = "test@test.test"
EDITOR = True


def test_create_user_200():

  response=client.post(
    "/users",
    json={"username": USERNAME,"password": PASSWORD,"mailaddress": MAILADDRESS,"editor": EDITOR}
  )

  assert response.status_code==200
  assert response.json()=={
    "userid": 1,
    "username": USERNAME,
    "password": HASSEDPASS,
    "mailaddress": MAILADDRESS,
    "editor": EDITOR
  }

def test_create_user_false():
  response=client.post(
    "/users",
    json={"username": USERNAME,"password": PASSWORD,"mailaddress": MAILADDRESS,"editor": EDITOR}
  )
  assert response.status_code==200
  assert response.json()=={"status":False}

def test_create_user_luck_name():
  response=client.post(
    "/users",
    json={"password": PASSWORD,"mailaddress": MAILADDRESS,"editor": EDITOR}
  )
  assert response.status_code==422

def test_get_token_200():
  (content, header) = encode_multipart_formdata([('username', USERNAME),('password',PASSWORD)])
  response = client.post(
    '/token',
    headers={'Content-Type': header},
    data=content)

  assert response.status_code==200

def test_get_users_me():
  (content, header) = encode_multipart_formdata([('username', USERNAME),('password',PASSWORD)])
  accesstoken = client.post(
    '/token',
    headers={'Content-Type': header},
    data=content).json()["access_token"]
  response=client.get(
    '/users/me',
    headers={"Authorization": "Bearer "+accesstoken}
  )
  assert response.status_code==200
  assert response.json()=={
    "userid": 1,
    "username": USERNAME,
    "password": HASSEDPASS,
    "mailaddress": MAILADDRESS,
    "editor": EDITOR
    }


