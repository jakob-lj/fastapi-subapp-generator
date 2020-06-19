import os
import sys

try:
    name = sys.argv[1]
except:
    print("Missing sub name")
    sys.exit(1)

os.system("mkdir %s" % name)

init = open("%s/__init__.py" % name, "w")
crd = open("%s/crud.py" % name, "w")
database = open("%s/database.py" % name, "w")
models = open("%s/models.py" % name, "w")
schemas = open("%s/schemas.py" % name, "w")
app = open("%s/app.py" %name, "w")

crd.write("""
from sqlalchemy.orm import Session

from . import models, schemas

# TODO: write crud functions
""")

database.write("""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./boatbook.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@host.docker.internal:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# TODO: Update database connection
""")

schemas.write("""
from typing import List

from pydantic import BaseModel

# TODO: write schemas
""")

models.write("""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# TODO: Write models
""")

app.write("""
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# TODO: Create endpoints
""")


init.close()
crd.close()
database.close()
models.close()
schemas.close()
app.close()