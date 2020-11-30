# import modules here
try:
    from flask import Flask, request
    from flask_restful import Api, Resource, reqparse, abort
    import logging

except Exception as e:
    print("Some modules didn't import correctly.  {}".format(e))

# Create a flask app and wrap it in an RESTful api
app = Flask(__name__)
api = Api(app)

# Create an object to hold video data added/stored
videos = {}

# Create a request parsing object
# Reqparser will validate request parameters
# Define mandatory arguments for put request
# If args w/reqd=True not provided, display help message
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of the video rqd", required=True)
video_put_args.add_argument("views", type=int, help="vid views rqd", required=True)
video_put_args.add_argument("likes", type=int, help="vid likes rqd", required=True)

# Handle requests for video_id not in videos = {}
def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video ID is not valid")

def abort_if_video_id_exist(video_id):
    if video_id in videos:
        abort(409, message="Video ID already used")


# Create classes that inherit from Resource,
# Override HTTP methods to define res behavior
# Return values must be JSON SERIALIZABLE
# Method declaration includes reqd params
class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def post(self):
        return {"data":"posted"}
    
    def put(self, video_id):
        #check if defined arguments are provided, and if video_id unavailable
        abort_if_video_id_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204

# Register res w/api by class name, route, & route params <type:label>
# Route param label must match corresponding method parameters above
api.add_resource(Video, "/video/<int:video_id>")

# Start server and flask app on localhost, port 5003
# Debugger on only while in development environment
# TURN DEBUGGER OFF FOR PRODUCTION ENV
if __name__ == "__main__":
    app.run(host="localhost", port=5003, debug=True)