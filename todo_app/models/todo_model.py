# -*- coding: utf-8 -*-
from odoo import models, fields, api
class TodoTask(models.Model):
    _name = 'todo.task' # model identifier required field
    _description = 'To-do Task' #provides friendly name for the model
    name = fields.Char('Description', required=True)#required field
    active = fields.Boolean('Active?', default=True)
    is_done = fields.Boolean('Done?', default=False)

    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done #not efficient use write() instead
            return True

    @api.model
    def do_clear_done(self):
        dones = self.search([('is_done', '=', True)])
        dones.write({'active': False})
        return True