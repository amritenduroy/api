import sqlite3
from flask_restful import Resource
from flask_jwt import JWT, jwt_required


class Book(Resource):
    @jwt_required()
    def get(self, isbn):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        sql = 'SELECT * FROM books WHERE isbn =?'
        result = c.execute(sql, (isbn,))
        record = result.fetchone()
        if record:
            result = {
                'Title': record[1],
                'Author': record[2],
                'Average_Rating': record[3],
                'ISBN': record[4],
                'ISBN13': record[5],
                'Language_Code': record[6],
                'Number_Of_Pages': record[7],
                'Rating_Counts': record[8],
                'Text_Reviews_Counts': record[9]
            }
            return result, 200
        conn.close()
        return {
            'message': 'No records corresponding to the ISBN %s'%(isbn,)
        }, 400

