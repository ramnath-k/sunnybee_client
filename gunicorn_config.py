import multiprocessing

bind = "127.0.0.1:8000"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 4

max_requests = 100
loglevel = "debug"

settings = "sunnybee_client.settings"

accesslog = "logs/gunicorn_access.log"
errorlog = "logs/gunicorn_error.log"

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(L)s %(p)s %({Header}i)s %({Header}o)s'

