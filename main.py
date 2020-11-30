# import modules here
try:
    from flask import Flask
    from flask_restful import Api, Resource
    import logging

except Exception as e:
    print("Some modules didn't import correctly.  {}".format(e))

# Create a flask app and wrap it in an RESTful api
app = Flask(__name__)
api = Api(app)

# Create classes that inherit from Resource,
# Override HTTP methods to define res behavior
# Return values must be JSON SERIALIZABLE
# Method declaration includes reqd params
class HelloWorld(Resource):
    def get(self, name, age):
        return {"test name": name,
                "test age": age
        }

    def post(self):
        return {"data":"posted"}

# Register res w/api by class name, route, & route params
# Route param names must match method param names above
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>")

# Start server and flask app on localhost, port 5003
# Debugger on only while in development environment
# TURN DEBUGGER OFF FOR PRODUCTION ENV
if __name__ == "__main__":
    app.run(host="localhost", port=5003, debug=True)