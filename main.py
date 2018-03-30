from flask import Flask,request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
       <form action="/encrypt" method="post">
        <label>
            Rotate by
            <input type="text" value=0 name="Rotate_by"/>
         <textarea rows="4" cols="50" name="str_encrypt">{0}</textarea>   
         
        </label>
        <br><input type="submit" value="Submit Query"/>
    </form>
    </body>
</html>
"""


@app.route("/encrypt", methods=['POST'])
def encrypt():
    
    Rotate_by=request.form['Rotate_by']
    str_encrypt=request.form['str_encrypt']

    return form.format(rotate_string(str_encrypt,int(Rotate_by)))
@app.route("/")
def index():

    return form.format("")
app.run()


