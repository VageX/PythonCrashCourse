guest_list = ['Lauren', 'Biscuit', 'Steph']
print(guest_list[0] + ", you are invited to dinner.")
print(guest_list[2] + ", you are invited to dinner.")
print(guest_list[1] + ", you are invited to dinner.")
print("\t")

cant_make_it = 'Steph'
guest_list.remove(cant_make_it)
print(cant_make_it + " can't make it to dinner tonight.")
print("\t")

guest_list.append('Denis')
print(guest_list)
print(guest_list[0] + ", you are invited to dinner.")
print(guest_list[2] + ", you are invited to dinner.")
print(guest_list[1] + ", you are invited to dinner.")
print("\t")

print("We found a bigger dinner table.  Rolling squad deep.")
guest_list.insert(0, 'Evan')
guest_list.insert(2, 'Victoria')
guest_list.append('Bugsy')
print("\t")
print("Here is the updated dinner invitee list.")
print(guest_list)
for guest in guest_list:
    print(guest + ", you are invited to dinner.")
print("\t")

print("Turns out, the new dinner table won't arrive in time for dinner.  I can only have two people over.")
guest_list.pop(0)
guest_list.pop(1)
guest_list.pop(2)
guest_list.pop(2)
print(guest_list)
print(guest_list[0] + ", we're still good for dinner.")
print(guest_list[1] + ", we're still good for dinner.")
del guest_list
print(guest_list)