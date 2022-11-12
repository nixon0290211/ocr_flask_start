from PIL import Image
from flask import Flask, render_template, request
import pyocr

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    # リクエストファイル
    ocr_file = request.files["file"]
    img = Image.open(ocr_file)
    # OCRの準備
    tools = pyocr.get_available_tools()
    tool = tools[0]
    # OCR
    txt = tool.image_to_string(
        img, lang="eng+jpn", builder=pyocr.builders.TextBuilder()
    )
    # 読みとりエラー
    return render_template("index.html", txt=txt)


if __name__ == "__main__":
    app.run(host="0,0,0,0", port=5001, debug=True)
