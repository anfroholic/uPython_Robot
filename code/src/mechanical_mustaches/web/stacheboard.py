import mechanical_mustaches as mm
from mechanical_mustaches import m
import mechanical_mustaches.web.picoweb as picoweb
# import mechanical_mustaches.web.ulogging as logging
import json
import esp32
import uasyncio
import sys
import gc




g_imprtd = False

user_buttons = {}
page = ''


    
def create_webpage():
    global page
    global user_buttons
    
    try:
        from agents.stache_board import buttons as user_buttons

    except Exception as e:
        sys.print_exception(e)
        pass
    
    
    page = ''.join([f"<html><head><title>Mo's Mayhem</title><style>{mm.send_file('mustache.css')}</style>",
f"""
</head><body>
{mm.send_file("header.html")}

<br>
<h1>Mo's Stache'board<br></h1><h3>dashboard</h3><strong>
<div>
<table>
<tr><td>count:</td><td id="count"> </td></tr>
<tr><td>robot.state:</td><td id="m_state"> </td></tr>
<tr><td>temp:</td><td id="temp"> </td></tr>
""",
''.join([f'<tr><td>{name.replace("_", ".")}:</td><td id="{name}"> </td></tr>' for name, _ in m.the_report]),
"""
</table></div>
<br><br></strong><p><script>
var source = new EventSource("stacheboard/events");
source.onmessage = function(event) {
  var load = JSON.parse(event.data);
  console.log(load);
  document.getElementById("temp").innerHTML = load.temp;
  document.getElementById("count").innerHTML = load.count;
  document.getElementById("m_state").innerHTML = load.m_state;
""",
''.join([f'document.getElementById("{name}").innerHTML = load.{name};' for name, _ in m.the_report]),
"""}
source.onerror = function(error) {
    console.log(error);
    document.getElementById("result").innerHTML += "EventSource error:" + error + "<br>";
    }
</script></body></html>"""])


form_data = None

funcs = {
    'disabled': lambda: m.change_state('disabled'),
    'auto': lambda: m.change_state('auto'),
    'teleop': lambda: m.change_state('teleop'),
    'test': lambda: m.change_state('test')
    }


def button(func, color, location):
    return f'<a href="/stacheboard?button_{location}={func}"><button class="button {color}">{func}</button></a>'

def process(form):
    global g_imprtd
    for k, v in form.items():
        if k =='button_m':
            funcs[v]()
        if k =='button_stache':
            user_buttons[v]()

# @site.route("/")
def index(req, resp):
    gc.collect()
    if not page:  # page should be created only after all agents and m have finished booting
        
        create_webpage()
        
                
    if req.method == "POST":
        yield from req.read_form_data()
    else: # must be GET
        req.parse_qs()
    print('printing form data', req.form)
    process(req.form)
    yield from picoweb.start_response(resp)
    yield from resp.awrite(page)
    for func in funcs:
        yield from resp.awrite(button(func, 'pink', 'm'))
    yield from resp.awrite('<br><hr><strong>agents.stache_board.buttons</strong><br>')
    if not user_buttons:
        yield from resp.awrite('<strong><p style="color:red">agents.stacheboard buttons failed to load<br>check traceback to find issue</p></strong>')
    else:
        for butt in user_buttons:
            yield from resp.awrite(button(butt, 'grey', 'stache'))
    yield from resp.awrite('</p></html>')
    


def events(req, resp):
    print("Event source connected")
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/event-stream\r\n")
    yield from resp.awrite("\r\n")
    i = 0
    try:
        while True:
            load = {"count": i,
                    "temp": esp32.raw_temperature(),
                    "m_state": m.state}
            load.update(m.report())
            load = "data: {}\n\n".format(json.dumps(load))
            yield from resp.awrite(load)
            yield from uasyncio.sleep(.5)
            i += 1
    except OSError:
        print("Event source connection closed")
        yield from resp.aclose()




ROUTES = [
    ("/", index),
    ("/events", events),
]

app = picoweb.WebApp(__name__, ROUTES)


