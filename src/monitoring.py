```python
import logging
from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

# Initialize Flask application
app = Flask(__name__)

# Initialize Prometheus Metrics for Flask
metrics = PrometheusMetrics(app)

# Enable default metrics for Prometheus
metrics.info('app_info', 'Application info', version='1.0.0')

# Custom metric for monitoring API requests
api_requests_total = metrics.counter(
    'api_requests_total', 'Total number of API requests',
    labels={'endpoint': lambda: request.endpoint}
)

@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint to ensure the application is running.
    """
    return jsonify({"status": "healthy"}), 200

@app.route('/api/data', methods=['GET'])
@api_requests_total
def get_data():
    """
    Example endpoint to demonstrate API functionality and monitoring.
    """
    # Simulate data retrieval process
    data = {"message": "Data fetched successfully"}
    return jsonify(data), 200

if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=5000)
```