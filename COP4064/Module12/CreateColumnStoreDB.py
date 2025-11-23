/home/merrick1412/.virtualenvs/Module12/bin/python /home/merrick1412/repository/COP4064/Module12/CreateColumnStoreDB.py
Could not connect to monetdb://localhost/demo: [Errno 111] Connection refused
Traceback (most recent call last):
  File "/home/merrick1412/repository/COP4064/Module12/CreateColumnStoreDB.py", line 136, in <module>
    main()
  File "/home/merrick1412/repository/COP4064/Module12/CreateColumnStoreDB.py", line 123, in main
    conn = get_monetdb_connection()
  File "/home/merrick1412/repository/COP4064/Module12/CreateColumnStoreDB.py", line 37, in get_monetdb_connection
    conn = pymonetdb.connect(
  File "/home/merrick1412/.virtualenvs/Module12/lib/python3.10/site-packages/pymonetdb/__init__.py", line 203, in connect
    return Connection(target)
  File "/home/merrick1412/.virtualenvs/Module12/lib/python3.10/site-packages/pymonetdb/sql/connections.py", line 65, in __init__
    self.mapi.connect(target, handshake_options_callback=handshake_options_callback)
  File "/home/merrick1412/.virtualenvs/Module12/lib/python3.10/site-packages/pymonetdb/mapi.py", line 141, in connect
    self.connect_target()
  File "/home/merrick1412/.virtualenvs/Module12/lib/python3.10/site-packages/pymonetdb/mapi.py", line 211, in connect_target
    self.connect_loop()
  File "/home/merrick1412/.virtualenvs/Module12/lib/python3.10/site-packages/pymonetdb/mapi.py", line 252, in connect_loop
    self.try_connect()
  File "/home/merrick1412/.virtualenvs/Module12/lib/python3.10/site-packages/pymonetdb/mapi.py", line 327, in try_connect
    raise err
  File "/home/merrick1412/.virtualenvs/Module12/lib/python3.10/site-packages/pymonetdb/mapi.py", line 316, in try_connect
    s.connect(addr)
ConnectionRefusedError: [Errno 111] Connection refused

Process finished with exit code 1
