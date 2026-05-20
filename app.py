from flask import Flask, render_template, request

app = Flask(__name__)


# ------------------- HEALTH CHECK FUNCTION ------------------- #
def health_insights(name, age, weight, height, bp, sugar, pulse):

    insights = []

    # BMI Calculation
    bmi = weight / ((height / 100) ** 2)

    # ---------------- BMI CHECK ---------------- #
    if bmi < 18.5:
        bmi_status = "Underweight"
        insights.append(
            f"Your BMI is {bmi:.1f}. You are Underweight "
            f"(Normal BMI: 18.5 - 24.9)."
        )

    elif 18.5 <= bmi <= 24.9:
        bmi_status = "Healthy"
        insights.append(
            f"Your BMI is {bmi:.1f}. You are in a Healthy range "
            f"(Normal BMI: 18.5 - 24.9)."
        )

    else:
        bmi_status = "Overweight"
        insights.append(
            f"Your BMI is {bmi:.1f}. You are Overweight "
            f"(Normal BMI: 18.5 - 24.9)."
        )

    # ---------------- BLOOD PRESSURE CHECK ---------------- #
    if bp < 90:
        bp_status = "Low"
        insights.append(
            "Your Blood Pressure is Low "
            "(Normal BP: 90 - 120 mmHg)."
        )

    elif 90 <= bp <= 120:
        bp_status = "Normal"
        insights.append(
            "Your Blood Pressure is Normal "
            "(Normal BP: 90 - 120 mmHg)."
        )

    else:
        bp_status = "High"
        insights.append(
            "Your Blood Pressure is High "
            "(Normal BP: 90 - 120 mmHg)."
        )

    # ---------------- SUGAR LEVEL CHECK ---------------- #
    if sugar < 70:
        sugar_status = "Low"
        insights.append(
            "Your Sugar Level is Low "
            "(Normal Sugar: 70 - 140 mg/dL)."
        )

    elif 70 <= sugar <= 140:
        sugar_status = "Normal"
        insights.append(
            "Your Sugar Level is Normal "
            "(Normal Sugar: 70 - 140 mg/dL)."
        )

    else:
        sugar_status = "High"
        insights.append(
            "Your Sugar Level is High "
            "(Normal Sugar: 70 - 140 mg/dL)."
        )

    # ---------------- PULSE RATE CHECK ---------------- #
    if pulse < 60:
        pulse_status = "Low"
        insights.append(
            "Your Pulse Rate is Low "
            "(Normal Pulse: 60 - 100 bpm)."
        )

    elif 60 <= pulse <= 100:
        pulse_status = "Normal"
        insights.append(
            "Your Pulse Rate is Normal "
            "(Normal Pulse: 60 - 100 bpm)."
        )

    else:
        pulse_status = "High"
        insights.append(
            "Your Pulse Rate is High "
            "(Normal Pulse: 60 - 100 bpm)."
        )

    # ---------------- OVERALL HEALTH STATUS ---------------- #
    health_status = "Good"

    if (
        bmi_status != "Healthy"
        or bp_status != "Normal"
        or sugar_status != "Normal"
        or pulse_status != "Normal"
    ):
        health_status = "Needs Attention"

    return insights, health_status, bmi


# ------------------- HOME PAGE ------------------- #
@app.route('/')
def index():
    return render_template('index.html')


# ------------------- ANALYZE ROUTE ------------------- #
@app.route('/analyze', methods=['POST'])
def analyze():

    # Get form data
    name = request.form['name']
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bp = int(request.form['bp'])
    sugar = int(request.form['sugar'])
    pulse = int(request.form['pulse'])

    # Process health data
    insights, health_status, bmi = health_insights(
        name,
        age,
        weight,
        height,
        bp,
        sugar,
        pulse
    )

    # Send results to HTML page
    return render_template(
        'result.html',
        name=name,
        age=age,
        bmi=round(bmi, 1),
        bp=bp,
        sugar=sugar,
        pulse=pulse,
        insights=insights,
        health_status=health_status
    )


# ------------------- RUN APPLICATION ------------------- #
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
