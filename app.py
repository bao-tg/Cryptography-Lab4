from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

def query_db(query):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        column_names = [description[0] for description in cursor.description] if cursor.description else []
        return {'columns': column_names, 'rows': result}
    except Exception as e:
        return {'error': str(e)}
    finally:
        conn.close()

def get_image_list():
    image_folder = os.path.join(app.static_folder, 'image')
    return os.listdir(image_folder) if os.path.exists(image_folder) else []

@app.route('/')
def index():
    links = [
        {"label": "Show All Products", "query": "SELECT * FROM products"},
        {"label": "Products Under $1", "query": "SELECT * FROM products WHERE price < 1"},
        {"label": "Out of Stock (stock=0)", "query": "SELECT * FROM products WHERE stock = 0"}
    ]
    images = get_image_list()
    return render_template('index.html', links=links, images=images)

@app.route('/vuln_upload', methods=['GET', 'POST'])
def vuln_upload():
    if request.method == 'POST':
        file = request.files['image']
        filename = file.filename  
        filepath = os.path.join('static/image', filename)
        file.save(filepath)
    links = [
        {"label": "Show All Products", "query": "SELECT * FROM products"},
        {"label": "Products Under $1", "query": "SELECT * FROM products WHERE price < 1"},
        {"label": "Out of Stock (stock=0)", "query": "SELECT * FROM products WHERE stock = 0"}
    ]
    images = get_image_list()
    return render_template('index.html', links=links, images=images)

@app.route('/query')
def run_query():
    sql = request.args.get('sql')
    if not sql:
        return jsonify({'error': 'No SQL query provided'})
    result = query_db(sql)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

