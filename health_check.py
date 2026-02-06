# Simple Flask API demonstrating maintainable design.
# Each function is self-contained and clearly documented.

# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/status')
# def status():
#     """Health check endpoint for system monitoring."""
#     return jsonify(status="OK", message="Service running smoothly")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# Simple Flask API demonstrating maintainable design.
# Each function is self-contained and clearly documented.

from flask import Flask, jsonify
import logging
import sys

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/status')
def status():
    """Health check endpoint for system monitoring."""
    try:
        # Add actual health checks here (database connectivity, etc.)
        return jsonify(status="OK", message="Service running smoothly"), 200
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify(status="ERROR", message="Service experiencing issues"), 500

@app.route('/health')
def health():
    """Detailed health check with system information."""
    try:
        health_data = {
            "status": "healthy",
            "service": "health-check-api",
            "version": "1.0.0"
        }
        return jsonify(health_data), 200
    except Exception as e:
        logger.error(f"Detailed health check failed: {str(e)}")
        return jsonify(status="unhealthy", error=str(e)), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors gracefully."""
    return jsonify(error="Endpoint not found"), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify(error="Internal server error"), 500

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        sys.exit(1)