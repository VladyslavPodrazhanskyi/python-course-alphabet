from flask import Blueprint
from flask_restful import Api
from app_blueprint.trees.main import Main
trees = Blueprint("trees", __name__)

api = Api(trees)

api.add_resource(Main, "/")