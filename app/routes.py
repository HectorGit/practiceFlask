from app import app #means to get the app flask intance from the /app package

@app.route('/')
def index():
    return "Hello, World!" #here usually we would return some sort of a template, and possibly pass it some data if necessary 