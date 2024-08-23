from database import db
from models.customer import Customer 
from sqlalchemy import select
from utils.util import encode_token

def login(username,password): #login using unique info so we dont query mutiple users
    query = select(Customer).where(Customer.username == username)
    customer = db.session.execute(query).scalar_one_or_none()
    #query cust table for a customer with password and username

    if customer and customer.password == password:
        # if e have  a customer associated with username, validate the password
        auth_token = encode_token(customer.id,customer.role.role_name)

        response = {
            "status": "success",
            "message" : "Successfully Logged In",
            "auth_token" : auth_token
        }
        return response
    
    else:
        response = {
            "status" : "fail",
            "message" : "Invalid username or password"
        }
        return response 
    
    pass

def save(customer_data):
    new_customer = Customer(
        name = customer_data['name'],
        email  = customer_data['email'],
        password = customer_data['password'],
        phone = customer_data['phone'],
        username = customer_data['username'],
    )

    db.session.add(new_customer)
    db.session.commit()
    db.session.refresh(new_customer)
    return new_customer 

def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers