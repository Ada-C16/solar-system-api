from flask import Blueprint, jsonify


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
