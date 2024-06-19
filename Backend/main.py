from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.staticfiles import StaticFiles
import os
from typing import Annotated
from pydantic import BaseModel
import jwt
import sqlite3
import json
from fastapi.middleware.cors import CORSMiddleware
import string
import random
from datetime import date, datetime, time, timedelta
import io

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class User(BaseModel):
    email: str
    password: str

class Email(BaseModel):
    email:str

class Company(BaseModel):
    company: int

class Review(BaseModel):
    user: int
    date: str
    text: str
    type: str
    id_objet: str

class UserType(BaseModel):
    email: str
    password: str
    type: str

class Id(BaseModel):
    id: int

class AuthUser(BaseModel):
    accessToken: str
    email: str
    password: str

class AuthUserID(BaseModel):
    accessToken: str
    email: str
    password: str
    id: int

class UserUpdater(BaseModel):
    id: int
    name: str
    surname: str
    burthday: datetime
    phone: str
    email: str
    vk: str
    insta: str
    telegram: str
    password: str
    pic: UploadFile = File(...)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

try:
    con = sqlite3.connect('Yuliana_diplom.db')
    cursor = con.cursor()
    print('Connected')
except sqlite3.Error as error:
    print('Error', error)

@app.post("/sendcode")
async def setsendCode(email:Email):

    code = id_generator()
    print("Код подтверждения:" + code)
    result = []

    d = {}

    d["code"] = code
    result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.get("/complexes")
async def getComplexesList():

    #complexes = cursor.execute(f"SELECT name, type FROM complexes").fetchall()
    rows = cursor.execute(f"SELECT * FROM complexes").fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(result,ensure_ascii=False)
    return json.loads(json_result)

@app.get("/abons")
async def getAbonsList():

    #complexes = cursor.execute(f"SELECT name, type FROM complexes").fetchall()
    rows = cursor.execute(f"SELECT * FROM abonaments").fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(result,ensure_ascii=False)
    return json.loads(json_result)

@app.post("/login")
async def getAuthStatus(user: User):

    sql = "SELECT id, email, password FROM users WHERE email = ?"

    cursor.execute(sql, (user.email,))

    row = cursor.fetchone()

    result = []
    d = {}
    if str(row[2]) == user.password:
        encoded_jwt = jwt.encode({str(row[0]): "payload"}, "secret", algorithm="HS256")
        d["accessToken"] = encoded_jwt
        #d["auth_success"] = True
    #else:
        #d["auth_success"] = False
    d["email"] = row[1]
    d["password"] = row[2]

    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getUserData")
async def getUserData(user: AuthUser):

    sql = "SELECT * FROM users WHERE email = ?"

    cursor.execute(sql, (user.email,))

    row = cursor.fetchone()
    d = {}
    for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
    print(d)
    return d

