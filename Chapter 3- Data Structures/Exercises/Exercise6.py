Invitee = ['cris bumsted' , 'robin williams' , 'sam sulek' , 'gordon ramsay' , 'stephen hawking' , 'elvis presley']
for invitedpeople in Invitee:
    print(invitedpeople + ", Please come over for dinner at my home.")


Invitee = ['cris bumsted' , 'robin williams' , 'sam sulek' , 'gordon ramsay' , 'steve Jobs' , 'elvis presley']
for invitedpeople in Invitee:
    print ("one of the invitee's sadly cancelled but I invited a new person so " + invitedpeople + "I invite you over for dinner")

invitedpeople = Invitee.pop(5)
print (Invitee)
invitedpeople = Invitee.pop(3)
print (Invitee)

for invitedpeople in Invitee:
    print ("You, " + invitedpeople + " are still invited to dinner at my home.")
print (Invitee)
if len(Invitee) >= 2:
    del Invitee[-2:]
print (Invitee)