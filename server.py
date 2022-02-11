from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Type play, a number, and a color divided by / to start!'

@app.route('/play')
def play():
    return render_template('play.html', num = 3, color = 'lightblue')

@app.route('/play/<int:num>')
def playnum(num):
    return render_template('play.html', num = num, color = 'lightblue')

@app.route('/play/<int:num>/<color>')
def playnumcolor(num, color):
    
    return render_template('play.html', num = num, color = color)
    


if __name__ == '__main__':

    app.run(debug = True)