def player_losses(matches):
  win_dict = {}
  lose_dict = {}
  
  win_list = []
  lose_list = []

  for match in matches:
    if match[0] in win_dict:
      
      win_dict[match[0]] += 1
    else:
      win_dict[match[0]] = 1

    if match[1] in lose_dict:
      lose_dict[match[1]] += 1
    else:
      lose_dict[match[1]] = 1

  for player in win_dict:
    if player not in lose_dict:
      win_list.append(player)

  for player in lose_dict:
    if lose_dict[player] == 1:
      lose_list.append(player)

  return [sorted(win_list), sorted(lose_list)]

    






input = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(player_losses(input))