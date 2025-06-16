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
    demo = req.input["demo"]
    searchword = req.input["searchword"]
    amount = req.input["amount"]

    if demo:
        result = [
            {
                "url": "https://www.tiktok.com/@ddden49/video/7094935536153988353",
                "like": 389000,
                "number": 1
            },
            {
                "url": "https://www.tiktok.com/@ayami_yamichan/video/6971361926592924929",
                "like": 237400,
                "number": 2
            },
            {
                "url": "https://www.tiktok.com/@tantei_cosme/video/7255979521478823169",
                "like": 122200,
                "number": 3
            },
            {
                "url": "https://www.tiktok.com/@yokoyamaamane/video/7123899637299268865",
                "like": 101100,
                "number": 4
            },
            {
                "url": "https://www.tiktok.com/@gimihpxgwnx/video/7399960692142525704",
                "like": 66800,
                "number": 5
            },
            {
                "url": "https://www.tiktok.com/@nazo111111/video/7233339925830044929",
                "like": 57300,
                "number": 6
            },
            {
                "url": "https://www.tiktok.com/@mote_cosme/video/7080858571398745346",
                "like": 53000,
                "number": 7
            },
            {
                "url": "https://www.tiktok.com/@shushu_223_/video/7129087684571663618",
                "like": 52800,
                "number": 8
            },
            {
                "url": "https://www.tiktok.com/@egachannel1/video/7096065068353293569",
                "like": 48500,
                "number": 9
            },
            {
                "url": "https://www.tiktok.com/@karen_beauty02/video/7504999841597099284",
                "like": 48000,
                "number": 10
            },
            {
                "url": "https://www.tiktok.com/@1haud/video/7406597185027968264",
                "like": 45500,
                "number": 11
            },
            {
                "url": "https://www.tiktok.com/@tsumiki_beauty/video/7099374295180184834",
                "like": 43500,
                "number": 12
            },
            {
                "url": "https://www.tiktok.com/@noponopisu2/video/7127214496791137538",
                "like": 41900,
                "number": 13
            },
            {
                "url": "https://www.tiktok.com/@nao__belle/video/7377699725698534664",
                "like": 41600,
                "number": 14
            },
            {
                "url": "https://www.tiktok.com/@kuraberu_cosme/video/7391460008157842706",
                "like": 37100,
                "number": 15
            }
        ]
    else:
        try:
            from app.scrape.list.logic import run_flow
            result = run_flow(searchword, amount)
        except Exception as e:
            return JSONResponse(status_code=400, content={"success": False, "error": str(e)})

    return JSONResponse(status_code=200, content={"success": True, "data": result})

