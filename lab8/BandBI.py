def BandBI():
    infile = open("inputfile.txt", "r")
    outfile = open('Result.txt','w')
    result=[]
    for line in infile:
        command=line.strip()[:2].upper()
        room=line.strip()[2:].strip()
        if command=='NB':
            result.append(room)
        elif command == 'LB':
            outfile.write('Number of bedrooms in service: {:2d}\n'.format(len(result)))
            outfile.write('------------------------------------\n')
            for r in result:
                outfile.write(r+'\n')
        elif command == 'PL':
            outfile.write(room+'\n')
    infile.close()
    outfile.close()            
BandBI()                 
