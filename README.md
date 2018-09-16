# menu_api_sample
Python-flask application that reads restaurant menu data from PostgreSQL and serving it to web app. SQLAlchemy and flask_restful frameworks provide the desired database and API functionality. 

The creates engine for a PostgreSQL database. The connection parameters are to be provided. Ideally, it should be done via configuration file.

db_connect = create_engine('postgresql+psycopg2://user:password@hostname/database_name')

The following line provides routing to the desired resource location (i.e.: /restaurant/:restaurantId/item).

api.add_resource(Resto_Menu, '/restaurant/<restaurant_id>/item')

Class Resto_Menu carries out the connection to database, queries the specified route for a menu list. It organizes the response of the query into python dictionary. The “result” dictionary is converted to JSON format.

Note: the data structure of the database table is not known. It's assumed that the query will return all menu items for a restaurant specified by Restairant Id. Creation of “result” python dictionary from  query needs to be researched and developed further based on the DB data structure. The data is assumed to be both nested and hierarchical; hence an efficient parsing of data needs to be designed to avoid too many recursive calls to a function



