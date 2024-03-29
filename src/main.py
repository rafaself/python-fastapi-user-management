from src.apps.authentication.middlewares import check_permissions
from src.apps.authentication.routes import auth_router
from src.apps.many_to_many.permissions_groups_and_permissions.routes import permissions_and_groups_router
from src.apps.many_to_many.permissions_groups_and_users.routes import users_and_groups_router
from src.apps.permissions.routes import permissions_router
from src.apps.permissions_groups.routes import permissions_groups_router
from src.apps.routes.routes import routes_router
from src.apps.users.routes import user_router

from fastapi import FastAPI


app = FastAPI()


@app.get("/hello-world")
def hello_world():
    return "Hello world!"


app.middleware("http")(check_permissions)


app.include_router(user_router)
app.include_router(auth_router)
app.include_router(permissions_router)
app.include_router(permissions_groups_router)
app.include_router(users_and_groups_router)
app.include_router(permissions_and_groups_router)
app.include_router(routes_router)
