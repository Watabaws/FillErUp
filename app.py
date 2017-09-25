#Adam Abbas
#SoftDev pd 7
#HW04: Fill up yer Flask
#2017-09-21

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_werld():
    return '''<title> Bird is the word </title> <h1> Welcome to my world </h1>\n<h3> You like birds? </h3><h3>Click bird!</h3>
    <a href="/chicken"><center><img width='100'  src="https://i.pinimg.com/236x/b8/8e/00/b88e00b6fa232a4b27b3d3cb0bd436a9--chicken-roosters.jpg"><br></a>'
    <a href="/duck"><img width='100'  src="https://previews.123rf.com/images/tigatelu/tigatelu1404/tigatelu140400332/27657271-Cute-duck-cartoon-Stock-Vector.jpg"><br></a>'
    <a href="/penguin"><img width='100'  src="https://openclipart.org/image/2400px/svg_to_png/17535/lemmling-Cartoon-penguin.png"><br></a>'
    <a href="/vulture"><img width='100'  src="http://media.gettyimages.com/vectors/vulture-sitting-on-a-branch-vector-id512172788?s=612x612"><br></a>'
    <a href="/flamingo><img width='100'  src="https://previews.123rf.com/images/cthoman/cthoman1403/cthoman140300025/26322292-A-cartoon-pink-flamingo-standing-on-one-leg--Stock-Vector.jpg"></center><br></a>'''


@app.route("/chicken")
def chickpic():
    return '''<style> body { background-color: red; } </style>
    <center><img width='500'src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOEc4AAoTEXpd_xTB9EbjY2asvXZw_Hhk-0m-VS845Stod7SF6eQ"></center>'''


@app.route("/duck")
def duckpic():
    return '''<style> body { background-color: yellow; } </style>
    <center><img width='500'  src="https://previews.123rf.com/images/tigatelu/tigatelu1404/tigatelu140400332/27657271-Cute-duck-cartoon-Stock-Vector.jpg"></center>'''


@app.route("/penguin")
def pengpic():
    return '''<style> body { background-color: black; } </style>
    <center><img width='500'  src="https://openclipart.org/image/2400px/svg_to_png/17535/lemmling-Cartoon-penguin.png"></center>'''


@app.route("/vulture")
def vulpix():
    return '''<style> body { background-color: purple; } </style>
    <center><img width='500'  src="http://media.gettyimages.com/vectors/vulture-sitting-on-a-branch-vector-id512172788?s=612x612"></center>'''

@app.route("/flamingo")
def flapic():
    return '''<style> body {background-color: pink; } </style>
    <center><img width='500'  src="https://previews.123rf.com/images/cthoman/cthoman1403/cthoman140300025/26322292-A-cartoon-pink-flamingo-standing-on-one-leg--Stock-Vector.jpg"></center>'''



if __name__ == "__main__":
    app.debug = True
    app.run()
