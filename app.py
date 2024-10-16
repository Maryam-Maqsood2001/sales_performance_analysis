from flask import Flask, jsonify, request
import pandas as pd
from llm_integration import generate_insights

app = Flask(__name__)

# Load the sales data
sales_data = pd.read_csv('sales_performance_data.csv')

# Endpoint: Individual Sales Representative Performance Analysis
@app.route('/api/rep_performance', methods=['GET'])
def rep_performance():
    rep_id = request.args.get('rep_id')
    rep_data = sales_data[sales_data['employee_id'] == int(rep_id)]
    
    if rep_data.empty:
        return jsonify({"error": "Sales representative not found"}), 404
    
    prompt = f"Analyze the following sales performance data: {rep_data.to_dict(orient='records')}"
    insights = generate_insights(prompt)
    
    return jsonify({
        "rep_id": rep_id,
        "performance": rep_data.to_dict(orient='records'),
        "insights": insights
    })

# Endpoint: Overall Sales Team Performance Summary
@app.route('/api/team_performance', methods=['GET'])
def team_performance():
    prompt = f"Summarize the overall performance of the sales team based on the following data: {sales_data.to_dict(orient='records')}"
    insights = generate_insights(prompt)
    
    return jsonify({
        "team_performance": sales_data.describe().to_dict(),
        "insights": insights
    })

# Endpoint: Sales Performance Trends and Forecasting
@app.route('/api/performance_trends', methods=['GET'])
def performance_trends():
    time_period = request.args.get('time_period', 'monthly')  # Default to 'monthly'
    
    # Generate a basic trend analysis (this can be enhanced)
    trends_summary = sales_data[['created', 'lead_taken', 'tours_booked', 'applications']].resample(time_period).sum()
    prompt = f"Analyze the following sales trends for the period: {trends_summary.to_dict(orient='records')}"
    insights = generate_insights(prompt)
    
    return jsonify({
        "trends": trends_summary.to_dict(),
        "insights": insights
    })

if __name__ == '__main__':
    app.run(debug=True)
