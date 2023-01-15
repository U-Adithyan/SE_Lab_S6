import sqlite3
from flask import current_app as app
from werkzeug.exceptions import abort

def get_db_connection():
  conn = sqlite3.connect(app.config['DATABASE'])
  conn.row_factory = sqlite3.Row
  return conn


def get_posts():
  conn = get_db_connection()
  posts = conn.execute('SELECT * FROM posts').fetchall()
  conn.close()
  return posts

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def create_post(title,content):
  conn = get_db_connection()
  conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
  conn.commit()
  conn.close()
  return 200

def edit_post(title, content, id):
  conn = get_db_connection()
  conn.execute('UPDATE posts SET title = ?, content = ?'
               ' WHERE id = ?',
               (title, content, id))
  conn.commit()
  conn.close()
  return 200

def delete_post(id):
  conn = get_db_connection()
  conn.execute('DELETE FROM posts WHERE id = ?', (id,))
  conn.commit()
  conn.close()