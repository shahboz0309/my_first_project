from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySQL konfiguratsiyasi

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'        # sizning MySQL user nomingiz
app.config['MYSQL_PASSWORD'] = 'your_password'  # sizning MySQL parolingiz
app.config['MYSQL_DB'] = 'social_site_db'

mysql = MySQL(app)

# Ro'yxatdan o'tish

@app.route('/register', methods=['POST'])
def register():
 data = request.get_json()
 username = data['username']
 password = generate_password_hash(data['password'])

 cursor = mysql.connection.cursor()
 cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
 mysql.connection.commit()
 cursor.close()

@app.route('/register', methods=['POST'])
def register():
 return jsonify({'message': 'Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi!'})


# Post qo‘shish

@app.route('/add_post', methods=['POST'])
def add_post():
 data = request.get_json()
 user_id = data['user_id']
 content = data['content']

 cursor = mysql.connection.cursor()
 cursor.execute("INSERT INTO posts (user_id, content) VALUES (%s, %s)", (user_id, content))
 mysql.connection.commit()
 cursor.close()

@app.route('/register', methods=['POST'])
def register():
 return jsonify({'message': 'Post muvaffaqiyatli qo‘shildi!'})


# Barcha postlarni olish

@app.route('/posts', methods=['GET'])
def get_posts():
 cursor = mysql.connection.cursor()
 cursor.execute("SELECT posts.id, users.username, posts.content, posts.created_at FROM posts JOIN users ON posts.user_id = users.id ORDER BY posts.created_at DESC")
 result = cursor.fetchall()
 cursor.close()

 posts = []
 for row in result:
    posts.append({
        'id': row[0],
        'username': row[1],
        'content': row[2],
        'created_at': str(row[3])
    })

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)
