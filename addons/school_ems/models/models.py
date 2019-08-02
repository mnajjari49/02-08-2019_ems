# -*- coding: utf-8 -*-
from datetime import datetime
from openerp.exceptions import ValidationError,UserError
from odoo import models, fields, api,_


class timetable_view_classes(models.Model):
	_name='student.classes'

	name=fields.Many2one('standard.standard')
	#name=fields.Selection([('oneyeardiploma','One Year Diploma'),('twoyeardiploma','Two Year Diploma'),('talkntalk','Talk N Talk')])
	course_level=fields.Many2one('standard.semester',string="Course Level")
	classes=fields.Many2one('school.standard',string="Class")
	classes_id=fields.One2many('student.regular.timetable','timetable_id')
	campuses=fields.Many2one('school.school',string='Campus')
	state=fields.Selection([('draft','Draft'),('confirm','Confirmed')],default='draft')
	start_date=fields.Date(string="Class Start Date")
	end_date=fields.Date(string="Class End Date")
	status=fields.Char(string=" Class Status")
	s_no=fields.Integer(string="S.No")


	
	@api.onchange('classes_id')
	def _get_s_no(self):
		self.s_no = len(self.classes_id)+1


	@api.onchange('classes')
	def get_class_dates(self):
		if self.classes:
			self.start_date=self.classes.start_date
			self.end_date=self.classes.end_date
			self.status=self.classes.state


	@api.multi
	def confirmed_class(self):
		self.write({'state':'confirm'})



	@api.multi
	@api.constrains('classes_id')
	def _check_lecture(self):
		domain = [('timetable_id', 'in', self.ids)]
		line_ids = self.env['student.regular.timetable'].search(domain)
		for rec in line_ids:
			records = [rec_check.id for rec_check in line_ids

	
			if (
                rec.teacher_start_time == rec_check.teacher_start_time or
                rec.teacher_end_time == rec_check.teacher_end_time 

                              )]
			if len(records) > 1:
				print "ttttttttttttttttttttt"
				print records,"666666666666666666666666666666"
				raise ValidationError(_('''You cannot set lecture at same
                                            time %s  at same day. 
                                         ''') % (rec.teacher_start_time
                                                        
                                                    ))

                # Checks if time is greater than 24 hours than raise error
            # if rec.start_time > 24:
            #     raise ValidationError(_('''Start Time should be less than
            #                                 24 hours!'''))
            # if rec.end_time > 24:
            #     raise ValidationError(_('''End Time should be less than
            #                                 24 hours!'''))
        	return True



	@api.constrains('classes')
	def check_class_in_time_table(self):
		for x in self:
			rec=self.env['student.classes'].search([('id', '<', x.id)])
			
			for x in rec:
				print self.classes.standard,'111111111111111111'

				if self.classes.standard==x.classes.standard:
					print x.classes.standard
					raise UserError(_('This class is already created '))
		return True
	





	


			
class timetable_for_student(models.Model):
	_name="student.regular.timetable"


	serial_no=fields.Integer(string="Serial No")
	teacher = fields.Many2one('school.teacher', 'Teacher',ondelete='cascade')
	subject = fields.Many2one('student.subjects', 'Subject',ondelete='cascade')

	teacher_start_time = fields.Char("Period Start Time")
	teacher_end_time = fields.Char("Period End Time")
	timetable_id=fields.Many2one('student.classes','Timetable',ondelete='cascade')
	substistute=fields.Many2one('school.teacher',string='Substistute Teacher')
	substistute_date=fields.Date(string="Date")
	course_level=fields.Many2one('standard.semester',string="Course Level")
	classes=fields.Many2one('school.standard',string="Class")
	campuses=fields.Many2one('school.school',string='Campus')
	name=fields.Many2one('standard.standard')
	start_date=fields.Date(string="Class Start Date")
	end_date=fields.Date(string="Class End Date")
	status=fields.Char(string=" Class Status")



	
			



class fee_details_inherited(models.Model):
	_inherit='account.invoice'

	date_of_invoice=fields.Datetime(string="Invoice Date",default=datetime.now())






		


	




			




	
		

				