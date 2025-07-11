# Assignment 1 
'''
The provided file_type_aggregator function is intended to decorate other functions. It assumes that the function it decorates has exactly 2 positional arguments.
'''

def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts
        # return result

    return wrapper
'''
Create a process_doc function that's decorated by file_type_aggregator. It should return the following string:
f"Processing doc: '{doc}'. File Type: {file_type}"

'''
@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"

def runner():
    process_doc("here we go guys", "docx")
    process_doc("alright, let's go to Abu Dhabi", "txt")
    process_doc("And you Brutus?", "txt")



# Example 1 
def vowel_counter(func):
    vowel_count = 0 
    def wrapper(doc):
        nonlocal vowel_count
        vowels = "aeiouAEIOU"
        for char in doc: 
            if char in vowels:
                vowel_count += 1
        print(f"Vowel count: {vowel_count}")
        return(func(doc))
    return wrapper

@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")


def process_doc2(doc):
    print(f"Document: {doc}")


def runner_deco1():
    # process_doc("I don't know how this thing works")
    transformed_func = vowel_counter(process_doc2)
    transformed_func("I don't know how this thing works")
    

runner()