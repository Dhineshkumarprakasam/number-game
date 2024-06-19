import sqlitecloud
from flask import Flask,render_template,request


url="sqlitecloud://cvwila88sk.sqlite.cloud:8860?apikey=cxhqnmn4jWRfmDVBbGZKsgPRLCP7iB389Mg2Swl2q9c"
con=sqlitecloud.connect(url)
cursor=con.cursor()
cursor.execute("use database game")
cursor.close()

app=Flask(__name__)

name=''
score=''
lev=''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_score',methods=['POST','GET'])
def save_score():
    global score
    global lev
    global name
    if request.method=='POST':
        cursor=con.cursor()
        score=request.form.get('score')
        if lev=="Easy level":
            cursor.execute("insert into easy (name,score) values(?,?)",(name,int(score)))
            con.commit()
        elif lev=="Medium level":
            cursor.execute("insert into medium (name,score) values(?,?)",(name,int(score)))
            con.commit()
        else:
            cursor.execute("insert into difficult (name,score) values(?,?)",(name,int(score)))
            con.commit()
        cursor.close()
        return render_template('index.html') 

@app.route('/game',methods=['POST','GET'])
def send_data():
    global name
    global lev
    if request.method == 'POST':
        name=request.form.get('username')
        lev=request.form.get('lev')
        return render_template('game.html',name=name,lev=lev)
@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

@app.route('/easy')
def easy():
    cursor=con.cursor()
    cursor.execute("select * from easy order by score desc")
    data=cursor.fetchall()
    cursor.close()
    return render_template('easy.html',easy=data)

@app.route('/medium')
def medium():
    cursor=con.cursor()
    cursor.execute("Select * from medium order by score desc")
    data=cursor.fetchall()
    cursor.close()
    return render_template('medium.html',medium=data)

@app.route('/difficult')
def difficult():
    cursor=con.cursor()
    cursor.execute("select * from difficult order by score desc")
    data=cursor.fetchall()
    cursor.close()
    return render_template('difficult.html',difficult=data)

@app.route('/help')
def helppage():
    return render_template('help.html')


if __name__=="__main__":
    app.run(debug=True)