
from flask import Flask, request, jsonify
from sales_data import load_sales_data
from llm_integration import generate_feedback

app = Flask(__name__)

sales_data = load_sales_data("sales_performance_data.csv")  

@app.route('/api/feedback/<string:rep_name>', methods=['GET'])
def feedback(rep_name):
    """Endpoint to get performance feedback for a specific sales representative."""
    query = f"Provide performance feedback for sales representative: {rep_name}."
    feedback = generate_feedback(sales_data, query)
    return jsonify({"feedback": feedback})

@app.route('/api/team_performance', methods=['GET'])
def team_performance():
    """Endpoint to assess overall team performance."""
    query = "Provide insights on overall team performance."
    feedback = generate_feedback(sales_data, query)
    return jsonify({"feedback": feedback})

@app.route('/api/performance_trends', methods=['GET'])
def performance_trends():
    """Endpoint for sales performance trends and forecasting."""
    query = "Analyze sales performance trends and forecast future sales."
    feedback = generate_feedback(sales_data, query)
    return jsonify({"feedback": feedback})

if __name__ == '__main__':
    app.run(debug=True)
