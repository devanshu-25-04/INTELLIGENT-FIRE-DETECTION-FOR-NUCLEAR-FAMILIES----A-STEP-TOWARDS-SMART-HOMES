import pymongo
client = pymongo.MongoClient("MONGO DB API")
db = client["clients"]
details=db["details"]
def validate(username,password,ID):
    user=details.find_one({'username':username},{"_id":1,"username":1,"password":1})
    msg=''
    id=''
    if user==None:
        msg="User does not exist"
    else:
        print(user)
        if user['password']!=password:
            msg="Wrong password, Try again"
        else:
            msg="Successfully logined"
            details.update_one({"username":username},{'$push':{"clientId":ID}},upsert=True)
    return msg


def sensorReading(id):
    msg=''
    try:
        users=details.find({},{"clientId":1,"Temperature":1,"Flame":1,"Gas":1,"Humidity":1})
        for user in users:
            for i in user['clientId']:
                if i==id:
                    print(user)
                    print(user['Te'])
                    t=user["Temperature"]
                    f=user["Flame"]
                    g=user["Gas"]
                    h=user["Humidity"]
                    msg="Temperature = " + t +" \nHumidity = "+h+"\nFlame="+f+"\nGas="+g
    except:          
        msg="Try Again"
    return msg
                
