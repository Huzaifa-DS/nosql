import redis

class RedisManager:
    def __init__(self, host='localhost', port=6379):
        self.client = redis.Redis(host=host, port=port)
    
    def cache_recommendations(self, user, recommendations):
        self.client.set(f'recommendations:{user}', ','.join(recommendations))
    
    def get_cached_recommendations(self, user):
        cached = self.client.get(f'recommendations:{user}')
        if cached:
            return cached.decode('utf-8').split(',')
        return None
