from flask import Flask, jsonify, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Excel data reading
def read_excel_data():
    df = pd.read_csv('sales_data.csv')
    # print(df)
    return df

# SQL data reading
def read_sql_data():
    engine = create_engine('sqlite:///sales.db')
    df = pd.read_sql('SELECT * FROM sales', con=engine)
    return df

# Endpoint for Excel data
@app.route('/api/excel', methods=['GET'])
def get_excel_data():
    df = read_excel_data()
    return jsonify(df.to_dict(orient='records'))

# Endpoint for SQL data
@app.route('/api/sql', methods=['GET'])
def get_sql_data():
    df = read_sql_data()
    return jsonify(df.to_dict(orient='records'))

# Endpoint for sales data filtering
@app.route('/api/sales', methods=['GET'])
def get_sales_data():
    source = request.args.get('source', 'excel')
    if source == 'excel':
        df = read_excel_data()
    else:
        df = read_sql_data()
    
    product = request.args.get('product')
    if product:
        df = df[df['Product'] == product]

    region = request.args.get('region')
    if region:
        df = df[df['Region'] == region]

    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
