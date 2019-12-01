from flask import Flask,redirect,url_for,request,render_template,make_response
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
import cx_Oracle
import sqlite3 as sql
app = Flask(__name__,template_folder='templates',static_folder='static')
database="C:\\sqlite\\cudis.db"

"""mysql = MySQL(app)
#app = Flask(__name__,template_folder='templates',static_folder='static')
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "test"
app.config['MYSQL_DATABASE_HOST'] = "127.0.0.1"
mysql.init_app(app)
#mysql = MySQL(app)"""


"""dsn_tns = cx_Oracle.makedsn('DESKTOP-V5J66MT', '1521', service_name='XE') 
conn = cx_Oracle.connect(user='SYSTEM', password='SBTNITC', dsn=dsn_tns)"""


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
	#curr=mysql.connection.cursor()
	if (request.method=="POST"):
		inptext=request.form["gene"]
		con = sql.connect(database)
		con.row_factory =sql.Row
		cur=con.cursor()
		cur.execute("select * from MITO where gene=?",(inptext,))
		row=cur.fetchall()
        
		#mysql=MySQL(app)
		#app.config['MYSQL_DATABASE_USER'] = 'Ridhanya'
		#app.config['MYSQL_DATABASE_PASSWORD'] = 'jasrid22'
		#app.config['MYSQL_DATABASE_DB'] = 'cudis'
		#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
		#mysql.init_app(app)
		"""c = conn.cursor()
		c.execute('select * from XE.test where GENE=inptext')
		for row in c:
			print(row[0], '-', row[1])"""






		"""conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  emp values(c)")
		data=cursor.fetchone()
		return(c)"""
		#print(row)
		#print("success")
		return render_template("list.html",row = row)
		
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

@app.route("/pradeep")
def pradeep():
	return render_template('pradeep.html')

@app.route("/sairam")
def sairam():
	return render_template('sairam.html')

@app.route("/ridhanya")
def ridhanya():
	return render_template('ridhanya.html')

@app.route("/angela")
def angela():
	return render_template('angela.html')
@app.route("/anubhav")
def anubhav():
	return render_template('anubhav.html')
@app.route("/himanshu")
def himanshu():
	return render_template('himanshu.html')

@app.route("/raidha")
def raidha():
	return render_template('raidha.html')

@app.route("/drrajanikanth")
def drrajinikanth():
	return render_template('rajanikanth.html')

	
if __name__ == '__main__':
    #app.run(debug=True)
     app.run(host='127.0.0.1',port='3307')