# Refer to the official document at https://neo4j.com/docs/api/python-driver/current/api.html
from neo4j import GraphDatabase

class Neo4jDriver(object):
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(encrypted=False, uri=uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def exec_read_cypher(self, cypher):

        with self._driver.session() as session:
            result = self._exec_cypher(session, cypher)

            # ret = result.single()
            ret = []
            # You need to iterate before the session.close()
            for record in result:
                ret.append(record)

            session.close()

        self._driver.close()
        return ret

    def exec_write_cypher(self, cypher):
        with self._driver.session() as session:
            created = session.write_transaction(self._exec_cypher, cypher)
            session.close()
        self._driver.close()
        return created

    @staticmethod
    def _exec_cypher(tx, cypher):
        print('[Cypher]: ', cypher)
        result = tx.run(cypher)
        # return result.single()[0]
        return result
