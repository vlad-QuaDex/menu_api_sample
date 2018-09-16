#!/usr/bin/python3

from flask import Flask, jsonify, render_template

from flask_restful import Resource, Api

from sqlalchemy import create_engine

import psycopg2

# Create DB connection engine
db_connect = create_engine('postgresql+psycopg2://user:password@hostname/database_name')

app = Flask(__name__)

api = Api(app)


    
class Resto_Menu(Resource):

    def get(self, restaurant_id):

        conn = db_connect.connect()

        # Execute DB query
        query = conn.execute("select * from restaurant where RestaurantId =%d "  %int(restaurant_id))

        result = {'menu': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}

        # Render template with variable menu that contains JSON representation of DB query
        
        return render_template("home.html", menu=jsonify(result))
    



api.add_resource(Resto_Menu, '/restaurant/<restaurant_id>/item') # Route_1


if __name__ == '__main__':

     app.run()

