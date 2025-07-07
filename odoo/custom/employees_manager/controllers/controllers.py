# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeesManager(http.Controller):
#     @http.route('/employees_manager/employees_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employees_manager/employees_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employees_manager.listing', {
#             'root': '/employees_manager/employees_manager',
#             'objects': http.request.env['employees_manager.employees_manager'].search([]),
#         })

#     @http.route('/employees_manager/employees_manager/objects/<model("employees_manager.employees_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employees_manager.object', {
#             'object': obj
#         })

