import os
import requests
import pandas as pd
import json
import inspect
from objects import Account, Mailbox

def test_auth():
	key = os.environ["parseur_api_key"]
	url = 'https://api.parseur.com/'
	command = f'curl -X GET {url} -H "Authorization: Token {key}"'
	stream = os.popen(command)
	output = stream.read()
	print(output)


def not_setup():
	print()
	print(f'function: {inspect.stack()[1].function} has not been set up')


class ParseurAPI:

	key = os.environ["parseur_api_key"]
	url = 'https://api.parseur.com/'
	headers = {'Authorization': 'Token ' + key}

	#list mailboxes
	def list_mailboxes(self, sorting_key=[], search_query=None):
		"""
		Mailboxes objects are called parsers in the API.   

		To list all your mailboxes, make a GET request on /parser. The response is paginated

		The search query parameter will search in the following properties: 
		* mailbox name
		* mailbox email prefix
		"""
		supported_sorting_keys = [
			'name',
			'document_count',
			'template_count',
			'PARSEDOK_count',  # number of documents processed
			'PARSEDKO_count',  # number of documents not processed
			'QUOTAEXC_count',  # number of documents in quota exceeded status
			'EXPORTKO_count'   # number of documents in export failed status
		]  

		params = {'search_query': search_query}

		url = self.url + 'parser'
		if search_query:
			response = requests.get(url=url, params=params, headers=self.headers)
		else:
			response = requests.get(url=url,
															headers={'Authorization': 'Token ' + self.key})
		return response.json()

	def create_mailbox(self,
										 name,
										 email_prefix=None,
										 process_attachments=True,
										 master_parser_slug=None):
		"""
		Create a mailbox 
		To create a mailbox, make a POST request on /parser not_setup()ing the following keys: 
		 * name 
		 * email_prefix (optional, if not present, will be derived from name key)
		 * process_attachments: 
				 true / false (optional, defaults to true)
		 * master_parser_slug:
				 optional, set it if you want your mailbox to use one of our set of ready-
					 made templates. Possible values are: 
							 search-alerts, 
							 food-delivery, 
							 real-estate,
							 job-application,
							 property-bookings, 
							 job-search.
		"""
		url = self.url + 'parser'
		params = {'name': name, 'process_attachments': process_attachments}
		if email_prefix:
			params['email_prefix'] = email_prefix
		if master_parser_slug:
			params['master_parser_slug'] = master_parser_slug

		response = requests.post(url=url, params=params, headers={'Authorization': 'Token ' + self.key})
		return Account(response)

	def retrieve_mailbox(self, mailbox_id):
		"""
		Retrieve a mailbox 
		You can retrieve a mailbox with a GET request on /parser/:mailbox_id
		"""
		url = self.url + 'parser/:' + mailbox_id
		response = requests.get(url=url, headers={'Authorization': 'Token ' + self.key})
		return response

	def update_mailbox(self, mailbox_id):
		"""
		Update a mailbox 
		You can update a mailbox with a PUT or POST request on /parser/:mailbox_id
		"""
		not_setup()

	def copy_mailbox(self, mailbox_id):
		"""
		Copy a mailbox
		You can copy (duplicate) an existing mailbox with a POST on /parser/:mailbox_id/copy
		"""
		not_setup()

	def delete_mailbox(self, mailbox_id):
		"""
		Delete a mailbox 
		You can delete a mailbox with a DELETE request on /parser/:mailbox_id
		"""
		not_setup()

	def get_mailbox_schema(self, mailbox_id):
		"""
		Get the field structure (schema) of a mailbox
		You can get the mailbox schema with a GET request on /parser/:mailbox_id/schema
		
		Useful if you're planning to create a connector for Parseur. 
		"""
		not_setup()

	"""
	Manage Documents in a mailbox
	"""

	def send_documents(self):
		"""
		Send documents
		To send a document via API, check out this article
		"""
		not_setup()

	def list_documents(self, mailbox_id, document_set, sorting_key=None, search_query=None):
		"""
		List documents
		You can list your documents in a given mailbox with a GET request 
		on /parser/:mailbox_id/document_set. The response is paginated.

		Supported sorting keys (see the section below for more information):
			* name
			* created (default - received date)
			* modified (processed date)
			* status
		 
		The search query parameter will search in the following properties:
			* document id (exact match)
			* document name
			* template name
			* from to, cc and bcc email addresses
			* document metadata header
		"""
		not_setup()

	def retrieve_document(self, document_id):                   
		"""
		Retrieve a document
		You can retrieve a document and parsed results with a GET request 
		on /document/:document_id
		"""
		not_setup()

	def reprocess_document(self, document_id):
		"""
		Reprocess a document
		You can reprocess (parse) a document with a POST 
		on /document/:document_id/process
		"""
		not_setup()

	def skip_document(self, document_id):
		"""
		Skip a document
		You can set the Skipped status on a document with a POST 
		on /document/:document_id/skip
		"""
		not_setup()

	def copy_document(self, document_id, target_mailbox_id):
		"""
		Copy a document
		You can copy a document to another mailbox with a POST 
		on /document/:document_id/copy/:target_mailbox_id
		"""
		not_setup()

	def retrieve_doc_logs(self, document_id):
		"""
		Retrieve the logs for a document
		You can access the activity logs of a document with a GET 
		on /document/:document_id/log_set. Logs are paginated.
		"""
		not_setup()

	def delete_document(self, document_id):
		"""
		Delete a document
		You can delete a document with a DELETE request on /document/:document_id
		"""
		not_setup()

	# Manage Templates in a mailbox
	def list_templates(self, mailbox_id):
		"""
		List templates
		You can list your templates in a given mailbox with a GET request 
		on /parser/:mailbox_id/template_set. The response is paginated.

		Supported sorting keys (see the section below for more information):
			* name
			* created (creation date)
			* modified (default - last template update time or last time template was used)
			* last_activity (last time template was used)
			* status
			* document_count (number of documents matched by the template)
			
		The search query parameter will search in the following properties:
			* template name
		"""
		not_setup()

	def retrieve_template(self, template_id):
		"""
		Retrieve a template
		You can retrieve a template with a GET request on /template/:template_id
		"""
		not_setup()

	def copy_template(self, template_id, target_mailbox_id):
		"""
		Copy a template
		You can copy a template with a POST on /template/:template_id/copy/:target_mailbox_id
		"""
		not_setup()


	def delete_template(self, template_id):
		"""
		Delete a template
		You can delete a template with a DELETE request on /template/:template_id
		"""
		not_setup()

		# Manage Webhooks in a mailbox
	def list_webhooks(self, mailbox_id):
		"""
		List webhooks
		You can list your webhooks in a given mailbox with a GET request 
		on /parser/:mailbox_id

		Enabled webhooks are under the webhook_set key

		Paused webhooks are under the available_webhook_set key.
		"""
		not_setup()


	def create_webhook(self, event, target, category, mailbox_id, parser_field, name=None, headers=None):
		"""
		Create a webhook
		You can create a new webhook with a POST request on /webhook passing the following keys:
			* event: must be one of document.processed, document.processed.flattened, 
				document.template_needed  or table.processed (see our webhook reference 
				article for more information)
			* target: URL to send the data to, e.g. https://api.example.com/parseur
			* category: must be set to CUSTOM
			* parser: ID of the mailbox you want to add the webhook to, in numerical format
			* name: Custom name for the webhook. If omitted, will use the target URL instead. Optional
			* headers: JSON object containing the HTTP headers you want to send along with 
				the result data. Optional
			* parser_field: ID of a field or a table field you want the webhook to react to, 
				in the "PF12345" format
		"""
		not_setup()


	def enable_webhook(self, webhook_id):
		"""
		Enable a webhook
		You can enable an existing webhook for a given mailbox with a POST request 
		on /parser/:mailbox_id/webhook_set/:webhook_id
		"""
		not_setup()


	def pause_webhook(self, mailbox_id, webhook_id):
		"""
		Pause a webhook
		You can pause an existing webhook for a given mailbox with a DELETE request 
		on /parser/:mailbox_id/webhook_set/:webhook_id
		"""
		not_setup()


	def manage_parsed_data(self):
		"""
		Manage parsed data
		Parseur can send parsed data in real-time to your server via its Webhook feature. 
		Check out the webhook article to learn more.
		"""
		not_setup()



"""
Optional HTTP Query parameters
	The following query parameters can be mixed and matched.

	Pagination
		All GET request that return a list of documents, templates and mailboxes that support 
		the pagination by appending a page option to the URL. The default page size is 25. You 
		can change the page size using the page_size query parameter.

		For example: /parser?page=2&page_size=50 will list the 2nd page of your mailboxes, 
		each page containing 50 records.

	Searching
		Some endpoints support sorting via the search query parameter. The search value needs 
		to be URL encoded.
	
		For example /parser?search=test%20mailbox will search for mailbox names containing 
		"test mailbox"
	
		Unless stated otherwise, search is not case sensitive and will retrieve all entities that
		partially match the search string. For example, a mailbox search for foo will return 
		mailboxes named test.foo and FOO Mailbox 123.

	Sorting
		Some endpoints support sorting via the ordering query parameter.
			to sort a list ascending on the foo key, use ?ordering=foo
			to sort a list descending on the foo key, use ?ordering=-foo
	
		For example /parser?ordering=-document_count will list your mailboxes starting with 
		the one with the most documents
"""

