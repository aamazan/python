# Description: program to relearn file i/o
import csv # std lib first
import qs # local module

#name = input("Please enter a name for your .txt: \n")
#name += ".txt"
#f1 = open(name,"w")


#while str != "0":
#    if str == "0":
#        break
#    else:
#        f1.write(str + "\n")
#        str = input()

#f1.close()
#l = [1,1]
#for j in range(0,10):
#    l.append(l[j]+l[j+1])

#with open("csvtest.txt", "w") as csvfile:
#    wr = csv.writer(csvfile, delimiter = ',')

## Practice idea: input from console formatted and written into .csv


#-------------------------------------------------------------------------------

## Maybe options to search for a player by name,jersey, etc. and print out
    ## information specified by user input.
## Different types of search?
    ## By: name (obvious), jersey (would have to print all players with said jersey)
            ## rating, potential, by each stat (likely w/ user-defined print limit)
    ## Note: further paring down of printed data by allowing the user to
            ## input which fields they'd like using a binary expression?
## This is getting messy, making a UML to map this out


with open('players_20.csv', mode = 'r') as csv_file:
    csvr = csv.DictReader(csv_file, delimiter=',')
    for i in range(0,4):
        print(csvr[i])
