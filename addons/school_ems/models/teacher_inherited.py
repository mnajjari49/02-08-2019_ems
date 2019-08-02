import time
import re
import math
from datetime import datetime, timedelta, date
from dateutil import relativedelta
from openerp.exceptions import UserError



from odoo import models, fields, api,_




class teacher_inherited(models.Model):
	_inherit='school.teacher'

	


	counting=fields.Char(string="Count",compute="_get_default_name")
	extra_class=fields.Char(string="Extra Class",compute="_get_default_name")
	history=fields.Char(string="Class History",compute="_get_default_name")
	update_subjects=fields.Char(string="Teacher Subjects",compute="_get_default_name")
	

	@api.multi 
	def _get_default_name(self):
		data_obj = self.env['student.regular.timetable'].search([('teacher','=',self.employee_id.name),('status','=','running')])
		self.update_subjects = len(data_obj)
		self.counting=len(data_obj)
		rec = self.env['student.regular.timetable'].search([('substistute','=',self.employee_id.name),('status','=','running')])
		self.extra_class=len(rec)
		obj=self.env['student.regular.timetable'].search([('teacher','=',self.employee_id.name),('status','=','close')])
		self.history=len(obj)


	





	@api.multi
	def teacher_class_timetable1(self):

		return{
        	'type': 'ir.actions.act_window',
        	'name':'Extra Timetable',
        	'view_mode': 'tree',
        	# 'groups':'hr.group_hr_user,hr.group_hr_manager,base.group_user',
        	'res_model': 'student.regular.timetable',
        	'domain':[('substistute','=',self.employee_id.name),('status','=','running')],
    			}







	@api.multi
	def teacher_class_timetable(self):

		return{
        	'type': 'ir.actions.act_window',
        	'name':'Class Timetable',
        	'view_mode': 'tree',
        	# 'groups':'hr.group_hr_user,hr.group_hr_manager,base.group_user',
        	'res_model': 'student.regular.timetable',
        	'domain':[('teacher','=',self.employee_id.name),('status','=','running')],
    			}
	@api.multi
	def teacher_class_timetable2(self):
		return{
    		'type': 'ir.actions.act_window',
        	'name':'Extra Timetable',

        	'view_mode': 'tree',
       	 	# 'groups':'hr.group_hr_user,hr.group_hr_manager,base.group_user',
        	'res_model': 'student.regular.timetable',
        	'domain':[('teacher','=',self.employee_id.name),('status','=','close')],
        	

    			}




		
		



class warning_message_for_students(models.Model):
	_inherit = 'student.warning'


	campus=fields.Many2one('school.school',string='Campus')
	program=fields.Many2one('standard.standard',string='Program')
	course_level=fields.Many2one('standard.semester',string="Course Level")
	student=fields.Many2one('student.student',string='Student Name')


# class teacher_leave_request(models.Model):
# 	_name="teacher.leaves"
# 	_rec_name="teacher_id"



# 	teacher_id=fields.Many2one('school.teacher',string='Teacher Name',required=True)
# 	leave_type=fields.Selection([('sickleave','Sick Leave'),
# 								 ('annualleave','Annual Leave'),
# 								 ('compassionateleave','Compassionate Leave'),
# 								 ('marriageleave','Marriage Leave'),
# 								 ('otherleaves','Other Leaves')],required=True)
# 	date_from=fields.Date(string="Start Date",default=datetime.now())
# 	date_to=fields.Date(string="End Date",default=datetime.now())
# 	campus=fields.Char(string='Campus')
# 	department=fields.Char(string="Department")
# 	designation=fields.Char(string="Designation")
# 	substistute_teacher=fields.Many2one('school.teacher',string="Subsististute Teacher")
# 	remarks=fields.Text()
# 	leave_days=fields.Char(string="Leaves Count")
# 	state=fields.Selection([('draft','Draft'),('confirm','Confirmed'),('approve','Approved'),
# 							('reject','Rejected')],default="draft")



# 	@api.onchange('teacher_id')
# 	def get_details_from_teacher_record(self):
# 		if self.teacher_id:
# 			self.campus=self.teacher_id.school_id.name
# 			self.department=self.teacher_id.department_id.name
# 			self.designation=self.teacher_id.job_id.name
		



# 	@api.onchange('date_from')
# 	@api.constrains('date_from')
# 	def date_from_validation(self):
# 		fridays = self.all_fridays()
# 		for friday in fridays:
#  			if friday == self.date_from:
#  				raise UserError("Your Requested Start Date is Friday. Note: Week off")



		

# 	@api.onchange('date_from', 'date_to')
# 	def total_leave_days(self):
# 			d1 = datetime.strptime(self.date_from, "%Y-%m-%d")
# 			d2 = datetime.strptime(self.date_to, "%Y-%m-%d")
# 			self.leave_days=str(((d2 - d1).days))+' days'
		


# 	def all_fridays(self):
# 		total_fridays = []
# 		year = datetime.now().strftime("%Y")    
# 		d = date(int(year), 1, 1)
# 		d += timedelta(days = 4 - d.weekday())
# 		while d.year == int(year):
# 			total_fridays.append(str(d))
# 			d += timedelta(days = 7)
# 		return total_fridays



# 	@api.multi
# 	def confirmation(self):
# 		self.write({'state':'confirm'})

# 	@api.multi
# 	def approved(self):
# 		self.write({'state':'approve'})

# 	@api.multi
# 	def rejected(self):
# 		self.write({'state':'reject'})


class subjects_inherited(models.Model):
	_inherit="subject.subject"


	program=fields.Many2one('standard.standard',string="Program")
	course_level=fields.Many2one('standard.semester',string="Course Level")
class student_subjects(models.Model):
	_name = 'student.subjects'


	name=fields.Char(string="Subject Name")
	program_id=fields.Many2one('standard.standard',string='Program')
	semester_id=fields.Many2one('standard.semester',strint='Course Level')
	campus_id=fields.Many2one('school.school',string='Campus')
	sub_code=fields.Char(string='Subject Code')
class classes_inherited(models.Model):
	_inherit='school.standard'



	@api.constrains('division_id')
	def onchange_class_room(self):
		data=self.env['school.standard'].search([])
		for rec in data:
			if rec.state == 'running':
				if rec.end_date!=False and self.division_id.name==rec.division_id.name and self.school_id.name == rec.school_id.name:
					d=datetime.date(datetime.now())
					d2=datetime.strptime(rec.end_date, '%Y-%m-%d')
					d3=datetime.strptime(str(d), '%Y-%m-%d')
					delta=d2-d3
					raise UserError(_('In This Class Room Already Class Is GOing On."%s" days Left')%(delta.days))



class student_results_inherited(models.Model):
	_inherit='student.student'


	@api.multi
	def student_results(self):
		return{
        'type': 'ir.actions.act_window',
        'name':'Result',
        'view_mode': 'tree',
        'domain':[('name.name','=',self.name),('status','=','confirm')],
        'res_model': 'etq.result',
    	}

	