import requests

import datetime
from odoo import models,api,fields,_


class student_fee_inherited(models.Model):
	_inherit="student.payslip"




	email=fields.Char(string="Email")
	due_date=fields.Date(string="Due Date")



	@api.onchange('student_id')
	def get_student_email(self):
		self.email=self.student_id.email



	@api.multi
	def send_student_fee_reminder(self):
		rec=self.env['student.payslip'].search([])
		# print datetime.date.today(),"6666666666666666666666666666"

		#date_1 = datetime.datetime.strptime(today,'%Y-%m-%d')
		for x in rec:
			print type(x.due_date),"88888888888888888888888888888"
			print type(datetime.date.today())

			if x.state=='pending' and str(datetime.date.today())==str(x.due_date):

				print x.due_amount,"999999999999999999999999999999"
				
				url = "https://www.fast2sms.com/dev/bulk"
				payload = "sender_id=FSTSMS&message=Dear"+str(x.student_id.name)+" You need to pay " +str(x.due_amount)+" Due Amount. &language=english&route=p&numbers="+str(x.student_id.mobile)
				headers = {
						'authorization': "WnE3TqV6AIv5qf8ir5PKnVjXxCzhCFCHasABU58gXRhO9JFqFluWZXvlbsv9",
						'Content-Type': "application/x-www-form-urlencoded",
						'Cache-Control': "no-cache",
							}
				response = requests.request("POST", url, data=payload, headers=headers)
				# return response.text
		
		#developer 2
	# @api.onchange('date')
	# def get_student_due_date(self):
	# 	today = self.date 
	# 	date_1 = datetime.datetime.strptime(today,'%Y-%m-%d')
	# 	end_date = date_1 + datetime.timedelta(days=4)
	# 	self.due_date=end_date
		
		# tomorrow = today + datetime.timedelta(4)
		# dd=datetime.datetime.strftime(tomorrow,'%Y-%m-%d')
		# print dd,"00000000000000000000000000000000000000"




	
		