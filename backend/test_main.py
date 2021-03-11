from apps.report.router import Content
from re import S
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

CONTENT={
  'editor': {
    'input': {
      1: {
        'content': 'editor'
      },
      2: {
        'content': 'another1'
      }
    },
    'output':{
      1: {
        'localcontentid': 1,
        'content': 'editor',
        'groupid': None
      },
      2: {
        'localcontentid': 2,
        'content': 'another1',
        'groupid': None
      }
    },
    'inner': {
      1: {
        'contentid': 1,
        'localcontentid': 1,
        'username': 'a',
        'content': 'update editor'
      },
      2: {
        'contentid': 5,
        'localcontentid': 2,
        'username': 'a',
        'content': 'another1'
      }
    }
  },
  'not editor': {
    'input': {
      1: {
        'content': 'not editor'
      },
      2: {
        'content': 'another2'
      }
    },
    'output':{
      1: {
        'localcontentid': 1,
        'content': 'not editor',
        'groupid': None
      },
      2: {
        'localcontentid': 2,
        'content': 'another2',
        'groupid': None
      }
    },
    'inner': {
      1: {
        'contentid': 2,
        'localcontentid': 1,
        'username': 'b',
        'content': 'update not editor'
      },
      2: {
        'contentid': 6,
        'localcontentid': 2,
        'username': 'b',
        'content': 'another2'
      }
    }
  }
}

CONTENTGROUP= {
  'editor': {
    'inner': {
      1: {
        'groupid': 1,
        'username': USER['editor']['input']['username'],
        'localgroupid': 1,
        'contentid': CONTENT['editor']['inner'][1]['contentid'],
        'order': 0
      },
      2: {
        'groupid': 2,
        'username': USER['editor']['input']['username'],
        'localgroupid': 1,
        'contentid': CONTENT['editor']['inner'][2]['contentid'],
        'order': 1
      }
    }
  },
  'not editor': {
    'inner': {
      1: {
        'groupid': 3,
        'username': USER['not editor']['input']['username'],
        'localgroupid': 1,
        'contentid': CONTENT['not editor']['inner'][1]['contentid'],
        'order': 0
      },
      2: {
        'groupid': 4,
        'username': USER['not editor']['input']['username'],
        'localgroupid': 1,
        'contentid': CONTENT['not editor']['inner'][2]['contentid'],
        'order': 1
      }
    }  
  }
}

ACCESSTOKENS={
  'editor': "",
  'not editor': ""
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
    ACCESSTOKENS[tester]=response.json()['access_token']
    assert response.status_code==200

def test_get_all_users():
  testers = ['editor','not editor']
  for tester in testers:
    response=client.get(
      '/users',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]}
    )
    if tester=='editor':
      assert response.status_code==200
      assert response.json()==[USER['editor']['output'],USER['not editor']['output']]
    else:
      assert response.status_code==400


def test_get_users_me():
  testers = ['editor','not editor']
  for tester in testers:
    
    response=client.get(
      '/users/me',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]}
    )

    assert response.status_code==200
    assert response.json()==USER[tester]['output']

def test_update_me():
  testers = ['editor','not editor']
  for tester in testers:
    
    response=client.put(
      '/users/me',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = {'mailaddress':'kirryx@gmail.com'}
    )

    USER[tester]['output']["mailaddress"]='kirryx@gmail.com'

    assert response.json()['item']==USER[tester]['output']

def test_failure_get_character():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.get(
      '/characters/me',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
    )

    assert response.status_code==400

def test_create_character_me():
  testers = ["editor", "not editor"]
  for tester in testers:
    
    response=client.post(
      '/characters',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = CHARACTERS[tester]["input"]
    )

    assert response.status_code==200
    assert response.json()==CHARACTERS[tester]["output"]

def test_get_characters():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.get(
      '/characters/me',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
    )

    assert response.status_code==200
    assert response.json()== CHARACTERS[tester]['output']

def test_update_characters():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.put(
      '/characters/me',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = {'skills': ['updated','nice']}
    )
    CHARACTERS[tester]['output']['skills'] = ['updated','nice']
    assert response.json() == CHARACTERS[tester]['output']
    assert response.status_code == 200

def test_get_updated_characters():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.get(
      '/characters/me',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
    )

    assert response.status_code==200
    assert response.json()== CHARACTERS[tester]['output']

