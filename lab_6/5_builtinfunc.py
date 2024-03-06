def input_tuple():
    try:
        tuple_str = input("Enter elements of the tuple separated by commas: ")
        elements = tuple(eval(element) for element in tuple_str.split(','))
        my_tuple = tuple(elements)
        return my_tuple
    except Exception as e:
        print("Error:", e)
        return None


def all_elements_true(t):
    return all(t)

if __name__ == "__main__":
    my_tuple = input_tuple()
    result = all_elements_true(my_tuple)
    print("All elements of the tuple are True:", result)
