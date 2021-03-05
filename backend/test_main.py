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

def _get_access_token(tester)->str:
  username = USER[tester]['input']['username']
  password = USER[tester]['input']['password']

  (content, header) = encode_multipart_formdata([('username', username),('password',password)])
  access_token = client.post(
    '/token',
    headers={'Content-Type': header},
    data=content).json()['access_token']

  return access_token
  

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
    accesstoken=_get_access_token(tester)
    response=client.get(
      '/users/me',
      headers={'Authorization': 'Bearer '+accesstoken}
    )

    assert response.status_code==200
    assert response.json()==USER[tester]['output']

def test_update_me():
  testers = ['editor','not editor']
  for tester in testers:
    accesstoken=_get_access_token(tester)
    response=client.put(
      '/users/me',
      headers={'Authorization': 'Bearer '+accesstoken},
      json = {'mailaddress':'kirryx@gmail.com'}
    )

    output = USER[tester]['output'].copy()
    output["mailaddress"]='kirryx@gmail.com'

    assert response.json()['item']==output

def test_create_character_me():
  characters={
    "editor":{
      "input":{
        "department":"edit",
        "position": "editor",
        "skills": ["editor","QC"]
      },
      "output": {
        "id":1,
        "username": "editor",
        "department":"edit",
        "position": "editor",
        "skills": ["editor"]
      }
    },
    "not editor":{
      "input":{
        "department":"not edit",
        "position": "not editor",
        "skills": ["not editor"]
      },
      "output": {
        "id":2,
        "username": "not editor",
        "department":"not edit",
        "position": "not editor",
        "skills": ["not editor"]
      }
      
    }
  }
  testers = ["editor", "not editor"]
  for tester in testers:
    accesstoken=_get_access_token(tester)
    response=client.post(
      '/characters',
      headers={'Authorization': 'Bearer '+accesstoken},
      json = characters[tester]["input"]
    )

    assert response.status_code==200
    assert response.json()==characters[tester]["output"]



