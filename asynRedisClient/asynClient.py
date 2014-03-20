#!/usr/bin/python
# coding=utf-8

import brukva

c = brukva.Client(host='localhost', port=46379,selected_db=0)
c.connect()
loop = c.connection._stream.io_loop
def on_result(result):
    print result
c.set('foo', 'bar', on_result)
c.get('foo', on_result)
c.execute_command("GEOADD", on_result, "allpoi" ,"MERCATOR", "123456", "654321", "999999")
c.execute_command("GEOSEARCH", on_result, "allpoi" ,"MERCATOR", "123455", "654320", "RADIUS","1000","WITHCOORDINATES","WITHDISTANCES")
c.hgetall('foo', [on_result, lambda r: loop.stop()])
loop.start() # start tornado mainloop
