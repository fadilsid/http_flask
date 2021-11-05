from flask import Flask,request
from flask_cors import CORS
import requests
import json
import pdfkit


app=Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/print', methods=['POST','GET'])
def get_pdf():
    
    if request.method=='POST':
        clicked=request.json['item_array']
        hello = "KOT <br>"
        hello += "__________<br>"
        for i in clicked:

            print(i)
            print(str(i))
            item_name=i['Item_Name']
            item_code=i['Item_Code']
            qty=i['Qty']
            hello += '{} - {}  -  x {} <br>'.format(item_code,item_name,qty)

        options={
            "page-width":76.2
        }
        
        pdfkit.from_string(str(hello),'invoice6.pdf',options=options)
        
        return str(clicked)
