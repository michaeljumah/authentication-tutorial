from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

#def write_notification(email: str, message=""):
#    with open("log.txt", mode="w") as email_file:
 #       content = f"notification for {email}:{message}"
  #      email_file.write(content)
def add_nums(a: int, b:int):
    return a+b
        

@app.post("/send-notification/{email}")
async def send_notification(email: str, backgroundtasks: BackgroundTasks):
    backgroundtasks.add_task(write_notification, email, message="some notifications")
    return {"message":"Notification sent in the background"}
