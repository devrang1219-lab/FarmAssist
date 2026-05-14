from fastapi import FastAPI

app = FastAPI(title="FarmAssist Backend", description="Broker web app for connecting farmers and workers")

@app.get("/")
def read_root():
    return {"message": "Welcome to FarmAssist Backend"}

@app.get("/farmers")
def get_farmers():
    # Placeholder for farmer listings
    return {"farmers": []}

@app.get("/workers")
def get_workers():
    # Placeholder for worker listings
    return {"workers": []}

@app.post("/login")
def login(phone: str):
    # Placeholder for phone number login
    return {"token": "dummy_token", "user": {"phone": phone}}