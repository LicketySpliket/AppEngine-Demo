# Import your packages! These are remote "libraries" that you can use.
# When you import a package, you are accessing the tools that people have previously written.
# No need to re-invent the wheel!

# Flask - web server package
# time - time package
# random - random numbers package
from flask import Flask, jsonify
import time
import random
from hashlib import sha256

# Create an application.
# In Python, __name__ is the "name" of the module.
# You don't really need to worry about this, but if you run the script like python3 main.py, the __name__ is __main__.
app = Flask(__name__)

# Declare a response on the /generate-timestamp path.
# Let's send the user the current timestamp and a random number.
@app.route("/generate-timestamp")
def generate_timestamp():

    sha_test = ""
    random_num = str(random.randint(1, 100))

    # this is a random function that just takes some cpu usage
    # simulate actual server running
    for i in range(0, 100):
        sha_test += sha256(random_num.encode('utf-8')).hexdigest()


    return f"The time is {str(time.time())} and a random number is {random_num}. Your hash is {sha_test}"

@app.route("/loaderio-67da26bc7bdecd0fafcd70358599c75d.txt")
def handle_loader_verify():
    return "loaderio-67da26bc7bdecd0fafcd70358599c75d"

# More immediate-level Python, this is pretty common in small scripts.
# Prevent this "app.run" from being run if this code is imported elsewhere.
if __name__ == "__main__":
    # Start the app on port 8080!
    # You can now access it at http://0.0.0.0/generate-timestamp
    app.run(host="0.0.0.0", port=8080)
