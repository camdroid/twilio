from secrets import twilio_account_sid as sid
from secrets import twilio_account_token as token
from twilio.rest import TwilioRestClient


class TwilioHelper(object):
    def __init__(self):
        self.client = TwilioRestClient(sid, token)

    def call(self, to):
        from_ = self.get_number_for_call()
        print('Placing call from {} to {}'.format(from_, to))
        return
        call = self.client.calls.create(url=call_url+'/receive_call', to=to, from_=from_)

    def get_available_numbers(self):
        account = self.client.accounts.get(sid)
        raw_numbers = account.incoming_phone_numbers.list()
        numbers = [num.phone_number for num in raw_numbers]
        return numbers

    def get_number_for_call(self):
        # TODO This should take in the 'to' number to try to match
        # the area code (if available).
        return self.get_available_numbers()[0]


if __name__ == '__main__':
    tw = TwilioHelper()
    tw.get_available_numbers()