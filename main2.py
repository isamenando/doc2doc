def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    # return smallest of the two middle elements in even length list
    # This is the functional version of the solution
    # In essence, this single line:
    # Handles the sorting
    # Calculates the correct index for both odd and even length lists (following the specific rule for even lists in this problem)
    # Retrieves the value at that index.
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]

    # In contrast, This is how we would write the imperative version of the solution
    # sorted_list = sorted(font_sizes)
    # if len(sorted_list) % 2 == 0:
    #     return sorted_list[(len(sorted_list) // 2) - 1]
    # return sorted_list[(len(sorted_list) // 2)]