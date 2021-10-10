from flask import Flask , jsonify , abort , request
import models 
from models import Users
from flask_migrate import Migrate

## mail import 
from otp import generateOTP
from message_email import send_email
###

app= Flask(__name__)
db = models.setup_db(app)

migrate  = Migrate(app=app, db=db)

@app.route('/')
def index():
  return '<h2 style="color:blue ;">Hello from Heroku ;)</h2>'


### mail end point 



@app.route('/email', methods=['POST'])
def add_mail():
    is_valid_request()
    json_body = request.get_json()
    try:
        email = json_body['email'].lower()
        ## if user is here
        if email != Users.query.get(email) != None :                    
            return jsonify({
                "success":'false',
                'message':'user is already signed up'
            }) 
        # if not add the user to database
        user = Users(email= email, password=generateOTP())
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'success' : "true" ,
            'status_code':200
        })

    except :
        print('error happend while adding new user')
        abort(501)

## is valid request with json mail
def is_valid_request():
    json_body = request.get_json()
    if json_body == None or 'email' not in json_body:
        abort(400)
    

# check user if i the database
@app.route('/user', methods=['POST'])
def get_email():
    is_valid_request()    
    email = request.get_json()['email'].lower()
    try:
      # if user not found
      if Users.query.get(email) == None:        
        return jsonify({
                'message':'user not found'
            })

      # if not generate a password
      new_password = generateOTP()            
        # update user password in the database
      user = Users.query.get(email)
      user.password = new_password
      db.session.commit()

        # send mail with OTP 
      send_email(to = email, message=new_password)
      return jsonify({
            'message':'Check your email for password'            
        })
    except:    
      print('error while getting user')
      abort(501)

# is valid password auth json request  
def is_valid_password_request():
    json_body = request.get_json()
    if json_body == None or 'first_password' not in json_body or 'second_password' not in json_body or 'email' not in json_body:
        abort(400)


# email should verified before this end point

# email should verified before this end point
@app.route('/password', methods=['POST'])
def check_password():
    is_valid_password_request()
    ## retrive request json data
    first_password = request.get_json()['first_password']
    second_password = request.get_json()['second_password']
    email  = request.get_json()['email']
    try:
      if first_password != second_password:
            return jsonify({
                'success':False,
                'message':'make sure you the passwords are match'
            })
        # invalid password
      user = Users.query.get(email)
        
      if first_password != user.password :

        return jsonify({
                'status_code' : 401 ,
                'message' : 'wrong password ,  check your mail or try again',
                'success': False
            })

        ## valid user password
        ## update password with place holder     
        
      user.password = generateOTP()
      db.session.commit()
      return jsonify({
            'status_code':200,
            'success':True ,
            'message' : 'logged in successfully'
        })
    except:
      abort(501)

# end of mail end points 