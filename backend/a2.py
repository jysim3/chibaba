'''
COMP9321 2019 Term 1 Assignment Two Code Template
Student Name: Jie Shang
Student ID: 5153884
'''

import sqlite3
from sqlite3 import Error
import requests
import json 
import datetime,re
from flask import Flask
from flask import request
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_restplus import inputs
from flask_restplus import reqparse

def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        create_table_0 = """CREATE TABLE worldbank_table(
                                        collection_id int,
                                        indicator text ,
                                        indicator_value text,
                                        creation_time time
                                    ); """
        create_table_1 = """CREATE TABLE entries_table(
                                        collection_id int,
                                        country text ,
                                        year text ,
                                        value real
                                        collection_id integer references worldbank(collection_id)
                                    ); """

        cur = conn.cursor()
        cur.execute(create_table_0)
        conn.commit()
        cur.execute(create_table_1)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
    pass


app = Flask(__name__)
api = Api(app)

# Question 1 and Question 3
indicator_model = api.model('indicator_id', {'indicator_id': fields.String})

@api.route('/collections')
class worldbank(Resource):
    @api.response(200, 'OK')
    @api.response(404, "Not Found")
    @api.response(201,'Created')
    @api.expect(indicator_model, validate=True)
    def post(self):
        indicator_id = request.json['indicator_id']
        URL = "http://api.worldbank.org/v2/countries/all/indicators/" + indicator_id + "?date=2013:2018&format=json&per_page=100"

        data_api = requests.get(URL)
        data_json = data_api.json()
        # print(data_json)
        try:
            conn = sqlite3.connect('data.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        data_dic = {}

        cur.execute("SELECT max(collection_id) FROM worldbank_table")
        conn.commit()
        res = cur.fetchone()
        if res[0] != None:
            data_dic['collection_id'] = res[0] + 1
        else:
            data_dic['collection_id'] = 0 
        
        entries_list = []
        entries_dict_list = []
        
        for row in data_json[1]:
            entries_list.append((data_dic['collection_id'], row['country']['value'], row['date'], row['value']))
            entries_dict_list.append({'country':row['country']['value'], 'date':row['date'], 'value': row['value']}) #TODO

            data_dic["indicator"] = row['indicator']['id']
            data_dic["indicator_value"] = row['indicator']['value']
        
        data_dic["creation_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_dic["entries"] = entries_dict_list

        dict = {}
        cur.execute("INSERT INTO worldbank_table VALUES (?,?,?,?)", (data_dic['collection_id'], data_dic["indicator"], data_dic["indicator_value"],data_dic["creation_time"]))
        conn.commit()
        result1 = cur.fetchall()
        [dict[row] for row in result1]

        cur.executemany("INSERT INTO entries_table VALUES (?,?,?,?)", entries_list)
        conn.commit()
        result2 = cur.fetchall()
        [dict[row] for row in result2]
        return_dic = {}
        return_dic['location'] = "/<collections>/"+str(data_dic['collection_id'])
        return_dic['collection_id'] = str(data_dic['collection_id'])
        return_dic['creation_time'] = data_dic["creation_time"]
        return_dic['indicator'] = data_dic['indicator']
        return return_dic, 201 

    def get(self):
        try:
            conn = sqlite3.connect('data.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * FROM worldbank_table")
        conn.commit()
        result = cur.fetchall()
        dict_result = {}
        ll_result = []
        if result[0]:
            for i in result:
                temp_dict = {}
                temp_dict["location"] = "/<collections>/" + str(i[0])
                temp_dict['collection_id'] = i[0]
                temp_dict['creation_time'] = i[3]
                temp_dict['indicator'] = i[1]
                ll_result.append(temp_dict)
            return ll_result,200  
        else:
            return {'message': "Collection is empty"}, 404


## Question 2 and Question 4
@api.doc(params={'collection_id': 'Please input a collection_id'})
@api.route('/collections/<int:collection_id>')
class delete_id(Resource):
    @api.response(200, 'OK')
    @api.response(404, "Not Found")
    def delete(self, collection_id):
        try:
            conn = sqlite3.connect('data.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM worldbank_table WHERE collection_id == {collection_id}")
        result = cur.fetchall()
        if result:
            cur.execute(f"DELETE FROM worldbank_table WHERE collection_id == {collection_id}")
            conn.commit()
            cur.execute(f"DELETE FROM entries_table WHERE collection_id == {collection_id}")
            conn.commit()
            return {'message': f"Collection = {collection_id} is removed from the database!"}, 200
        else:
            return {'message': f"Collection = {collection_id} doesn't exist"}, 404

    def get(self, collection_id):
        try:
            conn = sqlite3.connect('data.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM worldbank_table WHERE collection_id == {collection_id}")
        conn.commit()
        result1 = cur.fetchall()

        cur.execute(f"SELECT * FROM entries_table WHERE collection_id == {collection_id}")
        conn.commit()
        result2 = cur.fetchall()
        entry_list = []
        if result1 and result2:
            for i in result2:
                temp_dict = {}
                temp_dict["country"] = i[1]
                temp_dict["date"] = i[2]
                temp_dict["value"] = i[3]
                entry_list.append(temp_dict)

            dict_result = {}
            dict_result["collection_id"] = result1[0][0]
            dict_result["indicator"] = result1[0][1]
            dict_result["indicator_value"] = result1[0][2]
            dict_result["creation_time"] = result1[0][3]


            dict_result["entries"] = entry_list
            return dict_result,200
        else:
            return {'message': f"Collection = {collection_id} doesn't exist"}, 404

## Question 5
@api.route('/collections/<int:collection_id>/<int:year>/<string:country>')
@api.doc(params={'collection_id': 'Please input a collection_id', 'year':'Choose a year from 2013 to 2018', 'country': 'Please nput a country name with " " '})
class economic_indicator(Resource):
    @api.response(200, 'OK')
    @api.response(404, "Not Found")
    def get(self, collection_id,year,country):
        try:
            conn = sqlite3.connect('data.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM entries_table WHERE collection_id == {collection_id} AND year == {year} AND country == {country}")
        conn.commit()
        result1 = cur.fetchall()

        cur.execute(f"SELECT indicator FROM worldbank_table WHERE collection_id == {collection_id}")
        conn.commit()
        result2 = cur.fetchone()
        ind_id = result2[0]

        cur.execute(f"SELECT indicator_value FROM worldbank_table WHERE collection_id == {collection_id}")
        conn.commit()
        result3 = cur.fetchone()
        ind_value = result3[0]
        # print(result1)

        if result1:
            dict_result = {}
            dict_result["collection_id"] = result1[0][0]
            dict_result["indicator_id"] = ind_id
            dict_result["country"] = result1[0][1]
            dict_result["year"] = result1[0][2]
            dict_result["value"] = result1[0][3]
            return dict_result,200
        else:
            return {'message': f"year {year} or country {country} not found in collection_id {collection_id}."}, 404

## Question 6

parser_query = reqparse.RequestParser()
parser_query.add_argument('query')

@api.doc(params={'collection_id': 'Please input a collection_id', 'year':'Choose a year from 2013 to 2018'})
@api.doc(params={'query': 'Optional, you can enter: topN or bottomN,N an integer which between 0 and 100'})
@api.route('/collections/<int:collection_id>/<int:year>')
class economic_indicator(Resource):
    @api.expect(parser_query, validate=True)
    @api.response(200, 'OK')
    @api.response(404, "Not Found")

    def get(self, collection_id, year):
        args = parser_query.parse_args()
        query = args.get('query')
        if not query:
            index = 2
        else:
            if 'top' in query:
                # print(query,type(query))
                query = re.sub(r"top", " ",query)
                index = 1
            else:
                query = re.sub(r'bottom', "", query)
                index = 0

        # if index != 2 and (not query.isdigit() or int(query) > 100 or int(query) == 0):
        #     index = 2

        try:
            conn = sqlite3.connect('data.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM entries_table WHERE collection_id == {collection_id} AND year == {year}")
        conn.commit()
        result1 = cur.fetchall()

        cur.execute(f"SELECT indicator FROM worldbank_table WHERE collection_id == {collection_id}")
        conn.commit()
        result2 = cur.fetchone()
        ind_id = result2[0]

        cur.execute(f"SELECT indicator_value FROM worldbank_table WHERE collection_id == {collection_id}")
        conn.commit()
        result3 = cur.fetchone()
        ind_value = result3[0]

        result_list = []
        whole_dict = {}
        for row in result1:
            dict_unsorted = {}
            dict_unsorted["collection_id"] = row[0]
            dict_unsorted["indicator_id"] = ind_id
            dict_unsorted["country"] = row[1]
            dict_unsorted["year"] = row[2]
            dict_unsorted["value"] = row[3]
            whole_dict[row[3]] = dict_unsorted

        sort_list = sorted(whole_dict.items())
        # print(sort_list)
      
        dict_result = {}
        entries_list = []
        if index == 1:
            num = int(query)
            for i in sort_list[:num-1]:
                entries_dic = {}
                entries_dic['country'] = i[1]['country']
                entries_dic['date'] = i[1]['year']
                entries_dic['value'] = i[1]['value']
                entries_list.append(entries_dic) 

            dict_result['indicator'] = ind_id
            dict_result['indicator_value'] = ind_value
            dict_result['entries'] = entries_list
            return dict_result, 200

        elif index == 0:
            num = int(query)
            for i in sort_list[-(num-1):]:
                entries_dic = {}
                
                entries_dic['country'] = i[1]['country']
                entries_dic['date'] = i[1]['year']
                entries_dic['value'] = i[1]['value']
                entries_list.append(entries_dic) 

            dict_result['indicator'] = ind_id
            dict_result['indicator_value'] = ind_value
            dict_result['entries'] = entries_list
            return dict_result, 200

        elif index == 2:
            for i in sort_list:
                entries_dic = {}
                entries_dic['country'] = i[1]['country']
                entries_dic['date'] = i[1]['year']
                entries_dic['value'] = i[1]['value']
                entries_list.append(entries_dic) 

            dict_result['indicator'] = ind_id
            dict_result['indicator_value'] = ind_value
            dict_result['entries'] = entries_list
            return dict_result, 200

if __name__ == '__main__':
    create_db('data.db')
    app.run(debug=True)

'''
Put your API code below. No certain requriement about the function name as long as it works.
'''


