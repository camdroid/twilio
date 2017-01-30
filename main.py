from flask import Flask
from flask import render_template
from flask import request
import twilio.twiml
import twilio_helper

app = Flask(__name__)
tw = twilio_helper.TwilioHelper()

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Cam")
    return str(resp)


@app.route("/make_call", methods=['GET'])
def prep_call():
    ''' Make outgoing calls according to the parameters given '''
    return render_template('call_form.html', call_url='/make_call')


@app.route('/make_call', methods=['POST'])
def make_call():
    tw.call(request.form['to'])
    return render_template('call_placed.html')


@app.route('/receive_call', methods=['GET', 'POST'])
def receive_call():
    resp = twilio.twiml.Response()
    resp.say('You\'ve reached Cam, please call back later.')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)

