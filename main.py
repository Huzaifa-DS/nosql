from neo4j_script import Neo4jManager
from redis_script import RedisManager
from mongodb_script import MongoDBManager

# Initialize managers
neo4j = Neo4jManager("bolt://localhost:7687", "neo4j", "helloworld")
redis = RedisManager()
mongodb = MongoDBManager("mongodb://localhost:27017/", "movie_recommendation")

user = "Alice"

# Get recommendations from Neo4j
recommendations = neo4j.get_recommendations(user)
print(f"Recommendations for {user}: {recommendations}")

# Cache recommendations in Redis
redis.cache_recommendations(user, recommendations)

# Log the action in MongoDB
mongodb.log_action(user, "viewed_recommendations", recommendations)

# Retrieve cached recommendations
cached = redis.get_cached_recommendations(user)
print(f"Cached Recommendations for {user}: {cached}")

# Retrieve logs from MongoDB
logs = mongodb.get_logs()
print("Logs:", logs)

# Close the Neo4j connection
neo4j.close()

