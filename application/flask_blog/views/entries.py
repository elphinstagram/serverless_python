# flask_blog/views/entries.py
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog.models.entries import Entry
from flask_login import login_required
from datetime import datetime

# show_entries 記事の一覧を表示


@app.route('/')
@login_required
def show_entries():
    entries = Entry. scan()
    entries = sorted(entries, key=lambda x: x.id, reverse=True)
    return render_template('entries/index.html', entries=entries)

# add_entry 記事を追加


@app.route('/entries', methods=['POST'])
@login_required
def add_entry():
    entry = Entry(id=int(datetime. now(). timestamp()),
                  title=request. form['title'], text=request.form['text'])
    entry. save()
    flash(' 新しく記事が作成されました')
    return redirect(url_for('show_entries'))

# new_entry 記事の新規追加フォームを表示


@app.route('/entries/new', methods=['GET'])
@login_required
def new_entry():
    return render_template('entries/new.html')

# show_entry　記事の詳細を表示


@app.route('/entries/<int:id>', methods=['GET'])
@login_required
def show_entry(id):
    entry = Entry.get(id)
    return render_template('entries/show.html', entry=entry)

# edit_entry(id)　記事の編集フォームを表示


@app.route('/entries/<int:id>/edit', methods=['GET'])
@login_required
def edit_entry(id):
    entry = Entry.get(id)
    return render_template('entries/edit.html', entry=entry)

# update_entry(id)　記事の更新


@app. route('/entries/< int: id >/update', methods=['POST'])
@login_required
def update_entry(id):
    entry = Entry.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    entry.save()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

# delete_entry 記事の削除


@app.route('/entries/<int:id >/delete', methods=['POST'])
@login_required
def delete_entry(id):
    entry = Entry.get(id)
    entry.delete()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))
