import time
import thread
import GUI as gui
import connection as conn

thread.start_new_thread(conn.connection, ())
thread.start_new_thread(gui.GUI, ())
print("Hello")
time.sleep(1000)