from flask import Flask, render_template, request , redirect
import re



app = Flask(__name__)


notes = []
@app.route('/', methods=["POST",'GET'])
def index():
    return render_template("home.html" ,message=False )

@app.route('/result',methods=['POST'])
def result():
    pattern = request.form.get('pattern')
    text = request.form.get('string')
    if pattern and text:
        matches = re.finditer(pattern=pattern, string=text)

        # text = re.sub(pattern='('+pattern+')',repl=r'<span>\1</span>',string=text)
        matches = [(match.group(),match.start(),match.end()) for match in matches]
        lis = []
        start = 0
        count = 0
        for match in matches:
            lis.append(('o',text[start:match[1]],None))
            lis.append(('h',text[match[1]:match[2]],count))
            count += 1
            start = match[2]
        lis.append(('o',text[start:],None))
        print(repr(text))
    
        return render_template("home.html" , matches = matches , pattern = pattern , text = lis , message=False )
    else:
        return redirect('/')
@app.route('/email_validate',methods = ['POST'])
def validate():

    email = request.form.get('email')
    email = email.strip()
    match = re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    return render_template("home.html" , email_valid = True if match else False , message = True)


if __name__ == '__main__':
    app.run(debug=True , port=5000)
