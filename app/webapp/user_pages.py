from flask import Blueprint, render_template, request, abort, redirect, url_for, flash, current_app, session, jsonify, send_from_directory
import json
import os
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
import contentful
import traceback
import requests

user_pages = Blueprint('user_pages', __name__)

@user_pages.route('/')
def home():
    r = requests.get("http://api-cluster-ip-service:5050")
    return r.json()
