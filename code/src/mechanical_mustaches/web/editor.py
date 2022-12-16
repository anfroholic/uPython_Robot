#
# This is a picoweb example showing how to handle form data.
#
import mechanical_mustaches as mm
import mechanical_mustaches.web.picoweb as picoweb
import gc
import uos
import machine
import utime
import uasyncio
app = picoweb.WebApp(__name__)

# globals
open_file = ''
open_filename = ''
files = []

def process(form, resp):
    """process POST request"""
    global open_file
    global open_filename
    for k, v in form.items():
        if k =='button_editor':
            open_filename = v
            with open(v, 'r') as f:
                open_file = f.read()
        elif k == 'button_reset':
            print('resetting Mo')
            machine.soft_reset()      
        elif 'save' in form:
            open_file = form['code']
            with open(open_filename, 'w') as f:
                f.write(open_file)



def parse_dir(dir_name, f) -> dict:
    global files
    ignore = ('mechanical_mustaches', 'boot.py', 'webrepl_cfg.py', 'main.py', 'config.py')
    name, _type, _, size = f
    ext = f'{dir_name}/{name}'
    if name in ignore:
        return
    if _type > 30000:  # this is a file
        files.append(ext)
    else:   # must be directory
        for file in uos.ilistdir(ext):
            parse_dir(ext, file)

def parse_dirs():
    global files
    files.clear()
    for f in uos.ilistdir():
        parse_dir('', f)
        

def button(func, color, location):
    return f'<a href="/editor?button_{location}={func}"><button class="button {color}">{func}</button></a>'

@app.route("/")
def index(req, resp):
    gc.collect()
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET, apparently
        req.parse_qs()
    # print(req.form)
    process(req.form, resp)
    parse_dirs()
    gc.collect()
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"""
<!DOCTYPE html><html><head><style>{mm.send_file('mustache.css')}</style></head><body>
{mm.send_file("header.html")}
<h1>Mo Edits!</h1><br>
<br><br>
<strong>filename: {open_filename}</strong><form action="editor" method="POST" id="coder">
<textarea class="textarea" name="code" autofocus="autofocus" cols=100 rows={open_file.count('\n') + 6} onfocus="var temp_value=this.value; this.value=''; this.value=temp_value">""")
    yield from resp.awrite(open_file)
    yield from resp.awrite("""</textarea>
<input type="submit" name="save" value="save"class="button pink_s" />
</form>
<br>
<a href="/editor?button_reset"><button class="button pink">reset</button><br><br>
""")
    for file in files:
        yield from resp.awrite(f"{button(file, 'grey', 'editor')}<br></body></html>")
    gc.collect()


    

def script():
    return """<script>
</script>"""


