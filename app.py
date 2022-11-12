from PIL import Image
from flask import Flask, render_template, request
import pyocr

# import requests
# import json

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

    # img_en_path = "images/tesseract_en.png"
    # img_jpn_path = "images/tesseract_jpn.png"


#     img = Image.open(img_en_path)
#     img = Image.open(file)
# if request.method == "POST":
#     if "file" not in request.files:
#         flash("ファイルが選択されていません")
# return redirect(request.url)

# file = request.files["ocrfile"]

#     if file.filename == "":
#         flash("ファイルが選択されていません")
#         return redirect(request.url)

#     if file:
#         outfile = paste_frame(file)
#         return render_template("upload.html", outfile=outfile)

# return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
