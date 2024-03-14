import base64
from typing import Any, TypedDict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Params(TypedDict, total=False):
    """传递的参数"""

    source_file: Any


@app.post("/train")
async def compare_data(params: Params):
    print(f"{params=}")

    with open("../result.png", "rb") as fb:
        contents = fb.read()
        b64 = base64.b64encode(contents).decode()

        return b64
