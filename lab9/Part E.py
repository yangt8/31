#  Yang Tang 53979886 and Yilin Huang 31687105.  ICS 31 Lab sec 7.  Lab asst 9.

from collections import namedtuple
Reservation = namedtuple('Reservation', 'id room_number arrival_date departure_date guest_name')
from datetime import *  
import time 

def DATE(R:str) -> str:
    l=R.split('/')
    D=date(int(l[2]),int(l[0]),int(l[1]))
    return D

def BandBI():
    infile = open("inputfile.txt", "r")
    outfile = open('Result.txt','w')
    result=[]
    result2=[]
    number=0
    for line in infile:
        command=line.strip()[:2].upper()
        room=line.strip()[2:].strip()
        if command=='NB':
            "add a new bedroom"
            if room not in result:
                result.append(room)
            else:
                outfile.write("Sorry, can't add room {} again; it's already on the list.\n".format(room))               
        elif command == 'LB':
            "list bedrooms"
            outfile.write('Number of bedrooms in service: {}\n'.format(len(result)))
            outfile.write('------------------------------------\n')
            for r in result:
                outfile.write(r+'\n')
        elif command == 'PL':
            "print line"
            outfile.write(room+'\n')
        elif command == 'DB':
            "delete bedroom"
            if room in result:
                test=[]
                for x in result2:
                    if x.room_number==room:
                        outfile.write("Deleting room {} forces cancellation of this reservation:\n".format(room))
                        outfile.write("    {} arriving {} and departing {} (Conf. #{})\n".format(x.guest_name,x.arrival_date,x.departure_date,x.id))
                        test.append(x)
                result.remove(room)
                for x in test:
                    result2.remove(x)
            else:
                outfile.write("Sorry, can't delete room {}; it is not in service now\n".format(room))               
        elif command == 'RR':
            "reserve room"
            l=room.split()
            if not l[0] in result:
                    outfile.write("Sorry; can't reserve room {}; room not in service\n".format(l[0]))
            elif DATE(l[1])>DATE(l[2]):
                outfile.write("Sorry, can't reserve room {} ({} to {});\n".format(l[0],l[1],l[2]))
                outfile.write("    can't leave before you arrive.\n")
            elif DATE(l[1])==DATE(l[2]):
                outfile.write("Sorry, can't reserve room {} ({} to {});\n".format(l[0],l[1],l[2]))
                outfile.write("    can't arrive and leave on the same day.\n")
            elif not l[0] in result:
                outfile.write("Sorry; can't reserve room {}; room not in service\n".format(l[0]))
            elif l[0] in result:
                boolen=0
                for i in result2:
                    if i.room_number==l[0]:
                        if (DATE(l[1])>=DATE(i.arrival_date) and DATE(l[1])<DATE(i.departure_date)):
                            boolen = 1
                        elif (DATE(l[2])<=DATE(i.arrival_date) and DATE(l[2])>DATE(i.departure_date)):
                            boolen=1
                            break
                if boolen==0:
                    number+=1
                    N=(l[0], l[1], l[2])
                    M=[]
                    for u in l:
                        if u not in N:
                            M.append(u)
                    R=Reservation(number, l[0], l[1], l[2],' '.join(M))
                    result2.append(R)
                    outfile.write('Reserving room {} for {} -- Confirmation #{} \n'.format(R.room_number,R.guest_name,R.id))
                    outfile.write('    (arriving {}, departing {})\n'.format(R.arrival_date,R.departure_date))
                else:
                    outfile.write("Sorry, can't reserve room {} ({} to {});\n".format(l[0],l[1],l[2]))
                    outfile.write("   it's already booked (Conf. #{})\n".format(i.id))                   
        elif command == 'LR':
            "list reservations"
            outfile.write('Number of reservations: {}\n'.format(len(result2)))
            outfile.write('No. Rm. Arrive      Depart     Guest\n')
            outfile.write('------------------------------------------------\n')
            for r in result2:
                outfile.write('  {} {} {} {} {}\n'.format(r.id, r.room_number, r.arrival_date, r.departure_date, r.guest_name))
        elif command == 'DR':
            "delete reservation"
            if R in result2:
                for i in result2:
                    if int(room) == i.id:
                        result2.remove(i)
            else:
                outfile.write("Sorry, can't cancel reservation; no confirmation number {}\n".format(room))
        elif command == 'RB':
            "reservations by bedroom"
            outfile.write("Reservations for room {}:\n".format(room))
            for i in result2:
                if i.room_number==room:
                    outfile.write("    {} to  {}:  {}\n".format(i.arrival_date,i.departure_date,i.guest_name))
        elif command == 'RG':
            "reservations by guest"
            outfile.write("Reservations for room {}:\n".format(room))
            for i in result2:
                if i.guest_name==room:
                    outfile.write("    {} to  {}:  room {}\n".format(i.arrival_date,i.departure_date,i.room_number))            
        elif command == 'LA':
            "list arrivals"
            outfile.write("Guests arriving on {}:\n".format(room))
            for i in result2:
                if i.arrival_date==room:
                    outfile.write("   {} (room {})\n".format(i.guest_name,i.room_number)) 
        elif command == 'LD':
            "list departures"
            outfile.write("Guests departing on {}:\n".format(room))
            for i in result2:
                if i.departure_date==room:
                    outfile.write("   {} (room {})\n".format(i.guest_name,i.room_number))
        elif command=="LF":
            '''list free bedrooms'''
            l=room.split()
            outfile.write("Bedrooms free between {} to {}:\n".format(l[0],l[1]))
            number_set=set()
            for i in result2:
                if (DATE(l[0])>=DATE(i.arrival_date) and DATE(l[0])<DATE(i.departure_date)):
                    number_set.add(i.room_number)
                elif (DATE(l[1])<=DATE(i.arrival_date) and DATE(l[1])>DATE(i.departure_date)):
                    number_set.add(i.room_number)
            for a in result:
                if a not in number_set:
                    outfile.write("   {}\n".format(a))
        elif command=="LO":
            l=room.split()
            outfile.write("Bedrooms occupied between {} to {}:\n".format(l[0],l[1]))
            number_set=set()
            for i in result2:
                if (DATE(l[0])>=DATE(i.arrival_date) and DATE(l[0])<DATE(i.departure_date)):
                    number_set.add(i.room_number)
                elif (DATE(l[1])<=DATE(i.arrival_date) and DATE(l[1])>DATE(i.departure_date)):
                    number_set.add(i.room_number)
            for a in result:
                if a in number_set:
                    outfile.write("   {}\n".format(a))
    infile.close()
    outfile.close()            
BandBI()
