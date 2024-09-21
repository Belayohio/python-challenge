import os
import csv

filename=os.path.join("..","Resources","budget_data.csv")
with open(filename,encoding='utf-8') as csv_file:
    csv_reader=csv.reader(csv_file)
    header=next(csv_reader)
    number_of_month=0
    months_list=[]
    net_proft= 0
    
    max_value=0
    ProfitLoss_lists=[]
    # break down the csv_reader into months_list and profit/loss
    for row in csv_reader:
      months_list.append(row[0])
      ProfitLoss_lists.append(row[1])
    for m in months_list:
        number_of_month+=1
        if m==len(months_list):
         break
   
    print(f"Total number of month:{number_of_month}")
# to find the net profit.
    for i in ProfitLoss_lists:
         net_proft+=int(i)
         if net_proft==len(ProfitLoss_lists):  
          break
        
       
    print(f"Total Net profit/loss:${net_proft}")
    
    # we need to conver the profitloss_list to integer in order to get the max value of the list.
    new_list=list(map(int,ProfitLoss_lists))
    #looping if the condition is met to get the maximum number.
    for numb in range(len(new_list)):
          # to get the maximum increased value:using built in function
         max_value=max(new_list)
         
         if new_list[numb]==max_value:
        
            index_date=months_list[numb]
    print(f"the greatest increase in profit:{index_date} $({max_value})")
        # to find the minimum value and the index of the date.
    for numb in range(len(new_list)):
          min_value= min(new_list )#  we can use python built in function then we can find the respctive date.
          if new_list[numb]==min_value:
           
            min_index_date=months_list[numb]
    print(f"the Greatest Decrease in profit:{min_index_date} $({min_value})")
       # to find Average change,the average change is the difference between ending and opening period.
       #opening period
    opening_period=new_list[0]
    closing_period=new_list[-1]
    averageChange=closing_period-opening_period
    print(f"Average Change: ${averageChange}")
    # we can zip all the out put at once:
    out_put=(f"Total number of month:{number_of_month}\n"f"Total Net profit/loss:${net_proft}\n"f"Average Change: ${averageChange}\n"f"the greatest increase in profit:{index_date} $({max_value})\n"
             f"the Greatest Decrease in profit:{min_index_date} $({min_value})")
    print(out_put)
    #write to text file in w mode it will create new text file .
    file_to_output = os.path.join("..","analysis", "budget_analysis.txt")  # Output file path
with open(file_to_output,'w',newline='') as text_file:
   text_file.write('\nFinancial Analysis\n-------------------\n')
   text_file.write(out_put)