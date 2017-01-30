from secrets import twilio_account_sid as sid
from secrets import twilio_account_token as token
from twilio.rest import TwilioRestClient
from log import Log


class TwilioHelper(object):
    def __init__(self):
        self.log = Log()
        self.client = TwilioRestClient(sid, token)
        # TODO Will need to eventually replace this with an actual url
        self.call_url = 'https://dee6942a.ngrok.io'

    def call(self, to):
        from_ = self.get_number_for_call()
        print('Placing call from {} to {}'.format(from_, to))
        call = self.client.calls.create(url=self.call_url+'/receive_call',
                                        to=to, from_=from_)
        self.log.msg('Call result: {}'.format(call))
        return call

    def get_available_numbers(self):
        account = self.client.accounts.get(sid)
        raw_numbers = account.incoming_phone_numbers.list()
        if raw_numbers:
            numbers = [num.phone_number for num in raw_numbers]
            return numbers
        raise Exception("Couldn't find any numbers with this account")

    def get_number_for_call(self):
        # TODO This should take in the 'to' number to try to match
        # the area code (if available).
        return self.get_available_numbers()[0]


if __name__ == '__main__':
    tw = TwilioHelper()
    tw.get_available_numbers()
