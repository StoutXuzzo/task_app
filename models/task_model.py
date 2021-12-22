# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class TaskModel(models.Model):
    _name = 'task_app.task_model'
    _description = 'Task Model' 
    _sql_constraints = [('task_name_uniq', 'UNIQUE (name, active)', 'There cannot be two tasks with the same name!!'),]

    name = fields.Char("Task Name", required = True)
    is_done = fields.Boolean("Is done?", default = False)
    active = fields.Boolean("Is active?", default = True)
    category = fields.Many2one("task_app.category_model", "Category")

    date = fields.Datetime("Last change", compute="_lastChange", store=True)

    def changeState(self):
        self.ensure_one()
        self.is_done = not self.is_done
        if (self.is_done):
            self.active = False

    def cleanFinished(self):
        data = self.search([("active", "=", False)])
        for obj in data:
            obj.unlink()

    @api.constrains("name")
    def _check_length(self):
        if len(self.name) < 5:
            raise ValidationError("The name of the task must have at least 5 characters!")
        return True

    @api.depends("name", "is_done", "active", "category")
    def _lastChange(self):
        self.date = datetime.now()
        return True

    
