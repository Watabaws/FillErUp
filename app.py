#Adam Abbas
#SoftDev pd 7
#HW04: Fill up yer Flask
#2017-09-21

from flask importFlask

app = Flask(__name__)

@app.route("/")
def hello_werld():
    print "<title> Bird is the word </title> <h1> Welcome to my world </h1>\n<h3> You like birds? </h3><h3>Click bird!</h3>"
    print '<a href="/chicken"><center><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOEc4AAoTEXpd_xTB9EbjY2asvXZw_Hhk-0m-VS845Stod7SF6eQ"></center><br></a>'
    print '<a href="/duck"><center><img src="https://previews.123rf.com/images/tigatelu/tigatelu1404/tigatelu140400332/27657271-Cute-duck-cartoon-Stock-Vector.jpg"></center><br></a>'
    print '<a href="/penguin"><center><img src="https://openclipart.org/image/2400px/svg_to_png/17535/lemmling-Cartoon-penguin.png"></center><br></a>'
    print '<a href="/vulture"><center><img src="http://media.gettyimages.com/vectors/vulture-sitting-on-a-branch-vector-id512172788?s=612x612"></center><br></a>'
    print '<a href="/flamingo><center><img src="https://previews.123rf.com/images/cthoman/cthoman1403/cthoman140300025/26322292-A-cartoon-pink-flamingo-standing-on-one-leg--Stock-Vector.jpg"></center><br></a>'
    
    
@app.route("/chicken")
def chickpic():
    print "<style> body { background-color: red; }"
    print '<center><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOEc4AAoTEXpd_xTB9EbjY2asvXZw_Hhk-0m-VS845Stod7SF6eQ"></center>'


@app.route("/duck")
def duckpic():
    print "<style> body { background-color: yellow; }"
    print '<center><img src="https://previews.123rf.com/images/tigatelu/tigatelu1404/tigatelu140400332/27657271-Cute-duck-cartoon-Stock-Vector.jpg"></center>'


@app.route("/penguin")
def pengpic():
    print "<style> body { background-color: black; }"
    print '<center><img src="https://openclipart.org/image/2400px/svg_to_png/17535/lemmling-Cartoon-penguin.png"></center>'


@app.route("/vulture")
def vulpix():
    print "<style> body { background-color: purple; }"
    print '<center><img src="http://media.gettyimages.com/vectors/vulture-sitting-on-a-branch-vector-id512172788?s=612x612"></center>'

@app.route("/flamingo")
def flapic():
    print "<style> body {background-color: pink; }"
    print '<center><img src="https://previews.123rf.com/images/cthoman/cthoman1403/cthoman140300025/26322292-A-cartoon-pink-flamingo-standing-on-one-leg--Stock-Vector.jpg"></center>'



if __name__ == "__main__":
    app.debug = True
    app.run()
    
