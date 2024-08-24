import datetime

now = datetime.datetime.now()
times = now.strftime("%y-%m-%d %H:%M:%S")

land = [
    [101, 'Kathmandu', 'North', 4, 500000, 'Available'],
    [102, 'Pokhara', 'East', 6, 60000, 'Available'],
    [103, 'Lalitpur', 'West', 4, 400000, 'Available'],
    [104, 'Biratnagar', 'South', 3, 30000, 'Available'],
]


def Land():
    system_code = 1234

    user_pin = int(input("Enter Code : "))

    if user_pin == system_code:
        while True:
            print("""

                1 : Home
                2 : Land Rent Sys
                3 : Exit

            """)
            option = int(input("Choose Option : "))

            if option == 1:
                print(f'''
             NEPALGUNJ REAL STATE CORPORATION
               DHAMBOJI-02, NEPALGUNJ, BANKE


                                    Date & Time : {times}
  Contact No : 081-52521736         email : jargha261975@gmail.com
''')
                print("--------------------------------------------------------------------")
                print(": Kitta :    City    : Direction :  Anna :  Rent (Rs) :  Status    :")
                print("--------------------------------------------------------------------")

                for items in land:
                    print(":", items[0], " " * (4 - len(str(items[0]))), ":",
                          items[1], " " * (9 - len(items[1])), ":",
                          items[2], " " * (8 - len(items[2])), ":",
                          items[3], " " * (4 - len(str(items[3]))), ":",
                          items[4], " " * (9 - len(str(items[4]))), ":",
                          items[5], " " * (8 - len(items[5])), ":",

                          )
                print("--------------------------------------------------------------------")
                option = int(input("Enter the Area you want to book (please mention in kitta) : "))

                if option == 101:
                    print("-------------------------------------------------------------")
                    print('''
                 NEPALGUNJ REAL STATE CORPORATION
                   DHAMBOJI-02, NEPALGUNJ, BANKE

      Contact No : 081-52521736     email : jargha261975@gmail.com
    ''')
                    print("-------------------------------------------------------------")
                    print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                    print("-------------------------------------------------------------")
                    print(land[0], end="  ")
                    print()
                    print("-------------------------------------------------------------")
                    name = input("Please Enter Your Name : ")
                    mob = input("Enter Contact No : ")
                    add = input("Enter Home / Permanent Address : ")
                    month = int(input("Enter Number of Month for Booking : "))
                    email = input("Enter email : ")
                    per_month = 500000
                    total = per_month * month
                    print('---------------------------------------------------------------------------------')
                    print(f'''
                                    NEPALGUNJ REAL STATE CORPORATION
                                      DHAMBOJI-02, NEPALGUNJ, BANKE

                                    Applicant Name : {name}
                                    Address        : {add}
                                    Mob No         : {mob}
                                    email ID       : {email}
                                    ...............................
                                     Rental Land Service & Charges
                                    ...............................
                                    City           : Kathmandu, North    
                                    Kitta          : 101                   
                                    Area           : 4 Anna                 
                                    Monthly Rent   : Rs. {per_month}/-      
                                    Booking Tenure : {month} Months
                                    Booking Date   : {times}
                                ------------------------------------------------------
                                    Total Amount   : Rs. {total}/-
                                ------------------------------------------------------
                                Thank You & Visit Again....!! | Helpline : 9868014825
                                        ''')
                    print('---------------------------------------------------------------------------------')

                elif option == 102:
                    print("-------------------------------------------------------------")
                    print('''
                 NEPALGUNJ REAL STATE CORPORATION
                   DHAMBOJI-02, NEPALGUNJ, BANKE

      Contact No : 081-52521736     email : jargha261975@gmail.com
    ''')
                    print("-------------------------------------------------------------")
                    print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                    print("-------------------------------------------------------------")
                    print(land[1], end="  ")
                    print()
                    print("-------------------------------------------------------------")
                    name = input("Please Enter Your Name : ")
                    mob = input("Enter Contact No : ")
                    add = input("Enter Home / Permanent Address : ")
                    month = int(input("Enter Number of Month for Booking : "))
                    email = input("Enter email : ")
                    per_month = 60000
                    total = per_month * month
                    print('---------------------------------------------------------------------------------')
                    print(f'''
                                NEPALGUNJ REAL STATE CORPORATION
                                  DHAMBOJI-02, NEPALGUNJ, BANKE

                                Applicant Name : {name}
                                Address        : {add}
                                Mob No         : {mob}
                                email ID       : {email}
                                ...............................
                                 Rental Land Service & Charges
                                ...............................
                                City           : Kathmandu, East    
                                Kitta          : 102                   
                                Area           : 6 Anna                 
                                Monthly Rent   : Rs. {per_month}/-      
                                Booking Tenure : {month} Months
                                Booking Date   : {times}
                            ------------------------------------------------------
                                Total Amount   : Rs. {total}/-
                            ------------------------------------------------------
                            Thank You & Visit Again....!! | Helpline : 9868014825
                                    ''')
                    print('---------------------------------------------------------------------------------')

                elif option == 103:
                    print("-------------------------------------------------------------")
                    print('''
                 NEPALGUNJ REAL STATE CORPORATION
                   DHAMBOJI-02, NEPALGUNJ, BANKE

      Contact No : 081-52521736     email : jargha261975@gmail.com
    ''')
                    print("-------------------------------------------------------------")
                    print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                    print("-------------------------------------------------------------")
                    print(land[2], end="  ")
                    print()
                    print("-------------------------------------------------------------")
                    name = input("Please Enter Your Name : ")
                    mob = input("Enter Contact No : ")
                    add = input("Enter Home / Permanent Address : ")
                    month = int(input("Enter Number of Month for Booking : "))
                    email = input("Enter email : ")
                    per_month = 400000
                    total = per_month * month
                    print('---------------------------------------------------------------------------------')
                    print(f'''
                                        NEPALGUNJ REAL STATE CORPORATION
                                          DHAMBOJI-02, NEPALGUNJ, BANKE

                                        Applicant Name : {name}
                                        Address        : {add}
                                        Mob No         : {mob}
                                        email ID       : {email}
                                        ...............................
                                         Rental Land Service & Charges
                                        ...............................
                                        City           : Kathmandu, West    
                                        Kitta          : 103                   
                                        Area           : 4 Anna                 
                                        Monthly Rent   : Rs. {per_month}/-      
                                        Booking Tenure : {month} Months
                                        Booking Date   : {times}
                                    ------------------------------------------------------
                                        Total Amount   : Rs. {total}/-
                                    ------------------------------------------------------
                                    Thank You & Visit Again....!! | Helpline : 9868014825
                                            ''')
                    print('---------------------------------------------------------------------------------')

                elif option == 104:
                    print("-------------------------------------------------------------")
                    print('''
                 NEPALGUNJ REAL STATE CORPORATION
                   DHAMBOJI-02, NEPALGUNJ, BANKE

      Contact No : 081-52521736     email : jargha261975@gmail.com
    ''')
                    print("-------------------------------------------------------------")
                    print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                    print("-------------------------------------------------------------")
                    print(land[3], end="  ")
                    print()
                    print("-------------------------------------------------------------")
                    name = input("Please Enter Your Name : ")
                    mob = input("Enter Contact No : ")
                    add = input("Enter Home / Permanent Address : ")
                    month = int(input("Enter Number of Month for Booking : "))
                    email = input("Enter email : ")
                    per_month = 30000
                    total = per_month * month
                    print('---------------------------------------------------------------------------------')
                    print(f'''
                                    NEPALGUNJ REAL STATE CORPORATION
                                      DHAMBOJI-02, NEPALGUNJ, BANKE

                                    Applicant Name : {name}
                                    Address        : {add}
                                    Mob No         : {mob}
                                    email ID       : {email}
                                    ...............................
                                     Rental Land Service & Charges
                                    ...............................
                                    City           : Kathmandu, South    
                                    Kitta          : 104                   
                                    Area           : 3 Anna                 
                                    Monthly Rent   : Rs. {per_month}/-      
                                    Booking Tenure : {month} Months
                                    Booking Date   : {times}
                                ------------------------------------------------------
                                    Total Amount   : Rs. {total}/-
                                ------------------------------------------------------
                                Thank You & Visit Again....!! | Helpline : 9868014825
                                        ''')
                    print('---------------------------------------------------------------------------')

                else:
                    print('Invalid Input...!!')
                    break
    else:
        print("Incorrect PIN")


Land()
