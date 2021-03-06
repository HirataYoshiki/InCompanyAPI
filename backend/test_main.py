from fastapi import FastAPI
from fastapi.testclient import TestClient
from requests.models import encode_multipart_formdata


from main import app

import hashlib
from copy import deepcopy


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

CHARACTERS={
  "editor":{
    "input":{
      "department":"edit",
      "position": "editor",
      "skills": ["editor","QC"]
    },
    "output": {
      "id":1,
      "username": USER['editor']['input']['username'],
      "department":"edit",
      "position": "editor",
      "skills": ["editor","QC"]
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
      "username": USER['not editor']['input']['username'],
      "department":"not edit",
      "position": "not editor",
      "skills": ["not editor"]
    }
    
  }
}

REPORTS={
  'editor': {
    'input': {
      'title': 'editor_title'
    },
    'output': {
      'reportid': 1,
      'localreportid': 1,
      'username': USER['editor']['input']['username'],
      'title': 'editor_title',
      'contentsid': None,
      'timestamp': None,
      'teamid': None,
      'headerid': None
    }
  },
  'not editor': {
    'input': {
      'title': 'not_editor_title'
    },
    'output': {
      'reportid': 2,
      'localreportid': 1,
      'username': USER['not editor']['input']['username'],
      'title': 'not_editor_title',
      'contentsid': None,
      'timestamp': None,
      'teamid': None,
      'headerid': None
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
  response=client.post(
    '/users',
    json={"username":"","password": "fakepass"}
  )
  assert response.json()==None
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

def test_get_all_users():
  testers = ['editor','not editor']
  for tester in testers:
    accesstoken=_get_access_token(tester)
    response=client.get(
      '/users',
      headers={'Authorization': 'Bearer '+accesstoken}
    )
    if tester=='editor':
      assert response.status_code==200
      assert response.json()==[USER['editor']['output'],USER['not editor']['output']]
    else:
      assert response.status_code==400


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

def test_failure_get_character():
  testers=['editor', 'not editor']
  for tester in testers:
    accesstoken = _get_access_token(tester)
    response = client.get(
      '/characters/me',
      headers={'Authorization': 'Bearer '+accesstoken},
    )

    assert response.status_code==200
    assert response.json() == {"status":False,"data":"Not Registered.try to post quest @ /characters/me with params... department:str,position:str,skills:str[...]"}

def test_create_character_me():
  testers = ["editor", "not editor"]
  for tester in testers:
    accesstoken=_get_access_token(tester)
    response=client.post(
      '/characters',
      headers={'Authorization': 'Bearer '+accesstoken},
      json = CHARACTERS[tester]["input"]
    )

    assert response.status_code==200
    assert response.json()==CHARACTERS[tester]["output"]

def test_get_characters():
  testers=['editor', 'not editor']
  for tester in testers:
    accesstoken = _get_access_token(tester)
    response = client.get(
      '/characters/me',
      headers={'Authorization': 'Bearer '+accesstoken},
    )

    assert response.status_code==200
    assert response.json()== CHARACTERS[tester]['output']

def test_update_characters():
  testers=['editor', 'not editor']
  for tester in testers:
    accesstoken = _get_access_token(tester)
    response = client.put(
      '/characters/me',
      headers={'Authorization': 'Bearer '+accesstoken},
      json = {'skills': ['updated','nice']}
    )

    updated = CHARACTERS[tester]['output']
    updated['skills'] = ['updated','nice']
    assert response.status_code == 200
    assert response.json() == updated

def test_get_updated_characters():
  testers=['editor', 'not editor']
  for tester in testers:
    accesstoken = _get_access_token(tester)
    response = client.get(
      '/characters/me',
      headers={'Authorization': 'Bearer '+accesstoken},
    )

    assert response.status_code==200
    assert response.json()== CHARACTERS[tester]['output']

def test_failure_create_report():
  testers=['editor', 'not editor']
  for tester in testers:
    json=REPORTS[tester]['input'].copy().pop('title')
    accesstoken = _get_access_token(tester)
    response = client.post(
      '/reports',
      headers={'Authorization': 'Bearer '+accesstoken},
      json = json
    )

    assert response.status_code==422

def test_failure_get_reports():
  testers=['editor', 'not editor']
  for tester in testers:
    accesstoken = _get_access_token(tester)
    response = client.post(
      '/reports',
      headers={'Authorization': 'Bearer '+accesstoken}
    )
    assert response.status_code==422


def test_create_report():
  testers=['editor', 'not editor']
  for tester in testers:
    accesstoken = _get_access_token(tester)
    response = client.post(
      '/reports',
      headers={'Authorization': 'Bearer '+accesstoken},
      json = REPORTS[tester]['input']
    )

  assert response.status_code==200
  assert response.json()==REPORTS[tester]['output']





