#Adam Abbas
#SoftDev pd 7
#HW04: Fill up yer Flask
#2017-09-21

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_werld():
    return "<title> Bird is the word </title> <h1> Welcome to my world </h1>\n<h3> You like birds? </h3><h3>Click bird!</h3>"
    return '<a href="/chicken"><center><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOEc4AAoTEXpd_xTB9EbjY2asvXZw_Hhk-0m-VS845Stod7SF6eQ"></center><br></a>'
    return '<a href="/duck"><center><img src="https://previews.123rf.com/images/tigatelu/tigatelu1404/tigatelu140400332/27657271-Cute-duck-cartoon-Stock-Vector.jpg"></center><br></a>'
    return '<a href="/penguin"><center><img src="https://openclipart.org/image/2400px/svg_to_png/17535/lemmling-Cartoon-penguin.png"></center><br></a>'
    return '<a href="/vulture"><center><img src="http://media.gettyimages.com/vectors/vulture-sitting-on-a-branch-vector-id512172788?s=612x612"></center><br></a>'
    return '<a href="/flamingo><center><img src="https://previews.123rf.com/images/cthoman/cthoman1403/cthoman140300025/26322292-A-cartoon-pink-flamingo-standing-on-one-leg--Stock-Vector.jpg"></center><br></a>'
    
    
@app.route("/chicken")
def chickpic():
    return "<style> body { background-color: red; }"
    return '<center><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOEc4AAoTEXpd_xTB9EbjY2asvXZw_Hhk-0m-VS845Stod7SF6eQ"></center>'


@app.route("/duck")
def duckpic():
    return "<style> body { background-color: yellow; }"
    return '<center><img src="https://previews.123rf.com/images/tigatelu/tigatelu1404/tigatelu140400332/27657271-Cute-duck-cartoon-Stock-Vector.jpg"></center>'


@app.route("/penguin")
def pengpic():
    return "<style> body { background-color: black; }"
    return '<center><img src="https://openclipart.org/image/2400px/svg_to_png/17535/lemmling-Cartoon-penguin.png"></center>'


@app.route("/vulture")
def vulpix():
    return "<style> body { background-color: purple; }"
    return '<center><img src="http://media.gettyimages.com/vectors/vulture-sitting-on-a-branch-vector-id512172788?s=612x612"></center>'

@app.route("/flamingo")
def flapic():
    return "<style> body {background-color: pink; }"
    return '<center><img src="https://previews.123rf.com/images/cthoman/cthoman1403/cthoman140300025/26322292-A-cartoon-pink-flamingo-standing-on-one-leg--Stock-Vector.jpg"></center>'



if __name__ == "__main__":
    app.debug = True
    app.run()
