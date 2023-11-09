from DB.redis.main_redis import make_redis_obj_with_a_specific_database
from variables_and_libs import AllData

def data_in_redis(item):
    redIs = make_redis_obj_with_a_specific_database(AllData.num_db)
    
    redIs.set_redis(item.phone, item.address)
    
    return "Ok"

def data_from_redis(phone):
    redIs = make_redis_obj_with_a_specific_database(AllData.num_db)
    
    return redIs.get_redis(phone)
    