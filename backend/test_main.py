from fastapi import FastAPI
from fastapi.testclient import TestClient
from requests.models import encode_multipart_formdata


from main import app

import hashlib


client = TestClient(app)
USER = {
  'editor':{
    'input':{
      'username': 'a',
      'password': 'a',
      'editor': True,
      'mailaddress': 'a'
    },
    'output':{
      'userid': 1,
      'username': 'a',
      'password': hashlib.sha256('a'.encode()).hexdigest(),
      'mailaddress': 'a',
      'editor': True
    }
  },
  'not editor':{
    'input':{
      'username': 'b',
      'password': 'b',
      'mailaddress': 'b',
      'editor': False
    },
    'output':{
      'userid': 2,
      'username': 'b',
      'password': hashlib.sha256('b'.encode()).hexdigest(),
      'mailaddress': 'b',
      'editor': False
    }
  }
}



def test_create_user_200():
  testers=['editor','not editor']
  for tester in testers:
    response=client.post(
      '/users',
      json=USER[tester]['input']
    )

    assert response.status_code==200
    assert response.json()==USER[tester]['output']



def test_create_user_doubled():
  response=client.post(
    '/users',
    json=USER['editor']['input']
  )
  assert response.status_code==200
  assert response.json()=={'status':False}

def test_create_user_luck_name():
  json = USER['editor']['input'].copy()
  json['username']=''
  response=client.post(
    '/users',
    json=json
  )

  assert response.status_code==200

def test_get_token_200():
  testers=['editor','not editor']
  for tester in testers:
    username = USER[tester]['input']['username']
    password = USER[tester]['input']['password']

    (content, header) = encode_multipart_formdata([('username', username),('password',password)])
    response = client.post(
      '/token',
      headers={'Content-Type': header},
      data=content)

    assert response.status_code==200

def test_get_users_me():
  testers = ['editor','not editor']
  for tester in testers:
    username=USER[tester]['input']['username']
    password=USER[tester]['input']['password']
    (content, header) = encode_multipart_formdata([('username', username),('password',password)])
    accesstoken = client.post(
      '/token',
      headers={'Content-Type': header},
      data=content).json()['access_token']
    response=client.get(
      '/users/me',
      headers={'Authorization': 'Bearer '+accesstoken}
    )

    assert response.status_code==200
    assert response.json()==USER[tester]['output']

