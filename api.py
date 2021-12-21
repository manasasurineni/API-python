#!/usr/bin/env python3
from flask import Flask, jsonify,request
from random import randint,seed
seed(5)

app = Flask(__name__) #We need to define app for our server

#Sample data
Data = [{'ID':randint(1,140),
         'name':'man',
         'year':'1996'},
        {'ID': randint(1,140),
         'name': 'vin',
         'year': '1992'},
        ]

@app.route('/',methods=['GET'])
def home():
    return 'Hello all'

@app.route('/Students',methods=['GET'])
def Students():
    #return Data
    return jsonify({'details':Data})

@app.route('/Students/ind/<ID>',methods=['GET'])
def ind(ID):
    for s in Data:
        if(str(s['ID'])==ID):
            print(s)
            student = s
            #return s

        #return 'Null'
    #return jsonify({'details': student})
    return student


@app.route('/Students/upd/<ID>',methods=['PUT'])
def upd(ID):
    for s in Data:
        if(str(s['ID'])==ID):
            student = s
            #print(s)

    if('ID' in request.json):
        print('Student already exists')
        #return 'Student already exists'
    if('name' in request.json):
        student['name'] = request.json['name']
        #return jsonify({"updated_student":student})
    if('year' in request.json):
        student['year'] = request.json['year']
        #return jsonify({"updated_student": student})
    return jsonify({"updated_student": student})

@app.route('/Students/add',methods=['POST'])
def add():
    Student = {'ID':randint(1,140), #request.json['ID'],
         'name': request.json['name'],
         'year':request.json['year']}
    Data.append(Student)
    #return Data
    #return jsonify({'details': Data}) #All the student details shown
    return Student #Just created data is shown

@app.route('/Students/rem/<ID>',methods=['DELETE'])
def remove(ID):
    for s in Data:
        if str(s['ID'])==ID:
            student = s
            #po
    if (student != 'Null'):
        Data.remove(student)
        #Data.pop(Student)
    return jsonify({'Deleted detail':student})
    #return 'Data removed for given ID'

if __name__ == "__main__":
    app.run(debug=True)





