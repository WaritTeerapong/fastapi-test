from fastapt import Fastapt

app = Fastapt()

@app.get("/")
def index():
    return {"details": "Hello, World!"}
