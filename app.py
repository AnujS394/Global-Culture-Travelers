from flask import Flask, render_template, url_for

app = Flask(__name__)

# Main pages
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/state.html')
def state():
    return render_template("state.html")

@app.route('/blog.html')
def blog():
    return render_template("blog.html")

@app.route('/translater.html')
def translater():
    return render_template("translater.html")

@app.route('/do.html')
def do_page():
    return render_template("do.html")

@app.route('/dont.html')
def dont_page():
    return render_template("dont.html")

# State Pages
@app.route('/mp.html')
def mp():
    return render_template("mp.html")

@app.route('/maharahtra.html')
def maharashtra():
    return render_template("maharahtra.html")

@app.route('/rajasthan.html')
def rajasthan():
    return render_template("rajasthan.html")

@app.route('/kerala.html')
def kerala():
    return render_template("kerala.html")

@app.route('/punjab.html')
def punjab():
    return render_template("punjab.html")

@app.route('/assam.html')
def assam():
    return render_template("assam.html")

@app.route('/odisha.html')
def odisha():
    return render_template("odisha.html")

# City / Cultural Pages
@app.route('/amravati.html')
def amravati():
    return render_template("amravati.html")

@app.route('/bhopal.html')
def bhopal():
    return render_template("bhopal.html")

@app.route('/indore.html')
def indore():
    return render_template("indore.html")

@app.route('/jabalpur.html')
def jabalpur():
    return render_template("jabalpur.html")

@app.route('/gwalior.html')
def gwalior():
    return render_template("gwalior.html")

@app.route('/ujjain.html')
def ujjain():
    return render_template("ujjain.html")

@app.route('/mumbai.html')
def mumbai():
    return render_template("mumbai.html")

@app.route('/nagpur.html')
def nagpur():
    return render_template("nagpur.html")

@app.route('/nashik.html')
def nashik():
    return render_template("nashik.html")

@app.route('/pune.html')
def pune():
    return render_template("pune.html")

@app.route('/jaipur.html')
def jaipur():
    return render_template("jaipur.html")

@app.route('/jodhpur.html')
def jodhpur():
    return render_template("jodhpur.html")

@app.route('/jaisalmer.html')
def jaisalmer():
    return render_template("jaisalmer.html")

@app.route('/udaipur.html')
def udaipur():
    return render_template("udaipur.html")

@app.route('/bikaner.html')
def bikaner():
    return render_template("bikaner.html")

@app.route('/b1.html')
def b1():
    return render_template("b1.html")

@app.route('/b2.html')
def b2():
    return render_template("b2.html")

@app.route('/b3.html')
def b3():
    return render_template("b3.html")

@app.route('/b4.html')
def b4():
    return render_template("b4.html")

@app.route('/b5.html')
def b5():
    return render_template("b5.html")

@app.route('/b6.html')
def b6():
    return render_template("b6.html")

@app.route('/uttarpradesh.html')
def uttarpradesh():
    return render_template("uttarpradesh.html")

@app.route('/jammukashmir.html')
def jammukashmir():
    return render_template("jammukashmir.html")

@app.route('/westbengal.html')
def westbengal():
    return render_template("westbengal.html")



if __name__ == "__main__":
    app.run(debug=True)
