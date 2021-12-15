import alembic.config
import os, os.path, time
from initializer.auth_initializer import check_create_single_admin

os.chdir(os.path.join(os.path.dirname(__file__), "db"))

time.sleep(5)

alembic.config.main(
    argv=[
        "--raiseerr",
        "upgrade",
        "head"
    ]
)

check_create_single_admin()