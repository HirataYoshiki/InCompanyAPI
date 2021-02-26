from typing import Optional
from fastapi import APIRouter,Depends

from auth import get_current_user
from db import get_session
from . import scheme,models

router= APIRouter()