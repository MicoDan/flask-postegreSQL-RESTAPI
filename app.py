from flask import Flask

app = Flas(__name__)

@app.get("/")
def home():
    return "Hello, world"