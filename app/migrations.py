import alembic.config
import os, os.path

os.chdir(os.path.join(os.path.dirname(__file__), "db"))

alembic.config.main(
    argv=[
        "--raiseerr",
        "upgrade",
        "head"
    ]
)