from quart import Quart, jsonify, request, send_from_directory
import random

app = Quart(__name__)

@app.get("/health")
async def health():
    return jsonify({"status": "ok"})

@app.get("/api/v1/random")
async def get_random():
    return jsonify({"value": random.randint(1, 100), "min": 1, "max": 100})

@app.post("/api/v1/reverse")
async def post_reverse():
    data = await request.get_json()
    num = data.get("number", 0)
    return jsonify({"original": num, "reversed": int(str(num)[::-1])})

@app.get("/api/v1/greet")
async def greet_user():
    return jsonify({"message": "Bigoof"})

@app.post("/api/v1/wordcount")
async def word_count():
    data = await request.get_json()
    text = data.get("text", "")
    char_count = len(text)
    word_count = len(text.split())
    
    return jsonify({
        "text": text,
        "characters": char_count,
        "words": word_count
    })

@app.get("/") # Root dir to serve html.
async def index():
    return await send_from_directory(".", "index.html")

@app.get("/js.js") # runs when root asks for js file 
async def javascript():
    return await send_from_directory(".", "js.js")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
