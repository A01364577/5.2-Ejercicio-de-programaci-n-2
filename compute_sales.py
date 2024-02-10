"""
This module computes the total cost of sales.
"""

import sys
import json
import time


def parse_arguments():

    """
    Parse command-line arguments.

    Returns:
        str: Filename of the price catalogue JSON file.
        str: Filename of the sales record JSON file.
    """
    if len(sys.argv) != 3:
        print("python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


def load_json(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        dict: Data loaded from the JSON file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Invalid JSON format in '{filename}'.")
        sys.exit(1)


def compute_total_cost(price_catalogue, sales_record):
    """
    Compute the total cost for all sales.

    Args:
        price_catalogue (list): List of products with their prices.
        sales_record (list): List of sales records.

    Returns:
        float: Total cost of all sales.
    """
    total_cost = 0
    for sale in sales_record:
        product_name = sale['Product']
        quantity = sale['Quantity']
        # Find product price in the catalogue
        for item in price_catalogue:
            if item['title'] == product_name:
                price = item['price']
                total_cost += price * quantity
                break  # Once found, no need to continue searching
        else:
            print(f"Price of '{product_name}' not found in catalogue.")
    return total_cost


def main():
    """
    Main function.
    """
    start_time = time.time()

    # Parse command-line arguments
    catalogue_file, sales_file = parse_arguments()

    # Load JSON files
    price_catalogue = load_json(catalogue_file)
    sales_record = load_json(sales_file)

    # Compute total cost
    total_cost = compute_total_cost(price_catalogue, sales_record)

    # Output results
    print("Total cost of all sales:", total_cost)
    with open("SalesResults.txt", "w", encoding='utf-8') as output_file:
        output_file.write(f"Total cost of all sales: {total_cost}\n")

    # Display execution time
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")


if __name__ == "__main__":
    main()
