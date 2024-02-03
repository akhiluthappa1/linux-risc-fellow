def process_list(input_list):
    # Check if the list length is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError("The list length must be a multiple of 10.")
    
    # Remove items at positions which are a multiple of 2 or 3
    filtered_list = [item for index, item in enumerate(input_list, start=1) if index % 2 != 0 and index % 3 != 0]
    
    return filtered_list

# Main function( entry point)
if __name__ == "__main__":
    try:
        input_list = [int(x) for x in input("Enter a list of integers separated by space: ").split()]
        result = process_list(input_list)
        print("Processed list:", result)
    except ValueError as e:
        print(e)
