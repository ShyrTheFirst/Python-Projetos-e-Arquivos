"creating hex number for block"

def create_acc(acc_number,last_acc,holder):
    number = acc_number
    last = last_acc
    name_nospace = holder.replace(" ", "")
    name = int(name_nospace, 36)
    acc_id = number+last+name
    print(hex(acc_id))


acc_number = int(input("Your account number: "))
last_acc = acc_number - 1
holder = input("Your name: ")
create_acc(acc_number,last_acc,holder)

#create_acc(102,101,"Eduardo Pin1ho"): 0x3b1e61de56d8d7e17
#create_acc(102,101,"Eduardo Pinho"): 0x1a466462d143f137
    
    
