from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play/<int:num>')
def playnum(num):
    return render_template('play.html', num = num)

@app.route('/play/<int:num>/<color>')
def playnumcolor(num, color):
    
    return render_template('play.html', num = num, color = color)
    


if __name__ == '__main__':

    app.run(debug = True)