from flask import Flask, request
import codecs
from PIL import Image
import pytesseract

app = Flask(__name__)	

@app.route('/')
def main():
	f = codecs.open("index.html", 'r', 'utf-8')
	document = f.read()
	template = """{0}"""
	template = template.format(document)
	return template

@app.route('/proccess_ocr', methods=['POST'])
def ocr():

	if request.method == 'POST':

		dt = request.json
		dts = dt["photo"].split("\\")
		img_path = "static/img/" + dts[2]

		text = pytesseract.image_to_string(Image.open(img_path), config = ('-l eng --oem 1 --psm 3'))
		ret = {"text": text, "path": img_path}
		return ret
	else:
		return "NOT OK"

@app.route('/proccess_flow', methods=['POST'])
def decision_flow():

	if request.method == 'POST':		
		return request.json

	else:
		return "NO OK"

if __name__ == '__main__':
    app.run(debug=True)