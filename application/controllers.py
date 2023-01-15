from flask import current_app as app
from flask import render_template, request, url_for, flash, redirect
from application.database import get_posts,get_post,create_post,edit_post,delete_post

@app.route('/')
def index():
  return render_template('index.html',posts = get_posts())

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!', 'danger')
    else:
      create_post(title,content)
      flash('"{}" was successfully created!'.format(title),'success')
      return redirect(url_for('index'))

  return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
  post = get_post(id)
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']
    if not title:
      flash('Title is required!','danger')
    else:
      edit_post(title, content, id)
      flash('"{}" was successfully updated!'.format(title),'warning')
      return redirect(url_for('index'))

  return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
  post = get_post(id)
  delete_post(id)
  flash('"{}" was successfully deleted!'.format(post['title']),'danger')
  return redirect(url_for('index'))