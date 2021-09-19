# Name: Elaf Abdullah Saleh Alhaddad
# Student ID: 31063977
# Assignment 1 = Task 1


def sort_counting_num(unsorted_list, col):
    """
    This function is used to perform the counting sort step in radix sort
    :param unsorted_list: The list that will be sorted
    :param col: the column that we are sorting in the list of numbers
    :return: the sorted list
    :Time complexity: O(N) - N is the number of elements in the list
    :Auxiliary space complexity: O(N) - N is the number of elements in the list
    """

    base = 10
    # creating the count array
    count_array = [None] * (9 + 1)  # O(10)
    for j in range(len(count_array)):  # O(10)
        count_array[j] = []

    # Counting the frequency of occurrence
    for i in range(len(unsorted_list)):  # O(N)
        count_array[unsorted_list[i] // (base ** col) % base].append(unsorted_list[i])

    # sorting the list
    index = 0
    for j in range(len(count_array)):  # O(10)
        for i in range(len(count_array[j])):  # O(N)
            unsorted_list[index] = count_array[j][i]
            index += 1

    return unsorted_list


def radix_sort_num(unsorted_list):
    """
    Function used to sort list of numbers using the radix sort method
    :param unsorted_list: the list that will be sorted
    :return: the sorted list
    :Time Complexity: O(kN) - k is the maximum number of digits in any element in the list and N is the number of elements
    in the list
    :Auxiliary space complexity: O(N) - N is the number of elements in the list
    """
    # Maximum number of digits
    maximum_digits = find_max_digits(unsorted_list)  # O(k + N)
    for k in range(maximum_digits):  # O(k)
        unsorted_list = sort_counting_num(unsorted_list, k)  # O(N)
    return unsorted_list


def find_max_digits(input_list) -> int:
    """
    :param input_list: list to find the maximum number of digits in the element
    :return: maximum number of digits in any element in the list
    :time complexity: O(k + N) - k is the maximum number of digits in any element in the list and N is the number of elements
    """
    # Finding the maximum number
    maximum = input_list[0]
    for i in range(1, len(input_list)):  # O(N)
        if maximum < input_list[i]:
            maximum = input_list[i]

    # Finding the maximum number of digits
    digit = 0
    while maximum > 0:  # O(k)
        maximum = maximum // 10
        digit += 1
    return digit


def best_interval(transactions, t):
    """
    :param transactions: unsorted list where each integer in the list represents the time that some transaction
    occurred
    :param t: length of time in seconds
    :return: a tuple (best_t, count) - best_t is the time that the interval starts and count is the number of elements
    in the interval of length t
    :time complexity: O(kN) - k is the maximum number of digits in any element in the list and N is the number of elements
    """
    # Sorting the list
    if len(transactions) > 0:
        transactions = radix_sort_num(transactions)  # O(kN)
        maximum = transactions[0] + t

    # Initialising variables
    best_int = (0, 0)
    i = 0
    j = 0
    count = 0

    while j < len(transactions) and i < len(transactions):  # O(N)
        if j == 0:
            if not (transactions[i] > maximum):
                count += 1
                i += 1
                best_t = transactions[i - 1] - t
                if best_t < 0:
                    best_t = 0
                if count > best_int[1]:
                    best_int = (best_t, count)
            else:
                best_t = transactions[i - 1] - t
                if best_t < 0:
                    best_t = 0
                best_int = (best_t, count)
                # prepare the variables for next iteration
                j += 1
                maximum = transactions[j] + t
                count -= 1
        elif transactions[j] == transactions[j - 1]:
            # To avoid redundant step in checking the intervals if the elements are the same
            j += 1
            maximum = transactions[j] + t
            count -= 1
        else:
            if not (transactions[i] > maximum):
                count += 1
                i += 1
                best_t = transactions[i - 1] - t
                if best_t < 0:
                    best_t = 0
                if count > best_int[1]:
                    best_int = (best_t, count)
            else:
                best_t = transactions[i - 1] - t
                if best_t < 0:
                    best_t = 0
                if count > best_int[1]:
                    best_int = (best_t, count)
                # prepare the variables for next iteration
                count -= 1
                j += 1
                maximum = transactions[j] + t
    return best_int


# Assignment 1 = Task 2

def sort_counting_word(word):
    """
    :param word: a string that will be sorted in alphabetical order
    :return: sorted string
    :Time complexity: O(M) - M is the number of characters in the string
    """
    # Find the largest letter
    maximum = find_max_char(word)
    # Computing the count array
    count_array = [0] * (maximum + 1)  # Worst case: O(26)
    # Calculating the frequencies
    for i in range(len(word)):  # O(M)
        count_array[ord(word[i]) - 97] += 1
    # updating the input list
    word = ""
    for i in range(len(count_array)):
        frequency = count_array[i]
        for j in range(frequency):
            word += chr(i + 97)
    return word


def find_max_char(word):
    """
    Finding the largest letter in a string
    :param word: string used to find the largest letter present in it
    :return: largest letter in the string
    :Complexity: O(M) - M is the number of elements in the string
    """
    # function to find the maximum value in letters
    maximum = ord(word[0]) - 97
    for i in range(1, len(word)):
        if maximum < ord(word[i]) - 97:
            maximum = ord(word[i]) - 97
    return maximum


def counting_sort_list_strings(list, col):
    """
    This function is used to perform the counting sort step in radix sort
    :param list: list that will be sorted
    :param col: the column that we are sorting in the list of strings
    :return: the sorted list
    :time complexity: O(L) - L is the number of elements in the list
    :auxiliary space complexity: O(L) - L is the number of elements in the list
    """
    count_array = [None] * 27
    # creating the count array
    for j in range(len(count_array)):
        count_array[j] = []

    # Counting the frequency of occurrence
    for i in range(len(list)):  # O(L)
        if len(list[i][1]) > col:
            count_array[ord(list[i][1][col]) - 96].append(list[i])
        else:
            count_array[0].append(list[i])

    # sorting the list
    index = 0
    for j in range(len(count_array)):
        for i in range(len(count_array[j])):  # O(L)
            list[index] = count_array[j][i]
            index += 1

    return list


def radix_sort_strings(list):
    """
    Sorting the strings in the list in alphabetical order
    :param list: List that contains unsorted strings
    :return: list with the elements sorted
    :Time complexity: O(LM) - L is the number of elements in the list and M is the length of the longest string in the list
    """
    lengths = []
    # Get the length of all the strings in the list
    for i in range(len(list)): # O(N)
        lengths.append(len(list[i][1]))
    # getting the number of letters in the longest string
    if len(lengths) > 0:
        m = find_max(lengths) - 1
        for i in range(m, -1, -1): # O(M)
            list = counting_sort_list_strings(list, i) # O(L)

    return list


def find_max(input_list) -> int:
    """
    Finds the maximum value in the list
    :param input_list: List with numbers
    :return: The maximum value in the list
    :Time complexity: O(L) - L is the number of elements in the list
    """
    maximum = input_list[0]
    for i in range(1, len(input_list)):
        if maximum < input_list[i]:
            maximum = input_list[i]
    return maximum


def words_with_anagrams(list1, list2):
    """
    Takes in two lists that will then be compared to find all the words in the first list which have an anagram in the
    second list
    :param list1: List of strings
    :param list2: List of strings
    :return: The words in the List1 which have an anagram in the List2
    :Time Complexity: O(L1M1 + L2M2) - L1 is the number of elements in list 1 and M1 is the length of the longest string in
    list1 L2 is the number of elements in list 2 and M2 is the length of the longest string in list2
    :Auxiliary space complexity: O(L1 + L2) - L1 is the number of elements in list1, L2 is the number of elements in
    list2
    """

    # Sorting each word in the two lists
    list1_sorted = [None] * len(list1)
    for i in range(len(list1)):  # O(L1)
        list1_sorted[i] = [i, sort_counting_word(list1[i])]

    list2_sorted = [None] * len(list2)
    for i in range(len(list2)):  # O(L2)
        list2_sorted[i] = [i, sort_counting_word(list2[i])]

    # sorting words in order in the two lists
    list1_sorted = radix_sort_strings(list1_sorted)
    list2_sorted = radix_sort_strings(list2_sorted)
    # removing duplicates in list 2:
    a = 0
    b = 0
    while a < len(list2_sorted) - 1 and b < len(list2_sorted):  # O(L2M2)
        if list2_sorted[b][1] == list2_sorted[a + 1][1]:
            a += 1
        else:
            list2_sorted[a + 1], list2_sorted[b + 1] = list2_sorted[b + 1], list2_sorted[a + 1]
            b += 1
            a += 1
    # Updating a based on the presence of repetition
    if a == b:
        a = len(list2)

    # Finding anagrams in list 1
    i = 0
    j = 0
    anagrams = []
    while i < len(list1):  # O(L1)
        if j == a: # Ensures that the loop will run L1 number of times
            i += 1
        else:
            if list1_sorted[i][1] == list2_sorted[j][1]:
                anagrams.append(list1[list1_sorted[i][0]])
                i += 1
            elif list1_sorted[i][1] > list2_sorted[j][1]:
                j += 1
            else:
                i += 1
    return anagrams

list_1 = ['zach', 'jacky', 'casper', 'laura', 'benny', 'desmond', 'john', 'arthur']
list_2 = []
for i in range(len(list_1)):
    list_2.append([i, list_1[i]])

list_3 = radix_sort_strings(list_2)
print(list_3)

