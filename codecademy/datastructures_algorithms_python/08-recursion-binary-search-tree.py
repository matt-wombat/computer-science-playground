def build_bst(my_list):
  if my_list == []:
    return "No Child"
  
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]

  print("Middle index:", middle_idx)
  print("Middle value:", middle_value)

  tree_node = { "data": middle_value }
  tree_node["left_child"] = build_bst(my_list[:middle_idx])
  tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])

  return tree_node

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)