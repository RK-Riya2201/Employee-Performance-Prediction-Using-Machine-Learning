from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('gwp.pkl', 'rb'))

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/predict")
def predict_page():
    return render_template('predict.html')

@app.route("/submit", methods=['POST'])
def submit_prediction():
    # Map categorical values if needed (here assume numeric values are sent from form)
    quarter = int(request.form['quarter'])
    department = int(request.form['department'])
    day = int(request.form['day'])
    team = int(request.form['team'])
    targeted_productivity = float(request.form['targeted_productivity'])
    smv = float(request.form['smv'])
    over_time = int(request.form['over_time'])
    incentive = int(request.form['incentive'])
    idle_time = float(request.form['idle_time'])
    idle_men = int(request.form['idle_men'])
    no_of_style_change = int(request.form['no_of_style_change'])
    no_of_workers = float(request.form['no_of_workers'])
    month = int(request.form['month'])

    total = [[
        quarter, department, day, team, targeted_productivity,
        smv, over_time, incentive, idle_time, idle_men,
        no_of_style_change, no_of_workers, month
    ]]

    prediction = model.predict(total)[0]  # Get scalar value

    # Convert prediction score to text
    if prediction < 0.3:
        text = 'Low Productive'
    elif prediction < 0.8:
        text = 'Medium Productive'
    else:
        text = 'Highly Productive'

    # Pass both text and numeric score to template
    return render_template('submit.html', prediction_text=text, prediction_score=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)
