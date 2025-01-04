def listtodict(lst):
  result={}
  for item ion lst:
      result[item[0]]=item[1:]
  return result

players=[[456, 'Seong Gi-hun' ,48],[218, 'Cho Sang-woo' ,47],[199, 'Ali Abdul' ,33],[001, 'Oh Il-nam' ,88],[067, 'Kang Sae-Byeok' ,24]]

print("List is ",players)
print("Converted dictionary is ",listtodict(players))
