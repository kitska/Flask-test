from flask import Flask, render_template, flash, redirect, url_for
from forms import YearForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = YearForm()
    if form.validate_on_submit():
        year = form.year.data
        result = is_leap_year(year)
        if result:
            flash(f"{year} є високосним роком!", "success")
            image = "assets/yes.png"
        else:
            flash(f"{year} не є високосним роком.", "danger")
            image = "assets/no.png"
        return render_template('result.html', year=year, result=result, image=image)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