@app.post("/getComplexData")
async def getComplexData(id: Id):

    sql = "SELECT * From complexes WHERE id = ?"

    cursor.execute(sql, (int(id.id),))

    row = cursor.fetchone()

    result = []
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.get("/trainers")
async def getTrainersList():

    rows = cursor.execute(f"SELECT * FROM trainer").fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(result,ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getTrainerData")
async def getTrainerData(id: Id):

    sql = "SELECT * From trainer WHERE id = ?"

    cursor.execute(sql, (int(id.id),))

    row = cursor.fetchone()

    result = []
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getTrainerFullNameById")
async def getTrainerFullNameById(id: Id):

    sql = "SELECT name, surname From trainer WHERE id = ?"

    cursor.execute(sql, (int(id.id),))

    row = cursor.fetchone()

    result = []
    d = {}

    d["name"] = row[0]
    d["surname"] = row[1]
    result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getUserAbons")
async def getUserAbons(user: AuthUser):

    sql = "SELECT id FROM users WHERE email = ?"

    cursor.execute(sql, (user.email,))

    row = cursor.fetchone()

    userId = row[0]

    sql = "SELECT abonament, status FROM owns WHERE user = ?"
    cursor.execute(sql, (userId,))
    rows = cursor.fetchall()
    result = []
    for row in rows:
        sql = "SELECT * FROM abonaments WHERE id = ?"
        cursor.execute(sql, (row[0],))
        rows_deep = cursor.fetchall()
        for row_deep in rows_deep:
            d = {}
            d["status"] = row[1]
            for i, col in enumerate(cursor.description):
                d[col[0]] = row_deep[i]

            result.append(d)

    json_result = json.dumps(result, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getAbonData")
async def getAbonData(id: Id):

    sql = "SELECT * From abonaments WHERE id = ?"

    cursor.execute(sql, (int(id.id),))

    row = cursor.fetchone()

    result = []
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getOwnData")
async def getOwnData(id: Id):

    sql = "SELECT * From owns WHERE abonament = ?"

    cursor.execute(sql, (int(id.id),))

    row = cursor.fetchone()

    result = []
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getComplexAbons")
async def getComplexAbons(id: Id):

    sql = "SELECT id FROM complexes WHERE id = ?"

    cursor.execute(sql, (id.id,))

    row = cursor.fetchone()

    complexId = row[0]

    sql = "SELECT * FROM abonaments WHERE complex = ?"
    cursor.execute(sql, (complexId,))
    rows = cursor.fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        result.append(d)

    json_result = json.dumps(result, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getTrainerAbons")
async def getTrainerAbons(id: Id):

    sql = "SELECT id FROM trainer WHERE id = ?"

    cursor.execute(sql, (id.id,))

    row = cursor.fetchone()

    complexId = row[0]

    sql = "SELECT * FROM abonaments WHERE trainer = ?"
    cursor.execute(sql, (complexId,))
    rows = cursor.fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        result.append(d)

    json_result = json.dumps(result, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/reservabon")
async def reservAbon(user: AuthUserID):

    sql = "SELECT id FROM users WHERE email = ?"

    cursor.execute(sql, (user.email,))

    row = cursor.fetchone()

    userId = row[0]

    sql = "INSERT INTO owns (abonament, user, status) VALUES (?, ?, ?)"
    cursor.execute(sql, (user.id,userId,"wait"))
    con.commit()

@app.post("/freezeabon")
async def freezeAbon(user: AuthUserID):

    sql = "SELECT id FROM users WHERE email = ?"

    cursor.execute(sql, (user.email,))

    row = cursor.fetchone()

    userId = row[0]

    sql = "UPDATE owns SET status = 'freezed' WHERE abonament = ? AND user = ? AND status = 'active'"
    cursor.execute(sql, (user.id,userId))
    con.commit()

    result = []
    d = {}

    d["status"] = 'freezed'
    result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/unfreezeabon")
async def unfreezeAbon(user: AuthUserID):
        sql = "SELECT id FROM users WHERE email = ?"

        cursor.execute(sql, (user.email,))

        row = cursor.fetchone()

        userId = row[0]

        sql = "UPDATE owns SET status = 'active' WHERE abonament = ? AND user = ? AND status = 'freezed'"
        cursor.execute(sql, (user.id, userId))
        con.commit()

@app.get("/complexes")
async def getComplexesList():

    #complexes = cursor.execute(f"SELECT name, type FROM complexes").fetchall()
    rows = cursor.execute(f"SELECT * FROM complexes").fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(result,ensure_ascii=False)
    return json.loads(json_result)

@app.post("/createuser")
async def createuser():

    #complexes = cursor.execute(f"SELECT name, type FROM complexes").fetchall()
    rows = cursor.execute(f"SELECT * FROM complexes").fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(result,ensure_ascii=False)
    return json.loads(json_result)

@app.post("/registrate")
async def registrate(user: User):

    sql = "INSERT INTO users (email, password) VALUES ( ?,?)"
    cursor.execute(sql, (user.email,user.password))
    con.commit()

@app.post("/cancelabon")
async def cancelabon(user: AuthUserID):
        sql = "SELECT id FROM users WHERE email = ?"

        cursor.execute(sql, (user.email,))

        row = cursor.fetchone()

        userId = row[0]

        sql = "UPDATE owns SET status = 'canceled' WHERE abonament = ? AND user = ?"
        cursor.execute(sql, (user.id,userId))
        con.commit()

@app.post("/extendabon")
async def extendabon(user: AuthUserID):
        sql = "SELECT id FROM users WHERE email = ?"

        cursor.execute(sql, (user.email,))

        row = cursor.fetchone()

        userId = row[0]

        sql = "UPDATE owns SET status = 'active' WHERE abonament = ? AND user = ? AND status = 'ended'"
        cursor.execute(sql, (user.id,userId))
        con.commit()

@app.post("/updateProfile")
async def updateProfile(name: Annotated[str, Form()],surname: Annotated[str, Form()],id: Annotated[str, Form()],phone: Annotated[str, Form()],burthday: Annotated[date, Form()],pic: Annotated[UploadFile, File()]):
    print(pic)
    picFile = await pic.read()
    userpath = 'yulianakostikova'
    serverpath = '/uploads/users/'+userpath+'/logo.png'
   # os.mkdir('/uploads')
   # os.mkdir('/uploads/users/')
   # os.mkdir('/uploads/users/' + userpath)
    with open(serverpath, "wb") as binary_file:
        binary_file.write(picFile)
    app.mount('/uploads', StaticFiles(directory='/uploads'), name="uploads")
    fullpath = 'http://127.0.0.1:8000' + serverpath

    sql = "UPDATE users SET name = ?, surname = ?, phone = ?, burthday = ?, pic = ? WHERE id = ?"
    print(name)
    cursor.execute(sql, (name, surname, phone, burthday, fullpath, id))
    con.commit()
    return True

@app.post("/getComplexReviews")
async def getComplexReviews(id: Id):

    sql = "SELECT id FROM complexes WHERE id = ?"

    cursor.execute(sql, (id.id,))

    row = cursor.fetchone()

    complexId = row[0]

    sql = "SELECT * FROM reviews  JOIN users ON users.id = reviews.user WHERE reviews.type = 'complex' AND reviews.id_object = ?"
    cursor.execute(sql, (complexId,))
    rows = cursor.fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        result.append(d)

    json_result = json.dumps(result, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/createReview")
async def createReview(review: Review):
    print(review)
    sql = "INSERT INTO reviews (text, user, date, type, id_object) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (review.text,review.user,review.date,review.type,review.id_objet))
    con.commit()

    sql = "SELECT id FROM reviews WHERE text = ? AND user = ? AND date = ? AND type = ? AND id_object = ?"
    cursor.execute(sql, (review.text, review.user, review.date, review.type, review.id_objet))
    row = cursor.fetchone()
    result = []
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getControlData")
async def getUserAbons(user: AuthUser):

    sql = "SELECT id FROM users WHERE email = ?"

    cursor.execute(sql, (user.email,))

    row = cursor.fetchone()

    userId = row[0]

    sql = "SELECT abonament, status FROM owns WHERE user = ?"
    cursor.execute(sql, (userId,))
    rows = cursor.fetchall()
    allcount = len(rows)

    sql = "SELECT abonament, status FROM owns WHERE user = ? AND status = 'active'"
    cursor.execute(sql, (userId,))
    rows = cursor.fetchall()
    activecount = len(rows)

    sql = "SELECT abonament, status FROM owns WHERE user = ? AND status = 'freezed'"
    cursor.execute(sql, (userId,))
    rows = cursor.fetchall()
    freezedcount = len(rows)

    sql = "SELECT abonament, status FROM owns WHERE user = ? AND status = 'ended' OR status = 'canceled'"
    cursor.execute(sql, (userId,))
    rows = cursor.fetchall()
    endedcount = len(rows)

    result = []

    d = {}
    d["allcount"] = allcount
    d["activecount"] = activecount
    d["freezedcount"] = freezedcount
    d["endedcount"] = endedcount
    result.append(d)

    json_result = json.dumps(d, ensure_ascii=False)
    return json.loads(json_result)

@app.post("/getRequestsAbons")
async def RequestsAbons(company: Company):

    sql = "SELECT id FROM abonaments WHERE complex = ?"

    cursor.execute(sql, (company.company,))

    row = cursor.fetchall()

    userId = row[0]

    sql = "SELECT abonament, status FROM owns WHERE user = ?"
    cursor.execute(sql, (userId,))
    rows = cursor.fetchall()
    result = []
    for row in rows:
        sql = "SELECT * FROM abonaments WHERE id = ?"
        cursor.execute(sql, (row[0],))
        rows_deep = cursor.fetchall()
        for row_deep in rows_deep:
            d = {}
            d["status"] = row[1]
            for i, col in enumerate(cursor.description):
                d[col[0]] = row_deep[i]

            result.append(d)

    json_result = json.dumps(result, ensure_ascii=False)
    return json.loads(json_result)