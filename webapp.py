from flask import Flask,redirect,url_for,request,render_template,make_response
app = Flask(__name__,template_folder='templates',static_folder='static')


@app.route("/")
def home():
	return render_template('home.html')

#@app.route("/data",methods=['POST','GET'])
#def data():
#	return render_template('home1.html')


if __name__ == '__main__':
    app.run(debug=True)