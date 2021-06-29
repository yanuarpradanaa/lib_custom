# -*- coding: utf-8 -*-
from odoo import http

# class LibCustom(http.Controller):
#     @http.route('/lib_custom/lib_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lib_custom/lib_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lib_custom.listing', {
#             'root': '/lib_custom/lib_custom',
#             'objects': http.request.env['lib_custom.lib_custom'].search([]),
#         })

#     @http.route('/lib_custom/lib_custom/objects/<model("lib_custom.lib_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lib_custom.object', {
#             'object': obj
#         })