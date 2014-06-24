import requests
import json

public_key = None
secret_key = None
base_url = 'http://datapagos.herokapp.com/api/v1'

class Token():
	@classmethod
	def show(self, uid):
		return requests.get(base_url + '/tokens/' + uid, auth=(public_key, secret_key))

class Charge():
	@classmethod
	def show(self, uid):
		return requests.get(base_url + '/charges/' + uid, auth=(public_key, secret_key))

	@classmethod
	def create(self, **kargs):
		return requests.post(base_url + '/charges', json.dumps(kargs), auth=(public_key, secret_key))

class Subscription():
	@classmethod
	def show(self, uid):
		return requests.get(base_url + '/subscriptions/' + uid, auth=(public_key, secret_key))

	@classmethod
	def create(self, **kargs):
		return requests.post(base_url + '/subscriptions', json.dumps(kargs), auth=(public_key, secret_key))