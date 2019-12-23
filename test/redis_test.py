import redis


redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)


def add_data(key, data, ttl):
    # data = json.dumps(data)
    ret_set = redis_client.hmset(key, data)
    ret_expire = redis_client.expire(key, ttl)
    return ret_set, ret_expire


def main():

    data = {'a': ['b']}
    if data:
        add_data('test', data, 60)
    return data


if __name__ == "__main__":
    print (main())
