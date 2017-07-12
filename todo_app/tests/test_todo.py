# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestTodo(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super(TestTodo, self).setUp(*args, **kwargs)  # calls setUp method of the parent class
        user_demo = self.env.ref('base.user_demo')  # get Demo user reference
        self.env = self.env(user=user_demo)  # change enviroment to Demo user
        return result

    def test_create(self):
        "Create a simple todo"
        Todo = self.env['todo.task']
        task = Todo.create({'name':'Test Task'})
        #task = Todo.create({'name': 'Test Task', 'user_id': 5})
        self.assertEqual(task.is_done, False)


    def test_toggle_done(self):
        Todo = self.env['todo.task']
        task = Todo.create({'name':'Test Task'})
        #task = Todo.create({'name': 'Test Task', 'user_id': 5})
        task.do_toggle_done()
        self.assertTrue(task.is_done)

    def test_clear_done(self):
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        #task = Todo.create({'name': 'Test Task', 'user_id': 5})
        task.do_toggle_done()
        task.do_clear_done()
        self.assertFalse(task.active)

    def test_record_rule(self):
        "Test per user record rules"
        Todo = self.env['todo.task']
        task = Todo.sudo().create({'name': 'Admin Task'})#change context to admin user and use it to create a task which should not be accessiable to Demo user
        #task = Todo.sudo().create({'name': 'Admin Task', 'user_id':5})
        with self.assertRaises(AccessError):#trying to accesss this task created by admin user using demo user raises AccessError exception
            Todo.browse([task.id]).name
        