from flask import Flask, request, render_template

from sqlalchemy.orm import Session

from db import Product, engine


app = Flask(__name__)


@app.route('/product', methods=['POST', 'GET'])
def get_products():
    if request.method == 'GET':
        with Session(engine) as sss:
            products = sss.query(Product).all()
        return render_template('products.html', products=products)

    elif request.method == 'POST':
        product = Product(
            name=request.form['name'],
            carbs=float(request.form['carbs']),
            proteins=float(request.form['proteins']),
            fats=float(request.form['fats']),
            grs=float(request.form['grs']),
        )
        with Session(engine) as sss:
            sss.add(product)
            sss.commit()

            products = sss.query(Product).all()
        return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run()
