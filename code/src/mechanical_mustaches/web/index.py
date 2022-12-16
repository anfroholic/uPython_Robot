import mechanical_mustaches as mm
from mechanical_mustaches import m
import mechanical_mustaches.web.picoweb as picoweb
import mechanical_mustaches.web.ulogging as logging
import json
import esp32
import uasyncio
import config
logging.basicConfig(level=logging.INFO)

import mechanical_mustaches.web.repl as repl
import mechanical_mustaches.web.stacheboard as stacheboard
import mechanical_mustaches.web.editor as editor

site = picoweb.WebApp(__name__)

errors_checked_for = False
errors = ''


@site.route("/")
@site.route("/home")
def index(req, resp):
    global errors_checked_for
    global errors
    if not errors_checked_for:
        with open('/mechanical_mustaches/web/errors.log', 'r') as f:
            errors = f.read().replace('\n', '<br>')
    
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"""
<!DOCTYPE html><html><head><title>Mo's Mayhem</title><style>{mm.send_file("mustache.css")}</style></head><body>
{mm.send_file("header.html")}



<h1 style="font-size:40px">Mo</h1><p style="font-size:20px; color: #FFFFFF;">by: The Mechanical Mustaches</p>{errors}
<img src='mechanical_mustaches/web/static/mm_logo.png'style="width: 150px;"></img><br>
<img src='mechanical_mustaches/web/static/FIRST_Horz_RGB.png' style="width: 150px;" /></img><br></body><html><br>
FIRST® Robotics Team 8122<br>
<p style="font-size:8px">FIRST ® , the FIRST® logo, FIRST ® Robotics Competition, and FIRST ® Tech Challenge, are registered
trademarks of FIRST ® (<a href="http://www.firstinspires.org">www.firstinspires.org</a>) which is not overseeing, involved with, or
responsible for this activity, product, or service.</p></html>
""")


@site.route("/about")
def about(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"""
<!DOCTYPE html><html><head><title>about</title><style>{mm.send_file("mustache.css")}</style></head><body>
{mm.send_file("header.html")}
<h1 style="font-size:40px">Mo</h1><p style="font-size:20px; color: #FFFFFF;">by: The Mechanical Mustaches</p>
<img src='mechanical_mustaches/web/static/mm_logo.png'style="width: 150px;"></img><br>
<img src='mechanical_mustaches/web/static/FIRST_Horz_RGB.png' style="width: 150px;" /></img><br></body><html><br>
FIRST® Robotics Team 8122<br>
<p> write about us here !!!</p>
<a href="/"><button class="button grey">home</button></a>
<p style="font-size:8px">FIRST ® , the FIRST® logo, FIRST ® Robotics Competition, and FIRST ® Tech Challenge, are registered
trademarks of FIRST ® (<a href="http://www.firstinspires.org">www.firstinspires.org</a>) which is not overseeing, involved with, or
responsible for this activity, product, or service.</p></html>
""")






site.mount('/repl', repl.app)
site.mount('/editor', editor.app)
site.mount('/stacheboard', stacheboard.app)
site.run(debug=1, port=80, host=mm.my_ip)

