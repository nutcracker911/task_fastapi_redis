# -*- coding: utf-8 -*-
from variables_and_libs import AllData,redis


class Redis():
   
    def __init__(self, 
                host = AllData.host_redis,
                port= AllData.port_redis) -> None:
        self.host = host
        self.port = port
    
    def connect_redis(self, db):
        self.r = redis.Redis(host=self.host, 
                            port=self.port, 
                            db = db,
                            decode_responses=True)

    def set_redis(self, key:str, value:str):
        self.r.set(key, value)
        
        
    def get_redis(self, key:str):
        
        if key not in self.r.keys():
            return "client not found"
        
        return self.r.get(key) 
 
 

def make_redis_obj_with_a_specific_database(num_db:int):
    redIs = Redis()
    redIs.connect_redis(num_db)
    return redIs
