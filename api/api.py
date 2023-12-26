# python packages
import os

# utilities
from .utils import connection_db, is_correct_url

# 3rd party packages
from flask import Flask, request, redirect
from flask_restful import Resource, Api
from dotenv import load_dotenv
from hashids import Hashids


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
api = Api(app)
load_dotenv()
hashids = Hashids(min_length=8, salt=str(os.getenv("SECRET_KEY")))


class UrlShortenerAPI(Resource):
    def post(self):
        # database connection config
        cnx = connection_db()
        data = request.get_json()
        long_url = data["longUrl"]

        if long_url:
            is_url = is_correct_url(long_url)
            if is_url is True and cnx.is_connected():
                # insert to db
                cursor = cnx.cursor()
                cursor.execute(
                    "INSERT INTO url_table" "(long_url)" "VALUES (%s)", (long_url,)
                )
                cnx.commit()
                # and make short url
                id = cursor.lastrowid
                hashid = hashids.encode(id)
                short_url = request.host_url + hashid
                # close database connection & cursor obj
                cursor.close()
                cnx.close()
                return {
                    "Message": "Data posted to db, connection closed",
                    "short_url": short_url,
                }

            else:
                cnx.close()
                return {
                    "error": "Your db connection failed or try to provide correct url address",
                    "status_code": 400,
                }

    def get(self, id):
        # decode encoded hash and retrieve object id
        decoded_id_tuple = hashids.decode(id)
        decoded_id = decoded_id_tuple[0]

        # database connection config
        cnx = connection_db()
        cursor = cnx.cursor()
        cursor.execute("SELECT long_url FROM url_table WHERE id = (%s)", (decoded_id,))

        data = cursor.fetchone()
        cursor.close()
        cnx.close()

        # in case JSON needed
        # return {"original_url": data[0]}
        return redirect(data[0])


api.add_resource(UrlShortenerAPI, "/api/post-org-url", "/<id>")


if __name__ == "__main__":
    app.run(debug=True)
