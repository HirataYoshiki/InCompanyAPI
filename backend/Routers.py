# All router in apps are gather here.
# if you add new app using develop/MakeNewApp.py and the app includes router,
# import router and add the router here.

from auth import router as auth_router
from apps.register.router import router as register_router
from apps.character.router import router as character_router
from apps.report.router import router as report_router

ROUTERS=[
  auth_router,
  register_router,
  character_router,
  report_router
  ]