try:
    numb = int(input("Enter Number : "))
    div = numb / 2
    print(numb)
except ZeroDivisionError as e:
    print("Occur Zero division error...!!", e)

except ValueError as e:
    print("Error Occured..!!", e)

finally:
    print("Always executed after exception....!!!")