@app.post("/scrape-indivisual")
def fastapi_scrape_indivisual(req: PromptRequest):
    demo = req.input["demo"]
    url = req.input["url"]
    amount = req.input["amount"]

    if demo:
        result = {
            "comments": [
                {
                    "name": "M",
                    "like": 9576,
                    "text": "値段と知名度でアネッサ使ってるけどこれ使ってみようかな、、",
                    "number": 1
                },
                {
                    "name": "ﾋﾅﾀ",
                    "like": 5767,
                    "text": "左のめっちゃでかいの使ってる",
                    "number": 2
                },
                {
                    "name": "えぬえふ",
                    "like": 3617,
                    "text": "女子サッカー部の者です。左のやつ時間置いて2回塗るとまじで焼けないです。アネッサと比較しても肌に優しいしコスパが良すぎます。毎日太陽にさらされてるのに肌白いと褒めていただけるので本当にオススメします",
                    "number": 3
                },
                {
                    "name": "すいれん 柴石",
                    "like": 3307,
                    "text": "どっちも使ったことあるけど白くなるのは伸び悪いし日焼け効果高いのはアリーだから間違えないで",
                    "number": 4
                },
                {
                    "name": "大崎",
                    "like": 2913,
                    "text": "おいおいさっきキュレル買っちゃったぞ",
                    "number": 5
                },
                {
                    "name": "( ◜ᴗ◝)",
                    "like": 1636,
                    "text": "Bioreばり良い、、。顔に使ってるんですけど、使い始めてから焼けてないって断言出来るくらい焼けてないです！！！",
                    "number": 6
                },
                {
                    "name": "B型女子",
                    "like": 1558,
                    "text": "女子サッカー部の者です。左のやつ時間置いて2回塗るとまじで焼けないです。アネッサと比較しても肌に優しいしコスパが良すぎます。毎日太陽にさらされてるのに肌白いと褒めていただけるので本当にオススメします",
                    "number": 7
                },
                {
                    "name": "모아♡",
                    "like": 890,
                    "text": "私の肌にはアリーが最強だった！",
                    "number": 8
                },
                {
                    "name": "小麦粉",
                    "like": 806,
                    "text": "右の日焼け止めを使ったらトーンアップしたおかげで、顔色悪いよ？大丈夫？と言われたので色黒さんは顔には向いてなさそうです😂",
                    "number": 9
                },
                {
                    "name": "はいさ",
                    "like": 714,
                    "text": "どっちの方がいいんだろうか…コメ欄見てると意外とマイナス意見あって迷う。右白くなるの凄いけどラメ多いって学校に塗っていけなそうな感じする…💭左に関してのコメあまりないから情報ほしい🥲",
                    "number": 10
                },
                {
                    "name": "ひなぴっ！🌟",
                    "like": 502,
                    "text": "右いつも使ってる！！",
                    "number": 11
                },
                {
                    "name": "︎︎",
                    "like": 445,
                    "text": "2つ目水に濡れたら白くなって手にカルピスついてるみたいになるから手の甲とかには塗らん方がいい🥲👍🏻",
                    "number": 12
                },
                {
                    "name": "まる",
                    "like": 424,
                    "text": "右を愛用している者です！ベタつきも少なく、光拡散ラメが入っているのでトーンアップ効果があります。よく白いねと言われるほど、最強です(><)♡♡これはリピ買いするほど良いのでオススメです！",
                    "number": 13
                },
                {
                    "name": "こはく",
                    "like": 406,
                    "text": "日焼け止め顔に塗ると、笑った後にほうれい線みたいな跡がつくので、皆さんどう対処してますか？？",
                    "number": 14
                },
                {
                    "name": "🐼",
                    "like": 362,
                    "text": "1倍最初に買ったのそれで私優勝(ごめんなさい)",
                    "number": 15
                }
            ],
            "datas": {
                "likes": 389000,
                "comments": 2164,
                "saves": 47800,
                "shares": 4479
            }
        }
    else:
        try:    
            from app.scrape.indivisual.logic import run_flow
            result = run_flow(url, amount)
        except Exception as e:
            return JSONResponse(status_code=400, content={"success": False, "error": str(e)})

    return JSONResponse(status_code=200, content={"success": True, "data": result})

@app.post("/generate-hook")
def fastapi_generate_hook(req: PromptRequest):
    demo = req.input["demo"]
    if demo:
        result = """
This is a DEMO DATA.
"""
    else:
        try:
            from app.generate.hook.logic import run_flow
            result = run_flow(req.input)
        except Exception as e:
            return JSONResponse(status_code=400, content={"success": False, "error": str(e)})

    return JSONResponse(status_code=200, content={"success": True, "data": result})

@app.post("/generate-content")
def fastapi_generate_content(req: PromptRequest):
    demo = req.input["demo"]
    if demo:
        result = """
This is a DEMO DATA.
"""
    else:
        try:
            from app.generate.content.logic import run_flow
            result = run_flow(req.input)
        except Exception as e:
            return JSONResponse(status_code=400, content={"success": False, "error": str(e)})

    return JSONResponse(status_code=200, content={"success": True, "data": result})


#ngrok
"""
ngrok http 8000
"""

#activate
"""
uvicorn api.main:app --host 0.0.0.0 --port 8000
"""