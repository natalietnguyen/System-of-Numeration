#  File: Radix.py

#  Description: To sort strings containing a combination of digits and lower case letters.

#  Student Name: Natalie Nguyen

#  Student UT EID: ntn687

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 22 March, 2023

#  Date Last Modified: 22 March, 2023


import sys


class Queue (object):
  # initializer
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns an int indicating the length of the longest
#         string in a
def get_longest_string(a):
  # creates a variable indicating the length of the longest 
  # string
  max_length = 0

  # iterates through each string in list a
  for string in a:
    # tests if the length of the current string is greater than 
    # the length of the longest string found so far
    if len(string) > max_length:
      # sets length of current string as max_length
      max_length = len(string) 

  # returns length of the longest string in a
  return max_length


# Input: a is a list of strings that have either lower case
#        letters or digits, max_length is an int that represents
#        the length of the longest string in a
# Output: returns list a version of list a where each string shorter
#         than max_length is adjusted to have extra spaces that account
#         for the difference in length
def add_padding(a, max_length):
  # creates a list
  a_new = []

  # iterates through each string in list a
  for i in range(len(a)):
    # tests if the current string is shorter than the longest string
    if len(a[i]) < max_length:
      # finds the difference in lengths
      diff = max_length - len(a[i])
      # creates a new string that includes spaces to the right of the 
      # string that accounts for difference in length
      new_str = a[i] + (' ' * diff)

      # adds new_str to list a_new
      a_new.append(new_str)
    else:
      # adds current string to list a_new
      a_new.append(a[i])

  # returns list of adjusted strings
  return a_new


# Input: a_padded is a list of strings that have either lower case
#        letters, digits, or spaces, max_length is an int that 
#        represents the length of the longest string in a
# Output: returns a version of list a_padded that contains no spaces
#         in each string
def remove_padding(a_padded, max_length):
  # creates a list
  a = []

  # iterates through each string in a_padded
  for i in range(len(a_padded)):
    # sets word as current string
    word = a_padded[i]
    # creates a variable indicating the number of spaces in word
    count = 0

    # iterates through the current string
    for j in range(max_length):
      # tests if the current string at index j is a space
      if word[j] == ' ':
        # increases count by 1
        count += 1

    # creates a new string that cuts out the spaces in word
    original_str = word[:max_length - count]

    # adds new string to list a
    a.append(original_str)

  # returns list of strings with no spaces
  return a


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  # a list containing all the queues for sorting
  #   index 0: Queue placement for digit zero or empty spaces
  #   indexes 1 - 9: Queue placement for digits
  #   indexes 10 - 35: Queue placement for lower case letters,
  #   index 36: Queue placement for ordering of all of strings
  queue_list = []

  for i in range(37):
    queue_list.append(Queue())

  # gets the length of the longest string in list a
  max_length = get_longest_string(a)
  
  # creates a new list with spaces added to strings that are 
  # shorter than the max length
  a_new = add_padding(a, max_length)

  # iterates through each character in the word from left to right
  for i in range((max_length - 1), -1, -1):
    # tests if loop is on the first iteration
    if i != max_length - 1:
      # assigns the newly sorted list to a_new
      a_new = queue_list[36].queue[:]

    # tests if the Queue for ordering of all strings is empty
    if queue_list[36].is_empty() != True:
      # empties the Queue object
      for j in range(queue_list[36].size()):
        queue_list[36].dequeue()
    
    # iterates through the list of strings
    for k in range(len(a_new)):
      # sets string equal to the string at index k
      string = a_new[k]
      # finds the ascii code of string at index i
      ascii_val = ord(string[i])

      # tests if character is a space
      if ascii_val == 32:
        # enqueues string to Queue at index 0
        queue_list[0].enqueue(string)
      # tests if character is a digit
      elif ascii_val <= 57:
        # finds the index of the Queue to enter string in
        index = ascii_val - 48

        # adds string to Queue at index
        queue_list[index].enqueue(string)
      # character is a lower case letter
      else:
        # finds the index of the Queue to enter string in
        index = ascii_val - 87

        # adds string to Queue at index
        queue_list[index].enqueue(string)
 
    # iteretes through the Queues in queue_list
    for queue in queue_list:
      # tests if the Queue is empty
      if queue.is_empty() == True:
        # skips to the next iteration
        continue
      else:
        # iterates through the strings in Queue
        for l in range(queue.size()):
          # removes and sets string to the first string in Queue
          string = queue.dequeue()
          # adds string to Queue at index 36
          queue_list[36].enqueue(string)
    
  # removes empty spaces within strings in the sorted list
  sorted_list = remove_padding(queue_list[36].queue, max_length)

  # returns list of sorted strings
  return sorted_list


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)


if __name__ == "__main__":
  main()

    
