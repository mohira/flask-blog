from flask import Flask, render_template

app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/not_exist')
def not_exist_template():
    return render_template('not_exist.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
