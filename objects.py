import json




class Mailbox:
	def __init__(self, data):
		d = json.loads(data)
		self.can_transform = d['can_transform']
		self.document_count = d['document_count']
		self.document_per_status_count = json.loads(d['document_per_status_count'])
		self.email_prefix = d['email_prefix']
		self.feature_flag_ocr = d['feature_flag_ocr']
		self.feature_flag_pdfminer = d['feature_flag_pdfminer']
		self.force_ocr = d['force_ocr']
		self.id = d['id']
		self.is_master = d['is_master']
		self.last_activity = d['last_activity']
		self.master_parser_name = d['master_parser_name']
		self.master_parser_slug = d['master_parser_slug']
		self.name = d['name']
		self.owner_email = d['owner_email']
		self.owner_id = d['owner_id']
		self.parser_object_count = d['parser_object_count']
		self.process_attachments = d['process_attachments']
		self.retention_policy = d['retention_policy']
		self.template_count = d['template_count']
		self.webhook_count = d['webhook_count']
		self.attachments_field = d['attachments_field']
		self.original_document_field = d['original_document_field']
		self.headers_field = d['headers_field']
		self.received_field = d['received_field']
		self.received_date_field = d['received_date_field']
		self.received_time_field = d['received_time_field']
		self.sender_field = d['sender_field']
		self.sender_name_field = d['sender_name_field']
		self.recipient_field = d['recipient_field']
		self.to_field = d['to_field']
		self.cc_field = d['cc_field']
		self.bcc_field = d['bcc_field']
		self.reply_to_field = d['reply_to_field']
		self.recipient_suffix_field = d['recipient_suffix_field']
		self.original_recipient_field = d['original_recipient_field']
		self.subject_field = d['subject_field']
		self.template_field = d['template_field']
		self.html_document_field = d['html_document_field']
		self.text_document_field = d['text_document_field']
		self.last_reply_field = d['last_reply_field']
		self.document_id_field = d['document_id_field']
		self.parent_id_field = d['parent_id_field']
		self.document_url_field = d['document_url_field']
		self.public_document_url_field = d['public_document_url_field']
		self.available_webhook_set = d['available_webhook_set']
		self.webhook_set = d['webhook_set']
		self.table_set = json.loads(d['table_set'])

	
	

class Account:
	def __init__(self, data):
		d = json.loads(data)
		self.count = d['count']
		self.current = d['current']  
		self.total = d['total']
		self.results = Mailbox(d['results'])

	def get_mailboxes(self):
		return self.results