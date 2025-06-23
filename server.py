from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import sys

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>Hello</title>
        </head>
        <body>
            <h1>Hello world</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
    

@app.get("/json")
async def json():
    return {"message": "Hello World"}

if __name__ == "__main__":
    try:
        port=int(sys.argv[1])
    except:
        port=9876
    uvicorn.run(app, host="0.0.0.0", port=port)
