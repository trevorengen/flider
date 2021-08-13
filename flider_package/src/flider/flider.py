import os
import pkg_resources
import argparse


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
    save_paths = ['flask_app/templates/', 'flask_app/config/', 'flask_app/', 'flask_app/static/css/', 'flask_app/static/js/', '']
    file_names = ['index.html', 'mysqlcontroller.py', '__init__.py', 'style.css', 'scripts.js', 'server.py']
    read_names = ['index.txt', 'mysqlcontroller.txt', 'init.txt', 'style.txt', 'scripts.txt', 'server.txt']
    parser = argparse.ArgumentParser(description='Contact me on github if you have any problems!\ngithub.com/trevorengen')
    parser.add_argument('-f', '--full', action='store_true', help='Installs all available default files.')
    is_full_install = parser.parse_args()
    if is_full_install:
        save_paths.append(['flask_app/models/', 'flask_app/controllers/'])
        file_names.append(['user.py', 'users.py'])
        read_names.append(['user.txt', 'users.txt'])
    for i in range(len(save_paths)):
        try:
            # os.path.dirname() gets the file name with the file dunder ONLY because this
            # module is not called directly. Directly calling this module will cause
            # the save to cease to work.
            save_path = os.path.dirname(__file__)
            completeName = os.path.join(save_paths[i], file_names[i])
            read_file = open(save_path + '/' + read_names[i], 'r')
            write_file = open(completeName, 'w')
            write_file.write(read_file.read())
            write_file.close()
            read_file.close()
        except Exception as e:
            print(e)
            print('Error on: ' + save_paths[i] + file_names[i])
