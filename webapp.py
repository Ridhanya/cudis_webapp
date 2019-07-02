from flask import Flask,redirect,url_for,request,render_template,make_response
from flask_mysqldb import MySQL
app = Flask(__name__,template_folder='templates',static_folder='static')
mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'Ridhanya'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jasrid22'
app.config['MYSQL_DATABASE_DB'] = 'cudis'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


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
		#mysql=MySQL(app)
		#app.config['MYSQL_DATABASE_USER'] = 'Ridhanya'
		#app.config['MYSQL_DATABASE_PASSWORD'] = 'jasrid22'
		#app.config['MYSQL_DATABASE_DB'] = 'cudis'
		#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
		#mysql.init_app(app)






		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("SELECT * from gene where genename='c'")
		data=cursor.fetchone()
		return(data)
		
	return("failed")
	
if __name__ == '__main__':
    app.run(debug=True)