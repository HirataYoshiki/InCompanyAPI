# All router in apps are gather here.
# if you add new app using develop/MakeNewApp.py and the app includes router,
# import router and add the router here.

from auth import router as auth_router
from apps.register.router import routers as register_router

ROUTERS=[
  auth_router,
  register_router
  ]