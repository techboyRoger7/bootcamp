"""
This program finds the most frequent integer in a list.

The idea is similar to counting votes: 
    1. Each number gets one count every time we see it.
    2. A dictionary stores each number and how many times it has appeared.
    3. While counting, we keep track of the number with the highest count so far.
    4. If another number only ties the highest count, we keep the earlier answer.
"""

def get_most_frequent_occurrence(numbers: list[int]) -> int | None:
    """
    Return the integer that appears most frequently in the list.

    If multiple integers have the same highest frequency, return the one
    that first became the most frequent while reading from left to right.
    """
    
    if len(numbers) == 0:
        print("numbers must not be empty")
        return None

    most_frequent_num = numbers[0]
    occurrence_dict = dict()
    highest_count = 0 

    for i in range(len(numbers)):

        if numbers[i] not in occurrence_dict:
            occurrence_dict[numbers[i]] = 1
        else:
            occurrence_dict[numbers[i]] += 1
        
        if occurrence_dict[numbers[i]] > highest_count:
            most_frequent_num = numbers[i]
            highest_count = occurrence_dict[numbers[i]]
    
    return most_frequent_num
    
    

if __name__ == "__main__":
    print(get_most_frequent_occurrence([1, 2, 3, 3, 3, 4, 4, 5]))
    print(get_most_frequent_occurrence([1, 2, 2, 3, 4, 4]))
    print(get_most_frequent_occurrence([]))