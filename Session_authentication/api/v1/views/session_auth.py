#!/usr/bin/env python3
""" Session Authentication view """

from flask import Blueprint, request, jsonify, make_response, abort
from models.user import User
import os

session_auth = Blueprint('session_auth', __name__)

@session_auth.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """ POST /api/v1/auth_session/login : Login route for session auth """

    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email.strip() == "":
        return jsonify({"error": "email missing"}), 400

    if not password or password.strip() == "":
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Importer auth ici pour éviter les imports circulaires
    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    response = make_response(user.to_json())
    session_name = os.getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response

@session_auth.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def session_logout():
    """ DELETE /api/v1/auth_session/logout : Logout route for session auth """
    from api.v1.app import auth  # Import ici pour éviter les imports circulaires
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
