import redis

host = '127.0.0.1'
port = 6379

r = redis.Redis(host=host, port=port)

k = "2019"
r.set(k, 'bar8')
print(r.get(k))