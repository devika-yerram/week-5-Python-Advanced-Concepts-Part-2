import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename="transaction_errors.log", level=logging.ERROR)

# Custom exceptions
class InvalidTransactionError(Exception):
    pass

class TransactionProcessingError(Exception):
    pass

# Error Logging Function
def log_error(error_message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.error(f"{timestamp} - {error_message}")

# Validate transaction data
def validate_transaction(transaction):
    try:
        amount = float(transaction.get("amount", 0))
        if amount <= 0:
            raise InvalidTransactionError("Transaction amount must be greater than zero.")
        return True
    except ValueError:
        raise InvalidTransactionError("Invalid amount. Please enter a numeric value.")

# Process a single transaction
def process_transaction(transaction):
    try:
        # Validate transaction data
        if validate_transaction(transaction):
            # Simulate transaction processing
            print(f"Processing transaction for {transaction['name']}: ${transaction['amount']}")
            # Additional processing logic here
            print("Transaction processed successfully.")
    except InvalidTransactionError as e:
        log_error(f"InvalidTransactionError: {e}")
        print(f"Error
