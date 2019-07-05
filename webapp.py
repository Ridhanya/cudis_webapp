from flask import Flask,redirect,url_for,request,render_template,make_response
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
app = Flask(__name__,template_folder='templates',static_folder='static')

mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'Ridhanya'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jasrid22'
app.config['MYSQL_DATABASE_DB'] = 'cudis'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'anemia.fever@gmail.com'
app.config['MAIL_PASSWORD'] = 'sreemundra2216'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/home")
def home_again():
	return render_template('home.html')


@app.route("/about_us")
def about_us():
	return render_template('about_us.html')

@app.route("/contact_us")
def contact_us():
	return render_template('contact_us.html')

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
@app.route("/result_contact", methods=['POST','GET'])
def result_contact():
	if(request.method=="POST"):
		v_name=request.form["name"]
		v_email=request.form["email"]
		v_comments=request.form["comments"]
		o_email="anemia.fever@gmail.com"
		msg=Message('viewers_comments',sender=v_email,recipients=[o_email])
		msg.body="The comment is %s and Name of the viewer is %s and email address is %s" %(str(v_comments),str(v_name),str(v_email))
		mail.send(msg)
		return render_template("result_success_contact.html")
	return render_template("result_failure_contact")
	
if __name__ == '__main__':
    app.run(debug=True)