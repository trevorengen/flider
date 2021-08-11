import os
def Flider():
    try:
        os.mkdir('flask_app')
        dirs = ['templates', 'config', 'models', 'controllers', 
        'static', 'static/css', 'static/js', 'static/img']
        for dir in dirs:
            os.mkdir('flask_app/'+dir)
    except Exception as e:
        print(e)
        print('Continuing...')
    save_paths = ['flask_app/templates/', 'flask_app/config', 'flask_app/', 'flask_app/static/css/', 'flask_app/static/js/']
    file_names = ['index.html', 'mysqlcontroller.py', '__init__.py', 'style.css', 'scripts.js']
    for i in range(len(save_paths)):
        try:
            completeName = os.path.join(save_paths[i], file_names[i])
            file = open(completeName, 'w')
            file.close()
        except Exception as e:
            print(e)
            print('Error on: ' + save_paths[i] + file_names[i])
