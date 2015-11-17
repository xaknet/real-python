from flask import Flask

app = Flask(__name__)

# error handing
app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

# dynamic route
@app.route("/search/<search_query>")
def search(search_query):
	return search_query

# values types
@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	value = value + 1
	return "correct = {}".format(value)


# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct = {}".format(value)

@app.route("/name/<name>")
def index(name):
	if name.lower() == "test":
		return "Hello, {}".format(name)
	else:
		return "Not Found", 404



def hello_world():
	return "Hello world"


if __name__ == "__main__":
	app.run()