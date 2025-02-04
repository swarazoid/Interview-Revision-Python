from datetime import datetime
import base64
import json

# Sample transaction dataset
TRANSACTIONS = [
    {"id": 1, "userid": 101, "currency": "USD", "amount": 150.5, "time": "2025-02-04T10:00:00"},
    {"id": 2, "userid": 102, "currency": "EUR", "amount": 200.0, "time": "2025-02-04T10:05:00"},
    {"id": 3, "userid": 101, "currency": "USD", "amount": 99.9, "time": "2025-02-04T10:10:00"},
    {"id": 4, "userid": 103, "currency": "INR", "amount": 5000.0, "time": "2025-02-04T10:15:00"},
    {"id": 5, "userid": 102, "currency": "USD", "amount": 300.0, "time": "2025-02-04T10:20:00"},
    {"id": 6, "userid": 104, "currency": "USD", "amount": 250.0, "time": "2025-02-04T10:25:00"},
    {"id": 7, "userid": 105, "currency": "GBP", "amount": 100.0, "time": "2025-02-04T10:30:00"},
    {"id": 8, "userid": 106, "currency": "USD", "amount": 500.0, "time": "2025-02-04T10:35:00"},
    {"id": 9, "userid": 107, "currency": "EUR", "amount": 700.0, "time": "2025-02-04T10:40:00"},
    {"id": 10, "userid": 108, "currency": "INR", "amount": 2000.0, "time": "2025-02-04T10:45:00"},
    {"id": 11, "userid": 109, "currency": "USD", "amount": 450.0, "time": "2025-02-04T10:50:00"},
    {"id": 12, "userid": 110, "currency": "INR", "amount": 750.0, "time": "2025-02-04T10:55:00"},
    {"id": 13, "userid": 111, "currency": "USD", "amount": 320.0, "time": "2025-02-04T11:00:00"},
    {"id": 14, "userid": 112, "currency": "EUR", "amount": 600.0, "time": "2025-02-04T11:05:00"},
    {"id": 15, "userid": 113, "currency": "USD", "amount": 1100.0, "time": "2025-02-04T11:10:00"}
]


# Function to filter transactions
def filter_transactions(transactions, filters):
    filtered = transactions
    for key, value in filters.items():
        if key in {"userid", "currency"}:
            filtered = [txn for txn in filtered if txn[key] == value]
        elif key == "min_amount":
            filtered = [txn for txn in filtered if txn["amount"] >= value]
        elif key == "max_amount":
            filtered = [txn for txn in filtered if txn["amount"] <= value]
    return filtered

# Cursor-based pagination implementation
# def encode_cursor(last_item):
#     return base64.urlsafe_b64encode(json.dumps({"id": last_item["id"], "time": last_item["time"]}).encode()).decode()

# def decode_cursor(cursor):
#     try:
#         return json.loads(base64.urlsafe_b64decode(cursor).decode())
#     except Exception:
#         return None

# Simplified cursor encoding and decoding without base64
def encode_cursor(last_item):
    # Directly encode the cursor using a JSON string representation
    return json.dumps({"id": last_item["id"], "time": last_item["time"]})

def decode_cursor(cursor):
    try:
        return json.loads(cursor)
    except Exception:
        return None

def cursor_paginate(transactions, limit, cursor, filters):
    transactions = filter_transactions(transactions, filters)
    
    if cursor:
        cursor_data = decode_cursor(cursor)
        if cursor_data:
            transactions = [txn for txn in transactions if txn["time"] > cursor_data["time"] or (txn["time"] == cursor_data["time"] and txn["id"] > cursor_data["id"])]
    
    paginated_data = transactions[:limit]
    next_cursor = encode_cursor(paginated_data[-1]) if len(paginated_data) == limit else None
    
    return {"data": paginated_data, "nextLink": next_cursor}




# Modular driver code for pagination with loop
def paginate_transactions(transactions, limit, filters):
    cursor = None
    page_number = 1
    while True:
        paginated_data = cursor_paginate(transactions, limit, cursor, filters)
        
        if not paginated_data["data"]:
            break
        
        print(f"Page {page_number}: {paginated_data['data']}")
        
        cursor = paginated_data["nextLink"]
        
        if not cursor:
            break
        
        page_number += 1

# Example usage of the modular pagination function
filters = {"userid": 101, "min_amount": 100}  # Apply filters (e.g., transactions for user 101 with min amount 100)
paginate_transactions(TRANSACTIONS, limit=5, filters=filters)  # Paginate with a limit of 5 per page