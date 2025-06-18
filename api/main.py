import json
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI(
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    input: dict

@app.post("/scrape-list")
def fastapi_scrape_list(req: PromptRequest):
    demo = req.input.get("demo")
    if demo:
        with open("app/scrape/list/demo.json", "r") as f:
            result = json.load(f)
    else:
        try:
            from app.scrape.list.logic import run_flow
            result = run_flow(req.input)
        except Exception as e:
            return JSONResponse(status_code=400, content={"success": False, "error": str(e)})

    return JSONResponse(status_code=200, content={"success": True, "data": result})

@app.post("/scrape-indivisual")
def fastapi_scrape_indivisual(req: PromptRequest):
    demo = req.input.get("demo")
    if demo:
        with open("app/scrape/indivisual/demo.json", "r") as f:
            result = json.load(f)
    else:
        try:
            from app.scrape.indivisual.logic import run_flow
            result = run_flow(req.input)
        except Exception as e:
            return JSONResponse(status_code=400, content={"success": False, "error": str(e)})

    return JSONResponse(status_code=200, content={"success": True, "data": result})

@app.post("/generate-hook")
def fastapi_generate_hook(req: PromptRequest):
    demo = req.input.get("demo")
    if demo:
        with open("app/generate/hook/demo.json", "r") as f:
            result = json.load(f)
    else:
        try:
            from app.generate.hook.logic import run_flow
            result = run_flow(req.input)
        except Exception as e:
            return JSONResponse(status_code=400, content={"success": False, "error": str(e)})

    return JSONResponse(status_code=200, content={"success": True, "data": result})

@app.post("/generate-content")
def fastapi_generate_content(req: PromptRequest):
    demo = req.input.get("demo")
    if demo:
        with open("app/generate/content/demo.json", "r") as f:
            result = json.load(f)
    else:
        try:
            from app.generate.content.logic import run_flow
            result = run_flow(req.input)
        except Exception as e:
            return JSONResponse(status_code=400, content={"success": False, "error": str(e)})

    return JSONResponse(status_code=200, content={"success": True, "data": result})


#activate
"""
uvicorn api.main:app --host 0.0.0.0 --port 8000
"""