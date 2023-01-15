from flask import Flask
from flask_restful import Api,Resource,abort
from flask_sqlalchemy import SQLAlchemy,Model

app=Flask(__name__)

#database
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.db"

api=Api(app)

class CityModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    temp=db.Column(db.String(100),nullable=False)
    weather=db.Column(db.String(100),nullable=False)
    people=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"City(name={name},temp={temp},weather={weather},people={people})"

db.create_all()

#mycity = {
#    1:{"name":"chon","weather":"hot","people":1500},
#    2:{"name":"rayong","weather":"cold","people":2000},
#    3:{"name":"bangkok","weather":"rain","people":5000},
#}

def notFoundCity(city_id):
    if city_id not in mycity:
        abort(404,message="Not found city")


class city(Resource):
    def get(self,city_id):
        notFoundCity(city_id)
        return mycity[city_id]

    def post(self):
        return {"data":"123"}


api.add_resource(city,"/city/<int:city_id>")

if __name__ == "__main__":
    app.run(debug=True)