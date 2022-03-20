from flask import Flask

app = Flask(__name__)

header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'


# @app.route('/')
# def root():
#     return 'This is home'


@app.route('/get_name/<name>')
def hello_world(name='World'):  # put application's code here

    app.post('What')
    app.logger.info('Hello')
    return f'<title>Hello</title><p> Hello {name}!</p><br><p><a href="/">Back</a></p>\n'


@app.route('/secret/name')
def not_important():
    return 'LOL'


if __name__ == '__main__':
    app.add_url_rule('/', 'index', (lambda: header_text + instructions + footer_text))
    app.run()
