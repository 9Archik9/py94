from flask import Flask, render_template, request
from sqlalchemy.orm import sessionmaker
from models import Article, engine

app = Flask(__name__, template_folder='templates')


@app.route('/')
def get_main_page():
    Session = sessionmaker(bind=engine)
    sess = Session()
    articles = sess.query(Article.header).all()
    num_articles = sess.query(Article).count()
    sess.close()
    return render_template('main_page.html', articles=articles, num_articles=num_articles)


@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        Session = sessionmaker(bind=engine)
        sess = Session()

        new_article = Article(header=title, content=content)
        sess.add(new_article)
        sess.commit()

        success = True
        sess.close()
        return render_template('add_article.html', success=success)

    return render_template('add_article.html', success=False)


if __name__ == '__main__':
    app.run()
