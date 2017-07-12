# -*- coding: utf-8 -*-
from odoo import models,fields,api

class TodoModel(models.Model):
    _inherit = 'todo.task'
    stag_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')

class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'
    name = fields.Char('Name', 40, translate=True)

    _parent_store = True
    _parent_name = 'parent_id'
    parent_id = fields.Many2one('todo.task.tag', 'Parent Tag', ondelete='restrict')
    parent_left = fields.Integer('Parent Left', index=True)
    parent_right = fields.Integer('Parent Right', index=True)

    child_ids = fields.One2many('todo.task.tag', 'parent_id', 'Child Tags')



class Stage(models.Model):
    #special fields
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence,name'

    #string fields
    name = fields.Char('Name', 40, translate=True)
    desc = fields.Text('Description')
    state = fields.Selection([('draft', 'New'), ('open', 'Started'), ('done', 'Closed')], 'State')
    docs = fields.Html('Documentation')

    #numeric fields
    sequence = fields.Integer('Sequence')
    per_complete = fields.Float('% Complete', (3,2))

    # Date fields:
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')

    # Other fields:
    isFolded = fields.Boolean('Folded?')
    image = fields.Binary('Image')