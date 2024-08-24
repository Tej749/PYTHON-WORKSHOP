land = [
    [101, 'Kathmandu', 'North', 4, 500000, 'Available'],
    [102, 'Kathmandu', 'East', 6, 60000, 'Available'],
    [103, 'Kathmandu', 'West', 4, 400000, 'Available'],
    [104, 'Kathmandu', 'South', 3, 30000, 'Available'],
    [105, 'Pokhara', 'North', 4, 200000, 'Available'],
    [106, 'Pokhara', 'West', 7, 7500000, 'Available'],
    [107, 'Butwal', 'Center', 6, 4500000, 'Available'],
    [108, 'Butwal', 'East', 3, 250000, 'Available'],
    [109, 'Nepalgunj', 'North', 10, 650000, 'Available'],
    [110, 'Kohalpur', 'South', 4, 3500000, 'Available'],
    [111, 'Kohalpur', 'East', 3, 250000, 'Available'],
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
                print('''
             NEPALGUNJ REAL STATE CORPORATION
               DHAMBOJI-02, NEPALGUNJ, BANKE

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
                name = input("Enter Name : ")
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

            City           : Kathmandu, North    
            Kitta          : 101                    
            Area           : 4 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months           
            Applicant Name : {name}
            Address        : {add}
            mob            : {mob}
            email ID       : {email}
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
                name = input("Enter Name : ")
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

            City           : Kathmandu, East    
            Kitta          : 102                    
            Area           : 6 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months            
            Applicant Name : {name}
            Address        : {add}
            mob            : {mob}
            email ID       : {email}
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
                name = input("Enter Name : ")
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

            City           : Kathmandu, West    
            Kitta          : 103                    
            Area           : 4 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months            
            Applicant Name : {name}
            Address        : {add}
            mob            : {mob}
            email ID       : {email}
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
                name = input("Enter Name : ")
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

            City           : Kathmandu, South    
            Kitta          : 104                    
            Area           : 3 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months            
            Applicant Name : {name}
            Address        : {add}
            mob            : {mob}
            email ID       : {email}
        ------------------------------------------------------
            Total Amount   : Rs. {total}/-
        ------------------------------------------------------------
        Thank You & Visit Again....!! | Helpline : 9868014825
                ''')
                print('---------------------------------------------------------------------------')

            elif option == 105:
                print("-------------------------------------------------------------")
                print('''
             NEPALGUNJ REAL STATE CORPORATION
               DHAMBOJI-02, NEPALGUNJ, BANKE

  Contact No : 081-52521736     email : jargha261975@gmail.com
''')
                print("-------------------------------------------------------------")
                print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                print("-------------------------------------------------------------")
                print(land[4], end="  ")
                print()
                print("-------------------------------------------------------------")
                name = input("Enter Name : ")
                mob = input("Enter Contact No : ")
                add = input("Enter Home / Permanent Address : ")
                month = int(input("Enter Number of Month for Booking : "))
                email = input("Enter email : ")
                per_month = 30000
                total = per_month * month
                print('-----------------------------------------------------------------------')
                print(f'''
            NEPALGUNJ REAL STATE CORPORATION
              DHAMBOJI-02, NEPALGUNJ, BANKE

            City           : Pokhara, North    
            Kitta          : 105                    
            Area           : 4 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months            
            Applicant Name : {name}
            Address        : {add}
            mob            : {mob}
            email ID       : {email}
        ------------------------------------------------------
            Total Amount   : Rs. {total}/-
        ------------------------------------------------------
        Thank You & Visit Again....!! | Helpline : 9868014825
                ''')
                print('----------------------------------------------------------------------')

            elif option == 106:
                print("-------------------------------------------------------------")
                print('''
             NEPALGUNJ REAL STATE CORPORATION
               DHAMBOJI-02, NEPALGUNJ, BANKE

  Contact No : 081-52521736     email : jargha261975@gmail.com
''')
                print("-------------------------------------------------------------")
                print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                print("-------------------------------------------------------------")
                print(land[5], end="  ")
                print()
                print("-------------------------------------------------------------")
                name = input("Enter Name : ")
                mob = input("Enter Contact No : ")
                add = input("Enter Home / Permanent Address : ")
                month = int(input("Enter Number of Month for Booking : "))
                email = input("Enter email : ")
                per_month = 7500000
                total = per_month * month
                print('---------------------------------------------------------------------------------')
                print(f'''
            NEPALGUNJ REAL STATE CORPORATION
              DHAMBOJI-02, NEPALGUNJ, BANKE

            City           : Pokhara, West    
            Kitta          : 106                   
            Area           : 7 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months            
            Applicant Name : {name}
            Address        : {add}
            mob            : {mob}
            email ID       : {email}
        ------------------------------------------------------
            Total Amount   : Rs. {total}/-
        ------------------------------------------------------
        Thank You & Visit Again....!! | Helpline : 9868014825
                ''')
                print('-----------------------------------------------------------------------')

            elif option == 107:
                print("-------------------------------------------------------------")
                print('''
             NEPALGUNJ REAL STATE CORPORATION
               DHAMBOJI-02, NEPALGUNJ, BANKE

  Contact No : 081-52521736     email : jargha261975@gmail.com
''')
                print("-------------------------------------------------------------")
                print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                print("-------------------------------------------------------------")
                print(land[6], end="  ")
                print()
                print("-------------------------------------------------------------")
                name = input("Enter Name : ")
                mob = input("Enter Contact No : ")
                add = input("Enter Home / Permanent Address : ")
                month = int(input("Enter Number of Month for Booking : "))
                email = input("Enter email : ")
                per_month = 4500000
                total = per_month * month
                print('---------------------------------------------------------------------------------')
                print(f'''
            NEPALGUNJ REAL STATE CORPORATION
              DHAMBOJI-02, NEPALGUNJ, BANKE

            City           : Butwal, Center
            Kitta          : 107                    
            Area           : 6 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months            
            Applicant Name : {name}
            Address        : {add}
            mob            : {mob}
            email ID       : {email}
        ------------------------------------------------------
            Total Amount   : Rs. {total}/-
        ------------------------------------------------------
        Thank You & Visit Again....!! | Helpline : 9868014825
                ''')
                print('---------------------------------------------------------------------------------')

            elif option == 108:
                print("-------------------------------------------------------------")
                print('''
             NEPALGUNJ REAL STATE CORPORATION
               DHAMBOJI-02, NEPALGUNJ, BANKE

  Contact No : 081-52521736     email : jargha261975@gmail.com
''')
                print("-------------------------------------------------------------")
                print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                print("-------------------------------------------------------------")
                print(land[7], end="  ")
                print()
                print("-------------------------------------------------------------")
                name = input("Enter Name : ")
                mob = input("Enter Contact No : ")
                add = input("Enter Home / Permanent Address : ")
                month = int(input("Enter Number of Month for Booking : "))
                email = input("Enter email : ")
                per_month = 250000
                total = per_month * month
                print('---------------------------------------------------------------------------------')
                print(f'''
            NEPALGUNJ REAL STATE CORPORATION
              DHAMBOJI-02, NEPALGUNJ, BANKE

            City           : Butwal, East    
            Kitta          : 108                    
            Area           : 3 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months            
            Applicant Name : {name}
            Address        : {add}
            mob            : {mob}
            email ID       : {email}
        ------------------------------------------------------
            Total Amount   : Rs. {total}/-
        ------------------------------------------------------
        Thank You & Visit Again....!! | Helpline : 9868014825
                ''')
                print('---------------------------------------------------------------------------------')

            elif option == 109:
                print("-------------------------------------------------------------")
                print('''
             NEPALGUNJ REAL STATE CORPORATION
               DHAMBOJI-02, NEPALGUNJ, BANKE

  Contact No : 081-52521736     email : jargha261975@gmail.com
''')
                print("-------------------------------------------------------------")
                print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                print("-------------------------------------------------------------")
                print(land[8], end="  ")
                print()
                print("-------------------------------------------------------------")
                name = input("Enter Name : ")
                mob = input("Enter Contact No : ")
                add = input("Enter Home / Permanent Address : ")
                month = int(input("Enter Number of Month for Booking : "))
                email = input("Enter email : ")
                per_month = 650000
                total = per_month * month
                print('---------------------------------------------------------------------------------')
                print(f'''
            NEPALGUNJ REAL STATE CORPORATION
              DHAMBOJI-02, NEPALGUNJ, BANKE

            City           : Nepalgunj, North    
            Kitta          : 109                    
            Area           : 10 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months             
            Applicant Name : {name}
            Address        : {add}
            mob            : {mob}
            email ID       : {email}
        ------------------------------------------------------
            Total Amount   : Rs. {total}/-
        ------------------------------------------------------
        Thank You & Visit Again....!! | Helpline : 9868014825
                ''')
                print('---------------------------------------------------------------------------------')




            elif option == 110:
                print("-------------------------------------------------------------")
                print('''
             NEPALGUNJ REAL STATE CORPORATION
               DHAMBOJI-02, NEPALGUNJ, BANKE

  Contact No : 081-52521736     email : jargha261975@gmail.com
''')
                print("-------------------------------------------------------------")
                print(": Kitta : City : Direction : Anna : Rent (Rs) : Status   :")
                print("-------------------------------------------------------------")
                print(land[9], end="  ")
                print()
                print("-------------------------------------------------------------")
                name = input("Enter Name : ")
                mob = input("Enter Contact No : ")
                add = input("Enter Home / Permanent Address : ")
                month = int(input("Enter Number of Month for Booking : "))
                email = input("Enter email : ")
                per_month = 3500000
                total = per_month * month
                print('---------------------------------------------------------------------------------')
                print(f'''
            NEPALGUNJ REAL STATE CORPORATION
              DHAMBOJI-02, NEPALGUNJ, BANKE

            City           : Kohalpur, East    
            Kitta          : 110                   
            Area           : 4 Anna                 
            Monthly Rent   : Rs. {per_month}/-      
            Booking Tenure : {month} Months            
            Applicant Name : {name}
            Address        : {add}
            Mob No         : {mob}
            email ID       : {email}
        ------------------------------------------------------
            Total Amount   : Rs. {total}/-
        ------------------------------------------------------
        Thank You & Visit Again....!! | Helpline : 9868014825
                ''')
                print('---------------------------------------------------------------------------------')



            else:
                print('Invalid Input...!!')


Land()
