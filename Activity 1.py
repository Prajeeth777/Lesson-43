list1=['Miami', 'Dallas', 'San Fransisco', 'Los Angeles', 'New York']
print("List elements are ",list1)

print(list1[2]," is a part of the Silicon Valley.")

list.append('Washington DC')
print("Updated list after adding is ",list1)

list1.sort()
print("Sorted list is ",list1)

list.reverse()
print("Reversed list is ", list1)

list.remove('Dallas')
print("Updated list after removing is , list1")

list1.pop(4)
print("List after popping an element is ",list1)

print("Length of the list is ",len(list1))

list1.clear()
print(list1)
