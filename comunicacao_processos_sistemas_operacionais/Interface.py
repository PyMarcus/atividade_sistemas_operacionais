from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


client_storage = list()
server_storage = list()


@app.route('/client', methods=['GET', 'POST'])
def client():
    if request.method == "POST":
        client_storage.append(request.form['message'])
        redirect(url_for('server'))
        return redirect(url_for('client'))
    else:
        return render_template('client.html', data=server_storage)


@app.route('/server', methods=['GET', 'POST'])
def server():
    if request.method == "POST":
        server_storage.append(request.form['message'])

        return redirect(url_for('server'))
    else:
        return render_template('server.html', data=client_storage)


@app.route('/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
