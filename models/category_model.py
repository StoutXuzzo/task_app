# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CategoryModel(models.Model):
    _name = 'task_app.category_model'
    _description = 'Category Model' 

    name = fields.Char("Category Name", required = True)
    description = fields.Html("Category Description", required = False, default = False)
    #refsh
    tasks = fields.One2many("task_app.task_model", "category", "Tasks")
    