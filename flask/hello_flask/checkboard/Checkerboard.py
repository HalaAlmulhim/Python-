from flask import Flask , render_template
app =  Flask(__name__)

print(__name__)

@app.rote('/')
def checkboard():
    return render_template("checkboard.html", x=8 , y=8)

@app.route("/<y>")
def checkboard1(y):
    return render_template("checkboard.html" , x=8 , y=int(y))

@app.route("//<x>/<y>")
def checkboard2(x, y):
    return render_template("checkboard.html" , x=int(x) , y=int(y))


if __name__=="__main__":
    app.run(debug=True)