import mechanical_mustaches as mm
from mechanical_mustaches import m
import wifi_cfg



mm.wifi_connect()


mm.start_web_page()
# webrepl.start()





import sys

try:
    from robot import *
    m.run(Robot())
except Exception as e:
    sys.print_exception(e)
    with open('/mechanical_mustaches/web/errors.log', 'w') as f:
        sys.print_exception(e, f)
    m.ss.fill(5,0,0)
    m.post("BOOT COMPLETE")
    m.post("WITH ERRORS")
    import uasyncio
    loop = uasyncio.get_event_loop()
    loop.run_forever()
    


  #----------------------------------
  #  comment all code above and write code in scratchpad
  #  for quick to boot code
  #----------------------------------
  

# from scratchpad import *
