from flask import Flask
from flask import render_template
import twilio.twiml
from config import call_url

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Cam")

    return str(resp)


@app.route("/make_call", methods=['GET'])
def make_call():
    ''' Make outgoing calls according to the parameters given '''
    return render_template('call_form.html', call_url=call_url)

if __name__ == "__main__":
    app.run(debug=True)

