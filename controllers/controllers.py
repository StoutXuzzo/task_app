# -*- coding: utf-8 -*-
# from odoo import http


# class Task-app(http.Controller):
#     @http.route('/task-app/task-app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task-app/task-app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('task-app.listing', {
#             'root': '/task-app/task-app',
#             'objects': http.request.env['task-app.task-app'].search([]),
#         })

#     @http.route('/task-app/task-app/objects/<model("task-app.task-app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task-app.object', {
#             'object': obj
#         })
