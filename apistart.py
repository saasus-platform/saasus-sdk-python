from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from saasus_sdk_python.callback.callback import Callback
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # この部分は適切なオリジンに制限すること,今回はサンプルアプリが動いてるポートにする
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/credential")
async def callback(request: Request):
    return await Callback().callback_route_function(request)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
