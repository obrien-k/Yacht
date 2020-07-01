from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app.decorators import admin_required

from app.models import EditableHTML
import docker
import socket

main = Blueprint('main', __name__)


@main.route('/')
def index():
    dclient=docker.from_env()
    hostname=socket.gethostname()
    host_ip=socket.gethostbyname(hostname)
    return render_template('main/index.html', **locals())

