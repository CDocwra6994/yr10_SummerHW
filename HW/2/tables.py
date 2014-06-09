#my different variables
replay=0
table=0
table_2=1
#getting the times table the user wants to view
table=int(input("Which times table would you like to display?"))
#getting how much of the table the user wants to view
replay=int(input("To which number in the times table would you like to display?\n\n\nFor example if you entered 15 it would be the times table you entred until you reach the number you entered."))
result=table*table_2
#the loop to generate the times table itself
while table_2 != replay+1:
    #the display code for the times table
    print("{0} x {1} = {2}".format(table,table_2,result))
    table_2 = table_2 + 1
    #result repeated to make sure it changes as the times table does
    result=table*table_2
print("And thats the {0} times table!".format(table))
