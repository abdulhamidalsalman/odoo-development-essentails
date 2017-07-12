{
    'name': 'To-Do Application',
    'description':'Manage your personal To-Do tasks.',
    'author':'Abdulhamid Alsalman',
    'depends': ['base'],
    'data': [
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml'],
    'application':True,
}