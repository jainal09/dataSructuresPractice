correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(sudoku_list):
  max_len_sudoku = len(sudoku_list)
  # Column Check
  for column_list in zip(*sudoku_list):
    if len(column_list) != len(set(column_list)):
      return False
  # Row Check
  for row_list in sudoku_list:
    if len(row_list) != len(set(row_list)):
      return False
    for element in row_list:
      if type(element) == int:
        if element > 0:
          continue
        else:
          return False
      else:
        return False
    row_list.sort(reverse=True)
    if row_list[0] > max_len_sudoku:
      return False
    
  return True
 
print(check_sudoku(incorrect))
print(check_sudoku(correct))
print(check_sudoku(incorrect2))
print(check_sudoku(incorrect3))
print(check_sudoku(incorrect4))
print(check_sudoku(incorrect5))