import json
import pandas as pd



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
		self.df = self.to_dataframe()


	def to_dataframe(self):
		df = pd.DataFrame()
		df['can_transform'] = self.can_transform
		df['document_count'] = self.document_count
		df['document_per_status_count'] = self.document_per_status_count
		df['email_prefix'] = self.email_prefix
		df['feature_flag_ocr'] = self.feature_flag_ocr
		df['feature_flag_pdfminer'] = self.feature_flag_pdfminer
		df['force_ocr'] = self.force_ocr
		df['id'] = self.id
		df['is_master'] = self.is_master
		df['last_activity'] = self.last_activity
		df['master_parser_name'] = self.master_parser_name
		df['master_parser_slug'] = self.master_parser_slug
		df['name'] = self.name
		df['owner_email'] = self.owner_email
		df['owner_id'] = self.owner_id
		df['parser_object_count'] = self.parser_object_count
		df['process_attachments'] = self.process_attachments
		df['retention_policy'] = self.retention_policy
		df['template_count'] = self.template_count
		df['webhook_count'] = self.webhook_count
		df['attachments_field'] = self.attachments_field
		df['original_document_field'] = self.original_document_field
		df['headers_field'] = self.headers_field
		df['received_field'] = self.received_field
		df['received_date_field'] = self.received_date_field
		df['received_time_field'] = self.received_time_field
		df['sender_field'] = self.sender_field
		df['sender_name_field'] = self.sender_name_field
		df['recipient_field'] = self.recipient_field
		df['to_field'] = self.to_field
		df['cc_field'] = self.cc_field
		df['bcc_field'] = self.bcc_field
		df['reply_to_field'] = self.reply_to_field
		df['recipient_suffix_field'] = self.recipient_suffix_field
		df['original_recipient_field'] = self.original_recipient_field
		df['subject_field'] = self.subject_field
		df['template_field'] = self.template_field
		df['html_document_field'] = self.html_document_field
		df['text_document_field'] = self.text_document_field
		df['last_reply_field'] = self.last_reply_field
		df['document_id_field'] = self.document_id_field
		df['parent_id_field'] = self.parent_id_field
		df['document_url_field'] = self.document_url_field
		df['public_document_url_field'] = self.public_document_url_field
		df['available_webhook_set'] = self.available_webhook_set
		df['webhook_set'] = self.webhook_set
		df['table_set'] = self.table_set
	
		return df




class Account:
	def __init__(self, data):
		d = json.loads(data)
		self.count = d['count']
		self.current = d['current']  
		self.total = d['total']
		self.results = Mailbox(d['results'])

	def get_mailboxes(self):
		return self.results

	def __str__(self):
		s = "Account details:\n" + \
		    f'  Count:   {self.count}' + \
			f'  Current: {self.current}' + \
			f'  Total:   {self.total}'

		return s