# -*- coding: utf-8 -*-
from odoo import http

# class SchoolEms(http.Controller):
#     @http.route('/school_ems/school_ems/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_ems/school_ems/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_ems.listing', {
#             'root': '/school_ems/school_ems',
#             'objects': http.request.env['school_ems.school_ems'].search([]),
#         })

#     @http.route('/school_ems/school_ems/objects/<model("school_ems.school_ems"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_ems.object', {
#             'object': obj
#         })