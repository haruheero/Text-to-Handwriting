# Text to Handwriting

Text to handwriting is an innovative app that can convert the text in uploaded document to handwriting format. The file can be uploaded in the format of pdf, txt or docx.
The text inside the file is then converted into handwriting using text_to_handwriting function of pywhatkit. The converted text is then returned inside an image format by the 
pywhatkit library. The converted text image is displayed on the app.

![Screenshot (569)](https://user-images.githubusercontent.com/63349641/149621628-e4f618e4-e407-44e4-b295-70433ac7c715.png)


## Usage

To use the app the user should click on the upload your files here button. User will then be prompted to upload a file from their local machine.

![image](https://user-images.githubusercontent.com/63349641/149621687-bd639d35-46b8-475e-88e5-85f89148f93b.png)

After successful upload *File Uploaded* will be displayed inside the box. 

![Screenshot (571)](https://user-images.githubusercontent.com/63349641/149621755-180aafe6-4c1e-436a-892b-64e7bb73f19f.png)

The by clicking on the Submit button the user can convert the text to handwriting.
After the conversion and display the users are given 2 options:
- They can download the png format.
- They can download the pdf format.

![Screenshot (572)](https://user-images.githubusercontent.com/63349641/149621598-7853e355-1b6a-4ca9-b04a-cb539f0d5208.png)

The file can be downloaded by clicking on the respective buttons given below the displayed image.

![Screenshot (573)](https://user-images.githubusercontent.com/63349641/149621612-5958fe52-443a-411e-ae57-e8d0e85a3426.png)

## Features

- Available in dark mode
- Responsive
- Download file in png or pdf
- Upload in any of the 3 formats (docx, txt, pdf)

 ### Dark mode

![Full page ss](https://user-images.githubusercontent.com/63349641/149622095-4b42c03a-511d-4de1-8838-ca5479bb5393.png)

### Responsive

<img src="https://user-images.githubusercontent.com/63349641/149622618-d56eb69f-58d3-4636-859e-a00ac4032dba.png" width="380">

## Working and technologies used
- Flask
- HTML
- CSS
- JavaScript
- Pywhatkit
- Docx
- PyPDF2

Text to Handwriting makes use of flask, pywhatkit, PyPDF2, docx, PIL, werkzeug, os as main libraries of python. The file is first uploaded and then stored in the uploads folder.
Then the file is read. The extension of the file is extracted then it is passed to the respective block to be further used. The file is then read by the filereaders and converted
to string and passed to pywhatkit text to handwriting library. The image is then returned and displayed on website via the flask operation.

The frontend of the website is made using HTML, CSS and JavaScript. The navbar contains links for home, about, features and contact and a toggle button for switching between light
theme and dark theme. Flask has been used to effectively upload and download converted and original documents.

## Demo
https://user-images.githubusercontent.com/63349641/149623032-101de590-1219-4977-851d-73111ccc8c28.mp4
