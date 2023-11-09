from variables_and_libs import FastAPI, BackgroundTasks, uvicorn, DataRedis, Status,DataFromRedis
from DB.redis.crud_data import data_in_redis,data_from_redis

app = FastAPI(title="Test_task")

@app.post(
    "/write_data",
    description = "Метод для записи данных в Redis"
)
async def write_data_in_redis(item : DataRedis,
                                background_tasks : BackgroundTasks) -> Status:
    """
    
    """
    background_tasks.add_task(
                                data_in_redis,
                                item
                            )
    
    return Status(status = "OK")

@app.post(
    "/check_data/{phone}",
    description = "Метод для чтения данных из Redis"
)
async def read_data_from_redis(phone : str) -> DataFromRedis:
    """
    
    """
    
    return DataFromRedis(address = data_from_redis(phone))

if __name__ == "__main__":
    uvicorn.run(app,
                host="0.0.0.0",
                port=80)