from flask import Flask, render_template, request
app = Flask(__name__)
def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            result += char
    return result
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        action = request.form['action']
        if action == 'Encrypt':
            result = encrypt(text, shift)
        else:
            result = encrypt(text, -shift)
        return render_template('index.html',original_text=text,
                               result=result, shift=shift)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
