#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
print('Welcome User!')

while True:
    try:
        option=int(input('\nMain Menu:\n1 - Tools Inventory\n2 - Personnel Directory\n3 - BorrowReturn Logbook\n4 - Exit\nSelect: '))
        if option not in (1,2,3,4):
            print("Invalid Selection")
            continue
        elif option == 1:
            print("\nWELCOME TO TOOLS INVENTORY")
            df=pd.read_csv('List_Of_Tools.csv')
            df.index = df.index+1
            print("\nInventory:")
            print(df)
            print("\nMENU:\n1 - Add Tools\n2 - Delete Tools\n3 - Modify Tools\n4 - Return")

            while True:
                try:
                    option = int(input("SELECT: "))
                    if option not in (1, 2, 3, 4):
                        print("Invalid Selection")
                        continue
                    elif option == 1:
                        f=open('List_Of_Tools.csv', 'a+',newline='')
                        writer=csv.writer(f)
                        NewItem=[]
                        name =(input(f"\nName of Tool: "))
                        while True:
                            try:
                                count = int(input("Number of Tools: "))
                                break
                            except ValueError:
                                print("Invalid input")
                                continue
                        NewItem.append([name,count])
                        writer.writerows(NewItem)
                        print(f"\n",name,"is successfully added to the inventory!")
                        f.close()
                        print("\nWELCOME TO TOOLS INVENTORY")
                        print("\nInventory:")
                        df=pd.read_csv('List_Of_Tools.csv')
                        df.index = df.index+1
                        print(df)
                        print(f"\nMENU:\n1 - Add Tools\n2 - Delete Tools\n3 - Modify Tools\n4 - Return")

                    elif option == 2:
                        f=open("List_Of_Tools.csv","r")
                        reader=csv.reader(f)
                        found=0
                        List=[]
                        tool=input("What tool do you want to delete? ")
                        for r in reader:
                            if (r[0]!=tool):
                                List.append(r)
                            else:
                                found=1 
                        f.close()
                        if found==0:
                            print("Tool not found.")
                        else:
                            f=open("List_Of_Tools.csv","w",newline='')
                            writer=csv.writer(f)
                            writer.writerows(List)
                            print(f"\n",name,"is successfully deleted!")
                            f.close()
                            print("\nWELCOME TO TOOLS INVENTORY")
                            print("\nInventory:")
                            df=pd.read_csv('List_Of_Tools.csv')
                            df.index = df.index+1
                            print(df)
                            print(f"\nMENU:\n1 - Add Tools\n2 - Delete Tools\n3 - Update Tools\n4 - Return")

                    elif option == 3:
                        f=open("List_Of_Tools.csv","r")
                        reader=csv.reader(f)
                        found=0
                        List=[]
                        tool=input("What tool do you want to update? ")
                        for r in reader:
                            if (r[0]==tool):
                                r[1]=input("What is the new count for this tool? ")
                                found=1
                            List.append(r)
                        f.close()
                        if found==0:
                            print("Tool not found.")
                        else:
                            f=open("List_Of_Tools.csv","w",newline='')
                            writer=csv.writer(f)
                            writer.writerows(List)
                            print(f"\n",tool,"is successfully updated!")
                            f.close()
                            print("\nWELCOME TO TOOLS INVENTORY")
                            print("\nInventory:")
                            df=pd.read_csv('List_Of_Tools.csv')
                            df.index = df.index+1
                            print(df)
                            print(f"\nMENU:\n1 - Add Tools\n2 - Delete Tools\n3 - Modify Tools\n4 - Return")

                    else:
                        break 
                except ValueError:
                    print('Invalid Input')
                    
        elif option == 2:
            print("\nWELCOME TO PERSONNEL DIRECTORY")
            print("\nPersonnel:")
            df=pd.read_csv('List_Of_Personnel.csv')
            df.index = df.index+1
            print(df)
            print(f"\nMENU:\n1 - Search\n2 - Return")

            while True:
                try:
                    option = int(input("SELECT: "))
                    if option not in (1, 2):
                        print("Invalid Selection")
                        continue
                    elif option == 1:
                        while True:
                            option = int(input(f"\nSearch by:\n1 - Name\n2 - Role\n3 - Cancel\nSELECT: "))
                            if option not in (1, 2, 3):
                                print("Invalid Selection")
                                continue
                            elif option == 1:
                                f=open("List_Of_Personnel.csv","r")
                                reader=csv.reader(f)
                                found=0
                                name=input("\nEnter complete name of personnel: ")
                                for r in reader:
                                    if (r[0]==str(name)):
                                        found=1
                                        print('\nName: ',r[0],'\nRole: ',r[1],'\nContact Number: ',r[2],'\nEmail Address: ',r[3])
                                if found==0:
                                    print("Name is not found.")
                                else:
                                    break
                            elif option == 2:
                                f=open("List_Of_Personnel.csv","r")
                                reader=csv.reader(f)
                                found=0
                                role=input("Enter role of personnel: ")
                                for r in reader:
                                    if (r[1]==role):
                                        found=1
                                        print('\nName: ',r[0],'\nRole: ',r[1],'\nContact Number: ',r[2],'\nEmail Address: ',r[3])
                                f.close()
                                if found==0:
                                    print("Role is not found.")
                                else:
                                    break
                            else:
                                break
                    else:
                        break
                except ValueError:
                    print('Invalid Input')
        elif option == 3:
            while True:
                try:
                    df=pd.read_csv('Borrow_Return_LogBook.csv')
                    df.index = df.index+1
                    df['Date_Borrowed'] = pd.to_datetime(df['Date_Borrowed'])
                    df['Date_Returned'] = pd.to_datetime(df['Date_Returned'])
                    print("WELCOME TO BORROW LOGBOOK!\n")
                    print('\nLogbook:\n')
                    print(df)
                    print("\nMENU:\n1 - Borrow Tool\n2 - Return Tool\n3 - Exit")
                    option = int(input("SELECT: "))
                    if option not in (1, 2, 3):
                        print("Invalid Selection\n")
                        continue
                    elif option == 1:
                        df=pd.read_csv('List_Of_Tools.csv')
                        df.index = df.index+1
                        print("\nSelect Tool to Borrow from the Inventory:")
                        print(df)
                        tool_borrow = input(f'\nEnter Tool to Borrow: ')
                        search = (df['Tool'] == tool_borrow)
                        if df[search].empty == True:
                            print("Tool not found.")
                        else:
                            pass
                        while True:
                            try:
                                quant_borrow = int(input('Enter Number of Tool to Borrow: '))
                                break
                            except ValueError:
                                print("Invalid input")
                                continue
                        date_borrow = input('Enter Date today (mm/dd/yyyy): ')
                        name_borrow = input('Enter Name of Borrower: ')
                        borrow_item = {
                            'Personnel': [name_borrow],
                            'Date_Borrowed': [date_borrow],
                            'Tool': [tool_borrow],
                            'Quantity': [quant_borrow]
                        }
                        print('\n',tool_borrow,'has been sucessfully borrowed.\n')
                        df=pd.read_csv('Borrow_Return_LogBook.csv')
                        new_df = pd.DataFrame(borrow_item)
                        df.append(new_df, ignore_index=True, sort = False)
                        df = df.append(new_df, ignore_index=True, sort = False)
                        df.to_csv('Borrow_Return_LogBook.csv', index=False)

                    elif option == 2:
                        df=pd.read_csv('Borrow_Return_LogBook.csv')
                        tool_return = input(f'\nEnter Tool to Return: ')
                        search = (df['Tool'] == tool_return)
                        if df[search].empty == True:
                            print("Tool not found.")
                        else:
                            name_return = input('Enter Name of Borrower: ')
                            search = (df['Personnel'] == name_return)
                            if df[search].empty == True:
                                print("Personnel not found.")
                            else:
                                date_return = input('Enter Date today (mm/dd/yyyy): ')
                                df.loc[search, 'Date_Returned'] = date_return
                                print(tool_return,'has been successfully returned.')
                                df.to_csv('Borrow_Return_LogBook.csv', index=False)

                    else:
                        break
                except ValueError:
                    print("Invalid Input")

        else:
            try:
                option=int(input('\nAre you sure you want to exit?\n1 - Yes\n2 - No\nSelect: '))
                if option not in (1,2):
                    print ("Invalid Selection")
                    continue
                elif option == 1:
                    print("Thank You!")
                    break
                else:
                    pass
            except ValueError:
                print("Invalid Input")
    except ValueError:
        print("Invalid Input")


# In[ ]:




