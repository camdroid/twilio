from flask import Flask
from flask import render_template
from flask import request
import twilio.twiml
import twilio_helper
from log import Log

app = Flask(__name__)
tw = twilio_helper.TwilioHelper()
log = Log()


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
    log.msg('Receiving call')
    resp = twilio.twiml.Response()
    resp.play('http://demo.twilio.com/hellomonkey/monkey.mp3')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)

