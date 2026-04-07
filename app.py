from flask import Flask, render_template, request
from src.prediction import predict_churn

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    prediction = None
    probability = None
    total = None
    category = None

    if request.method == "POST":

        tenure = float(request.form["tenure"])
        monthly = float(request.form["monthly_charges"])
        gender = int(request.form["gender"])
        contract = int(request.form["contract"])
        internet = int(request.form["internet"])
        payment = int(request.form["payment"])

        # total charges
        total = tenure * monthly

        # customer category
        if tenure < 6:
            category = "New Customer"
        elif tenure < 24:
            category = "Regular Customer"
        else:
            category = "Loyal Customer"

        data = [tenure, monthly, total, gender, contract, internet, payment]

        prediction, probability = predict_churn(data)

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        total=total,
        category=category
    )


if __name__ == "__main__":
    app.run(debug=True)