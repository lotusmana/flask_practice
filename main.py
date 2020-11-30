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
class HelloWorld(Resource):
    def get(self):
        return {"data": "hello world"}

# Register res w/api by class name and route
api.add_resource(HelloWorld, "/helloworld")

# Start server and flask app on localhost, port 5003
# Debugger on only while in development environment
# TURN DEBUGGER OFF FOR PRODUCTION ENV
if __name__ == "__main__":
    app.run(host="localhost", port=5003, debug=True)