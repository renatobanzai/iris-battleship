import irisnative
import json

class irisdomestic():
    def __init__(self, iris_config):
        self.iris_connection = None
        self.get_iris_connection(iris_config)
        self.iris_native = irisnative.createIris(self.iris_connection)
        return

    def isDefined(self, *args):
        return self.iris_native.isDefined(*args)

    def kill(self, *args):
        self.iris_native.kill(*args)

    def set(self, value, *args):
        return self.iris_native.set(value, *args)

    def get(self, *args):
        return self.iris_native.get(*args)

    def iterator(self, *args):
        return self.iris_native.iterator(*args)

    def get_iris_connection(self, iris_config):
        #todo: understand the behavior of connection object and implement the correct way
        if not self.iris_connection:
            self.iris_connection = irisnative.createConnection(iris_config["host"],
                                                               iris_config["port"],
                                                               iris_config["namespace"],
                                                               iris_config["username"],
                                                               iris_config["password"])

        return self.iris_connection

