from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
)

def insert_entities(entities):
    with driver.session() as session:
        for text, label in entities:
            session.run(
                "MERGE (e:Entity {name: $name, label: $label})",
                name=text, label=label
            )

def query_entities(label):
    with driver.session() as session:
        result = session.run("MATCH (e:Entity {label: $label}) RETURN e.name AS name", label=label)
        return [record["name"] for record in result]
