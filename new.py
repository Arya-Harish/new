from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/products', methods=['POST'])
def upload_products():
    # Get JSON data from the request
    data = request.get_json()
    
    # Check if the data is a list and has up to 500 products
    if not isinstance(data, list) or len(data) > 500:
        return jsonify({'error': 'Invalid input. Please submit a JSON batch of up to 500 products.'}), 400

    errors = []
    
    # Validate each product in the batch
    for product in data:
        if not validate_product(product):
            errors.append(generate_error(product))

    if errors:
        return jsonify({'error': 'Validation failed', 'errors': errors}), 400

    result = save_products_atomic(data)
    return jsonify(result), 200


def validate_product(product):
    required_fields = ['ProductID', 'Name', 'Category', 'Price', 'StockQuantity']
    for field in required_fields:
        if field not in product:
            return False
    return True


def generate_error(product):
    return f"Product {product.get('ProductID', 'unknown')} is missing required fields."


def save_products_atomic(products):
    # Simulate database save with atomic transaction logic
    try:
        # Begin transaction (pseudocode)
        for product in products:
            # Insert product into database (pseudocode)
            pass  # Replace with actual database insert logic
        # Commit transaction (pseudocode)
        return {'message': 'Products saved successfully.'}
    except Exception as e:
        # Rollback transaction (pseudocode)
        return {'error': 'Database write failed, no products saved.'}


if __name__ == '__main__':
    app.run(debug=True)