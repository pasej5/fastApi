from typing import List
import pdb; pdb.set_trace()

# class Solution:
#     def fizzbuzz(self, n: int) -> int:
#         """
#         Fizz buzz function, if number is divisable by a number should return fizzbuzz
#         Args:
#             n (int): this is the number we are loopin in
#         """
#         n = int()
#         for i in range(0, n+1):
#             Fizz = (i % 3 == 0)
#             Buzz = (i % 5 == 0)
#             FizzBuzz = Fizz and Buzz
            
#             if FizzBuzz:
#                  print("FizzBuzz")
#             elif Fizz:
#                 print("Fizz")
#             elif Buzz:
#                 print("Buzz")
#             else:
#                 print(i)
                
# if __name__ =="__main__":
#     s = Solution()
#     s.fizzbuzz("30")

# class Solution:
#     def is_palindrome(self, s: str) -> bool:
#         """
#         Function to check if the string is a palindrom.
#         Args:
#             s (str): the string we are checking
#         Returns:
#             bool
#         """
#         #     rev i Ver
        
#          # 1) check if the strin is alpha numeric
#          # 2) check if the left and right are the same
#          # 3) check if the string is upper or lower
         
#         low, high = 0, len(s)
         
#         while low < high:
         
#             while low < high and not s[low].isalnum():
#                 low += 1
#             while low < high and not s[high].isalnum():
#                 high -= 1
            
#             if s[low].lower() != s[high].lower():
#                 return False
            
#             low += 1
#             high -= 1
            
#         return True
    
    
# class Solution:
    
#     def bfs(self, grid, i, j):
#         """
#         breadth first search will called on i and j
#         """
#         #eplore all the 4 directions (up,down, left, and right)
#         #check if the neighbors are either 1
#         # mark visited to avoid revisiting
#         pass
    
    
#     def num_islands(self, grid: List[list[str]]) -> int:
#         """
#         number of islands
#         Args:
#             grid (list): grid which is a list of list of string
#         Rteurn:
#             returns the number of islands as an int
#         """
        
#         # we are going to iterate through the columns checking if the index is either 1 or == 0
#         # if its 1 we know its land and if its 0 we know its water
#         # we will also iterate through the columns and also check if its land or water 
#         # if its water we have to mark it visited so that we dont count it again
#         # we also need to make sure that when  we find land we implement a bfs that will check all the nearbours if they are also land
#         rows = len(grid)
#         col = len(grid[0])
        
#         if not grid:
#             return 0
#         for i in range(rows):
#             for j in range(col):
#                 if grid[i][j] == "1":
#                     self.bfs(i, j)
#                     num_islands = num_islands + 1
#         return num_islands


#is the window valid 
# do we have any duplicate in the set
#  is s[R] not in set()
    #if not then add s[R] to the set
    # longest += 1
    # s[r]+=1
    #else set.remove s[l] in set 
    # s[l]=+ 1
    # check if s[R] in set if not then add s[R to the set]
     
     # string 'abcabcbb'
     #          l r
     
     #  b c
    #        
      
# class Solution:
#     def longestSubstring(self, s: str) -> int:
#         """
#         Function that finds the longest substring in a given string.
#         Args:
#             s (str): the string wher we find the logest substring
#         Return:
#             int: return must be an int
#         """
#         l = 0
#         longest = 0
#         n = len(s)
#         sett = set() # constant look up
#         #window = (last ponter - first pointer) + 1 big O(n) because this is a linear solution
        
#         for r in range(n):
#             while s[r] in sett:
#                sett.remove(s[l])
#                l += 1
#             w = (r - l) + 1
            
#             longest = max(longest, w)
#             sett.add(s[r])
        
#         return longest
    
    # s = [r a c e C a r]
    
# class Solution:
#     def twoSum(self, s: int) -> Bool:
#         """
#         Functions that reverses a string.
#         Args:
#             s (str): string to be reversed
#         Returns:
#             Bool
#         """
#         new_string = ""
        
#         for c in s:
#            if c.isalnum():
#                new_string += c.lower()
#         new_string == new_string[::-1]
         
# class Solution:
#     def level_order(self, root: TreeNode) -> List[List[int]]:
#      """
#      Binary tree travesal
#      Args:
#         root (TreeNode): tree we are travesing
#     Returns: List of lists
#      """
     
#      # [3]
#      # [9, 20]
#      # [15, 7]
#      if root is None:
#          return []
#      result = []
#      queue = [root]
#      next_queue =[]
#      level = []
     
#      while queue != None:
#          for root in queue:
#              level.append(root.val)

class Node:
     def __init__(self, data=None, next=None):
         self.data = data
         self.next = next
         
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("This Node is empty")
            return
        
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)
       
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        return self
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1 
            itr = itr.next
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('This is not a valid index')
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            
            itr = itr.next
            
    def search(self, key):
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        if index == 0:
            self.add(data)
            
        if index > 0:
            new_node = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = node.next_node
                current -= 1
            prev_node = current
            next_node = current.next_node
            
            
    def remove(self, key):
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            pass
            
            
        
            
    
if __name__ == "__main__":
    
    ll = Linkedlist()
    ll = ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    
     
     
     
     