from flask import Flask,redirect,url_for,request,render_template,make_response
app = Flask(__name__,template_folder='templates',static_folder='static')


@app.route("/")
def home():
	return render_template('home.html')

@app.route("/home")
def home_again():
	return render_template('home.html')


@app.route("/about_us")
def about_us():
	return("helo")

@app.route("/projects")
def projects():
	return("welcome")

@app.route("/data")
def data():
	return render_template('data.html')
 
@app.route("/data_collect", methods=['POST','GET'])
def data_collect():
	if (request.method=="POST"):
		c=request.form["gene"]
		return(c)
	return("failed")
	
if __name__ == '__main__':
    app.run(debug=True)