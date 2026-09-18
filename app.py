import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Fixed emission factors
EMISSION_FACTORS = {
    'car': 0.20,
    'bus': 0.08,
    'flight': 0.25,
    'electricity': 0.80,
    'veg_meal': 0.50,
    'non_veg_meal': 2.00
}

activities = []
weekly_target = 50.0
error_msg = None

@app.route('/')
def index():
    global error_msg
    category_filter = request.args.get('category', 'all')
    
    if category_filter != 'all':
        filtered_activities = [a for a in activities if a['type'] == category_filter]
    else:
        filtered_activities = activities

    total_footprint = sum(a['co2'] for a in activities)
    trees_needed = round(total_footprint / 21, 1)
    
    breakdown = {}
    for a in activities:
        breakdown[a['type']] = breakdown.get(a['type'], 0) + a['co2']

    current_error = error_msg
    error_msg = None

    return render_template(
        'index.html',
        activities=filtered_activities,
        total_footprint=round(total_footprint, 2),
        weekly_target=weekly_target,
        breakdown=breakdown,
        selected_category=category_filter,
        error_msg=current_error,
        trees_needed=trees_needed
    )

@app.route('/add_activity', methods=['POST'])
def add_activity():
    global error_msg
    activity_type = request.form.get('type')
    
    raw_quantity = request.form.get('quick_quantity') or request.form.get('quantity')
    
    if not raw_quantity:
        return redirect(url_for('index'))

    try:
        quantity = float(raw_quantity)
    except (ValueError, TypeError):
        return redirect(url_for('index'))

    if quantity <= 0:
        error_msg = "Please enter a valid positive number."
        return redirect(url_for('index'))
    elif quantity > 50000:
        error_msg = f"Absurd Entry Blocked: {quantity:,.0f} units exceeds the realistic threshold of 50,000."
        return redirect(url_for('index'))

    factor = EMISSION_FACTORS.get(activity_type, 0)
    co2 = round(quantity * factor, 2)

    activities.insert(0, {
        'type': activity_type,
        'quantity': quantity,
        'co2': co2,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M')
    })
    return redirect(url_for('index'))

@app.route('/set_target', methods=['POST'])
def set_target():
    global weekly_target
    try:
        new_target = float(request.form.get('target'))
        if new_target > 0:
            weekly_target = new_target
    except (ValueError, TypeError):
        pass
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    global activities, weekly_target, error_msg
    activities.clear()
    weekly_target = 50.0
    error_msg = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
