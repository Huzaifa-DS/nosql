from neo4j import GraphDatabase

class Neo4jManager:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def get_recommendations(self, user):
        with self.driver.session() as session:
            query = """
            MATCH (a:User {name: $user})-[:LIKES]->(m:Movie)<-[:LIKES]-(other:User)-[:LIKES]->(rec:Movie)
            WHERE NOT (a)-[:LIKES]->(rec)
            RETURN rec.title AS Recommendation
            """
            result = session.run(query, user=user)
            return [record["Recommendation"] for record in result]
neo4j_script.py
