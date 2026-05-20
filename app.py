from flask import Flask, render_template, request

app = Flask(__name__)

# ------------------- HEALTH CHECK ------------------- #
def health_insights(name, age, weight, height, bp, sugar, pulse):
    insights = []

    bmi = weight / ((height / 100) ** 2)

    # BMI Check
    if bmi < 18.5:
        insights.append(f"Your BMI is {bmi:.1f} → Underweight.")
    elif 18.5 <= bmi < 24.9:
        insights.append(f"Your BMI is {bmi:.1f} → Healthy range.")
    else:
        insights.append(f"Your BMI is {bmi:.1f} → Overweight.")

    # Blood Pressure Check
    if bp < 90:
        insights.append("Low Blood Pressure.")
    elif 90 <= bp <= 120:
        insights.append("Normal Blood Pressure.")
    else:
        insights.append("High Blood Pressure.")

    # Sugar Check
    if sugar < 70:
        insights.append("Low Sugar Level.")
    elif 70 <= sugar <= 140:
        insights.append("Normal Sugar Level.")
    else:
        insights.append("High Sugar Level.")

    # Pulse Check
    if pulse < 60:
        insights.append("Low Pulse Rate.")
    elif 60 <= pulse <= 100:
        insights.append("Normal Pulse Rate.")
    else:
        insights.append("High Pulse Rate.")

    # Overall Status
    overall_status = "good"

    for text in insights:
        if any(word in text.lower() for word in ["underweight", "overweight", "low", "high"]):
            overall_status = "bad"
            break

    return insights, overall_status


# ------------------- ROUTES ------------------- #
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    name = request.form['name']
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bp = int(request.form['bp'])
    sugar = int(request.form['sugar'])
    pulse = int(request.form['pulse'])

    bmi = weight / ((height / 100) ** 2)

    insights, overall_status = health_insights(
        name,
        age,
        weight,
        height,
        bp,
        sugar,
        pulse
    )

    return render_template(
        'result.html',
        name=name,
        insights=insights,
        overall_status=overall_status,
        bmi=round(bmi, 1),
        bp=bp,
        sugar=sugar,
        pulse=pulse
    )


# ------------------- DEPLOY ------------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