def test_failure_create_report():
  testers=['editor', 'not editor']
  for tester in testers:
    json=REPORTS[tester]['input'].copy().pop('title')
    
    response = client.post(
      '/reportapp/reports',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = json
    )
    assert response.status_code==422

def test_failure_get_reports():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.post(
      '/reportapp/reports',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]}
    )
    assert response.status_code==422


def test_create_report():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.post(
      '/reportapp/reports',
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = REPORTS[tester]['input']
    )

  assert response.status_code==200
  assert response.json()==REPORTS[tester]['output']

def test_failure_update_report_header_is_not_registered():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.put(
      f"/reportapp/headers/{REPORTS[tester]['output']['localreportid']}",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = {'headerid': 1}
    )

    assert response.status_code==422

def test_failure_create_report_header():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.post(
      "/reportapp/headers",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = {'typei': 56}
    )
    assert response.status_code==422
 
def test_create_report_header():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.post(
      "/reportapp/headers",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = {'type': tester}
    )
    assert response.json()=={'localheaderid': 1,'type': tester}
    assert response.status_code==200

    
def test_update_report_header():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.put(
      "/reportapp/headers/1",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = {'type': "updated "+ tester}
    )
    assert response.json()=={"localheaderid": 1,"type": "updated "+ tester}
    assert response.status_code==200

def test_failure_create_content():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.post(
      "/reportapp/contents",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = {'contents': 2}
    )
    assert response.status_code==422

def test_create_content():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.post(
      "/reportapp/contents",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = CONTENT[tester]['input'][1]
    )
    assert response.json()==CONTENT[tester]['output'][1]
    assert response.status_code==200
    

def test_update_content():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.put(
      "/reportapp/contents/1",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = {'content': "update "+ tester}
    )
    assert response.status_code==200
    CONTENT[tester]['output'][1]['content']="update " + tester
    assert response.json()==CONTENT[tester]['output'][1]

def test_delete_content():
  testers=['editor', 'not editor']
  for tester in testers:
    
    dummy = client.post(
      "/reportapp/contents",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json = {'content': "dummy"}
    )

    response = client.delete(
      "/reportapp/contents/2",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
    )
    assert response.json()=={"status":True,"localcontentid": 2}
    assert response.status_code==200

def test_get_content_by_localcontentid():
  testers=['editor', 'not editor']
  for tester in testers:
    ACCESSTOKENS[tester] = _get_access_token(tester)
    response = client.get(
      "/reportapp/contents/1",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
    )
    assert response.json()==CONTENT[tester]['output'][1]
    assert response.status_code==200

def test_failure_get_content_by_id():
  testers=['editor', 'not editor']
  for tester in testers:
    
    response = client.get(
      "/reportapp/contents/2",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
    )
    assert response.status_code==400

def test_create_contentgroup():
  testers=['editor', 'not editor']
  for tester in testers:
    
    anothercontent = client.post(
      "/reportapp/contents",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json=CONTENT[tester]['input'][2]
    )

    response = client.post(
      "/reportapp/groups",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json={'localcontentids': [1,2]}
    )
    assert response.json()=={'localgroupid': 1,'contents': [CONTENT[tester]['inner'][1],CONTENT[tester]['inner'][2]]}

def test_get_contentgroup():
  testers=['editor', 'not editor']
  for tester in testers:
    response = client.get(
      "/reportapp/groups/1",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
    )
    assert response.json()=={'localgroupid': 1,'contents': [CONTENT[tester]['inner'][1],CONTENT[tester]['inner'][2]]}

def test_update_contentgroup():
  testers=['editor', 'not editor']
  for tester in testers:
    response = client.put(
      "/reportapp/groups/1",
      headers={'Authorization': 'Bearer '+ACCESSTOKENS[tester]},
      json={'localcontentids': [2,1]}
    )
    CONTENTGROUP[tester]['inner'][1]['groupid']+=5
    CONTENTGROUP[tester]['inner'][2]['groupid']+=3
    CONTENTGROUP[tester]['inner'][1]['order']=1
    CONTENTGROUP[tester]['inner'][2]['order']=0
    assert response.json()=={'localgroupid': 1,'contents': [CONTENTGROUP[tester]['inner'][2],CONTENTGROUP[tester]['inner'][1]]}


