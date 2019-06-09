from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from config import run_config

app = Flask(__name__)

app.config.from_object(run_config())

api = Api(app)

class HelloRest(Resource):
    def get(self):
        return {"key1": "value"}, 200, {"customs_header": "header_value"}
    def post(self):
      return "post"

a = ["Apple", "Amazon", "Alphabet", "Microsoft"]

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("page", type=int, help="wrong page")
# сюда можно добавлять location ( откуда парсер будет брать аргументы  на проверку.


# Наследование от parser:
# можно добавлять новые аргументы, удалять из родительского или их менять.
parser_2 = parser.copy()
parser_2.add_argument("value")
parser.add_argument("chapter", type=int, help="wrong chapter")


class Companies(Resource):
    def get(self):
        args = parser.parse_args(strict=True)
        response = dict()
        print(args)
        for i, element in enumerate(a):
            response[i+1] = element
        return response
    def post(self, value):    # элемент добавляется через url.
        a.append(value)
        return "Element added successfully"

    def put(self):
        # request.data -  данные, которые будут перед-ся в запросе в виде json dict with keys company and positon.
        # данные передаются in body of request ( see postman)
        import json
        data = json.loads(request.data) # превращаем json в словарь.
        company = data.get("company")
        position = data.get("position") - 1
        a.remove(company)
        a.insert(position, company)
        return "List updated successfully"

    def delete(self, value):
        a.remove(value)
        return "Element deleted successfully"



api.add_resource(HelloRest, "/")
api.add_resource(Companies, "/companies", "/companies/<value>")

if __name__ == '__main__':
    app.run(debug=True)
