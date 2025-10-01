from apscheduler.schedulers.background import BackgroundScheduler
from pydantic import BaseModel, Field
from fastapi import FastAPI
from datetime import datetime
import uvicorn
from enum import Enum
from apscheduler.triggers.cron import CronTrigger

app = FastAPI(title="Basic Cronjob", description="Apply basic cron job functionality using fastapi")

scheduler = BackgroundScheduler()
scheduler.start()

def send_reminder():
    print(f"Reminder is sent at: {datetime.now()}")

# class Weekdays (str,Enum):
#     mon = "mon"
#     tue = "tue"
#     wed = "wed"
#     thu = "thu"
#     fri = "fri"
#     sat = "sat"
#     sun = "sun"


class TimeInput(BaseModel):

    month:str = Field(default="1,2,3,4,5,6,7,8,9,10,11,12")
    day:str = Field(default="mon,tue,wed,thu,fri,sat,sun")
    hour:int = Field(..., ge=0, le=23)
    minute:int = Field(..., ge=0, le=59)


@app.post("/send-reminder-route")
def send_reminder_route(time:TimeInput):

    cron_args = {
    "month":time.month,
    "day_of_week":time.day,
    "hour":time.hour,
    "minute":time.minute
}

    cron_args = {k:v for k,v in cron_args.items() if v is not None}
    print(cron_args)
    scheduler.add_job(send_reminder, CronTrigger(**cron_args))
    return {"message":f"Request will be sent at {time.hour}:{time.minute}"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=800, reload=True)




