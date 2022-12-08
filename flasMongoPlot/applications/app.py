from flask import Flask, render_template
import pymongo

app = Flask(__name__)

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

client = pymongo.MongoClient("mongodb+srv://Useradmin:DataProg22@project.uzho4ty.mongodb.net/?retryWrites=true&w=majority")
db = client['ProjectDP']


@app.route('/')
def dashboard():
	ls = []
	for x in db.Payments_1.find({},{"_id":0, "Payment":1, "Total":1}):
		for i in x.values():
			ls.append(i)

	y = Convert(ls)
	x2 = {'Type': 'Quantity'}
	pay = {**x2, **y}

	ls1 = []
	for x1 in db.Sales_1.find({},{"_id":0, "Product line":1, "Quantity":1}):
		for i1 in x1.values():
			ls1.append(i1)

	y1 = Convert(ls1)
	x3 = {'ProductLine': 'Quantity'}
	sell = {**x3, **y1}

	ls2 = []
	for x4 in db.Buyers_1.find({},{"_id":0, "Gender":1, "Customer type":1}):
		for i2 in x4.values():
			ls2.append(i2)

	y2 = Convert(ls2)
	x5 = {'Gender': 'Customer'}
	buyy = {**x5, **y2}

	return render_template('home.html', pay=pay, sell=sell, buyy=buyy)



@app.route('/payment')
def pie_chart_pay():
	ls = []
	for x in db.Payments_1.find({},{"_id":0, "Payment":1, "Total":1}):
		for i in x.values():
			ls.append(i)

	y = Convert(ls)
	x2 = {'Type': 'Quantity'}
	data = {**x2, **y}
	return render_template('index.html', data=data)


@app.route('/sale')
def bar_chart_sale():
	ls1 = []
	for x1 in db.Sales_1.find({},{"_id":0, "Product line":1, "Quantity":1}):
		for i1 in x1.values():
			ls1.append(i1)

	y1 = Convert(ls1)
	x3 = {'ProductLine': 'Quantity'}
	data1 = {**x3, **y1}
	return render_template('third.html', data1=data1)



@app.route('/buyer')
def pie_chart_buy():
	ls = []
	for x in db.Buyers_1.find({},{"_id":0, "Gender":1, "Customer type":1}):
		for i in x.values():
			ls.append(i)

	y = Convert(ls)
	x3 = {'Gender': 'Customer'}
	data = {**x3, **y}
	return render_template('four.html', data=data)




if __name__ == "__main__":
	app.run()