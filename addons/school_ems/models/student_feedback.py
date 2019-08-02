
from odoo import models, fields, api,_


class student_feedback(models.Model):
	_name="student.feedbackform"


	# @api.model
	# def _default_employee_name(self):
	# 	return self.env.user.name


	# Basic Information for Feedback

	name=fields.Many2one('student.student',string="Student Name",required=True)
	s_id=fields.Char(string="Student ID No.")
	d_joining=fields.Date(string="Date of Joining")
	no_days=fields.Char(string="No. Days in MELI")
	course_level=fields.Char(string="Course Level")
	email=fields.Char(string="Email")
	campus=fields.Char(string="Campus")
	state=fields.Selection([('draft','Draft'),('confirm','Confirmed')],default="draft")


	# Feedback for Course Survey

	course_survey1=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	course_survey2=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	course_survey3=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	course_survey4=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	course_survey5=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	course_survey6=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	
	#Curriculum and classes for the term 

	curriculum1=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	curriculum2=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	curriculum3=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	curriculum4=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	curriculum5=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	curriculum6=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	curriculum7=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )

	# Feedback for Material
	material1=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	material2=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	material3=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )

	#feeback for campus environment

	environment1=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	environment2=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	environment3=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	environment4=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
#feedback for Trainers
	trainer1=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	trainer2=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )
	trainer3=fields.Selection([('strongly agree','Strongly Agree '),
									   ('agree','Agree'),
									   ('neutral','Neutral'),
									   ('disagree','Disagree'),
									   ('stronglydisagree','Strongly Disagree')],
									   )


#feedback for Recommendations

	remind=fields.Selection([('verylikely','Very likely '),
									   ('somewhatlikely','Somewhat likely'),
									   ('unsure','Unsure'),
									   ('notverylikely','Not very likely'),
									   ('notlikely','Not likely')],
									   )
	comment=fields.Text(string="Comments",required=True)



	@api.onchange('name')
	def get_student_details(self):
		if self.name:
			self.s_id=self.name.student_code
			self.d_joining=self.name.admission_date
			self.course_level=self.name.semester_id.name
			self.email=self.name.email
			self.campus=self.name.school_id.name




	@api.multi
	def feedback_confirmation(self):
		self.write({'state':'confirm'})


class studenr_profile_inherited(models.Model):
	_inherit="student.student"

	@api.multi
	def student_feedback_count(self):
		return{
        'type': 'ir.actions.act_window',
        'name':'Feed Back',
        'view_mode': 'tree,form',
        'res_model': 'student.feedbackform',
        'domain':[('name.name','=',self.name)],
        'context': {
	        'create':False,
	        'edit' : False,
	        'delete' : False,
	        }
    	}











