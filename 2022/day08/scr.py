import sys, getopt

file = ((getopt.getopt(sys.argv[1:],"i:")[0])[0])[1]

num_rows = sum(1 for line in open(file))
with open(file) as f:
     tree_arr = []
     for line in f:
         if ( tree_arr == [] ):
            num_cols = len(list(line.strip()))
         tree_arr = tree_arr + list(map(int, list(line.strip())))

visible = 0
sceinic_score = []
for tree_num in range(0, len(tree_arr)):
  current_tree_ht = tree_arr[tree_num]
  current_tree_row = int(tree_num / num_cols)
  current_tree_col = int(tree_num % num_cols)
  blocked_lft      = [index for index in range(current_tree_row * num_cols,tree_num) if tree_arr[index] >= current_tree_ht]
  current_tree_lft = tree_num - max(blocked_lft, default=(current_tree_row * num_cols))
  blocked_rt       = [index for index in range(tree_num+1,((current_tree_row + 1) * num_cols)) if tree_arr[index] >= current_tree_ht]
  current_tree_rt  = min(blocked_rt, default=(((current_tree_row + 1) * num_cols ) - 1)) - tree_num
  blocked_up       = [index for index in range(current_tree_col, tree_num-num_cols+1, num_cols) if tree_arr[index] >= current_tree_ht]
  current_tree_up  = int((tree_num - max(blocked_up, default=current_tree_col))  / num_cols)
  blocked_btm      = [index for index in range(tree_num+num_cols,1+(current_tree_col + (num_rows - 1) * num_cols),num_cols) if tree_arr[index] >= current_tree_ht]
  current_tree_btm = int((min(blocked_btm, default=(current_tree_col + (num_rows - 1) * num_cols ) ) - tree_num) / num_cols)
  sceinic_score += [current_tree_lft * current_tree_rt * current_tree_up * current_tree_btm]
  #print(f'{tree_num} :: {current_tree_ht} :: {blocked_lft},{blocked_rt},{blocked_up},{blocked_btm}')
  visible += 1 if ((blocked_lft == []) or (blocked_rt == []) or (blocked_btm == []) or (blocked_up == [])) else 0
     
#print(arr)
print(f'Part 1: {visible}')
print(f'Part 2: {max(sceinic_score)}')
