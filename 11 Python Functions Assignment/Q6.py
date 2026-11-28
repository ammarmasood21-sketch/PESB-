# Create a function
def chunk_list(items, size):

    result = []

    # Move through the list by size
    for i in range(0, len(items), size):

        # Take items according to size
        part = items[i:i + size]

        # Add the small list to result
        result.append(part)

    return result


items = [1, 2, 3, 4, 5, 6, 7]

print(chunk_list(items, 3))