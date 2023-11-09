from dataclasses import dataclass
import json
import redis
import sys
from fastapi import FastAPI, Request, BackgroundTasks
from pydantic import BaseModel
import uvicorn

class DataRedis(BaseModel):
    phone : str
    address : str

class DataFromRedis(BaseModel):
    address : str

class Status(BaseModel):
    status : str

@dataclass
class AllData:
    host_redis : str =  "127.0.0.1"
    port_redis : int = 6378
    num_db : int = 0