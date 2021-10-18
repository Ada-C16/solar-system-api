from flask import Blueprint, jsonify

planets_bp = Blueprint("planets_bp", __name__,url_prefix="/planets")
