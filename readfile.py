from fileinput import filename
import imp
from flask import Flask, render_template,request,redirect
import os
from werkzeug.utils import secure_filename
import pywhatkit as kit
import docx
import PyPDF2
from PIL import Image


def readfile(filename):
    ext=os.path.splitext(filename)[-1].lower()
    if ext=='.txt':
        f = open(filename, 'r')
        readcontent = f.read()
        text = kit.text_to_handwriting(
            readcontent, 'D:/pakhi/Documents/Competitons/Projects/text to handwriting/static/readcontent/test1.PNG', rgb=(20, 20, 20))
    elif ext=='.docx':
        doc = docx.Document(filename)
        doctext = []
        for singleline in doc.paragraphs:
            doctext.append(singleline.text)
        readcontent='\n'.join(doctext)
        text = kit.text_to_handwriting(
            readcontent, 'D:/pakhi/Documents/Competitons/Projects/text to handwriting/static/readcontent/test1.PNG', rgb=(20, 20, 20))
    elif ext=='.pdf':
        pdf = filename
        pdfread = PyPDF2.PdfFileReader(pdf)
        page = pdfread.getPage(0)
        pagecontent = page.extractText()
        readcontent = ' '.join(pagecontent.split())
        text = kit.text_to_handwriting(
            readcontent, 'D:/pakhi/Documents/Competitons/Projects/text to handwriting/static/readcontent/test1.PNG', rgb=(20, 20, 20))
    
    image = Image.open(
        'D:/pakhi/Documents/Competitons/Projects/text to handwriting/static/readcontent/test1.PNG')
    im=image.convert('RGB')
    im.save(r'D:/pakhi/Documents/Competitons/Projects/text to handwriting/static/readcontent/test1.pdf')

    return 'test1.PNG'


app = Flask(__name__)

app.config['IMAGE_UPLOADS'] = 'D:/pakhi/Documents/Competitons/Projects/text to handwriting/static/uploads'


@app.route("/", methods=['POST', 'GET'])
def upload_image():
    if request.method=='POST':
        image=request.files['file']
        if image.filename=='':
            print('Invalid')
            return redirect(request.url)

        filename=secure_filename(image.filename)

        basedir=os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config['IMAGE_UPLOADS'],filename))

        filen=readfile(filename)


        return render_template('index.html',filename=filename)

    return render_template('index.html')

# print(filename)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='/readcontent/test1.png'), code=301)


app.run(debug=True,port=5000)
