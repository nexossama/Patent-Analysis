import json

def remove_duplicates(json_file1, json_file2, unique_field):
    # Load data from JSON files
    with open(json_file1, 'r') as file:
        data1 = json.load(file)
    with open(json_file2, 'r') as file:
        data2 = json.load(file)

    # Extract unique identifiers from data1
    unique_ids_set = {item[unique_field] for item in data1}
    unique_ids_list = [item[unique_field] for item in data1]
    
    print(len(unique_ids_set))
    print(len(unique_ids_list))

    # Count and remove duplicates from data2
    removed_count = 0
    for i in range(len(data2)-1, -1, -1):
        if data2[i][unique_field] in unique_ids_set:
            data2.pop(i)
            removed_count += 1

    # Write modified data2 back to the file
    with open(f"{json_file2.split('.')[0]}_new.json", 'w') as file:
        json.dump(data2, file, indent=4)

    return removed_count

# Example usage:
json_file1 = 'data1.json'
json_file2 = 'data4.json'
unique_field = 'code'  # Replace 'code' with the unique identifier field in your JSON data

removed_count = remove_duplicates(json_file1, json_file2, unique_field)
print(f"Removed {removed_count} duplicate elements from {json_file2}")
