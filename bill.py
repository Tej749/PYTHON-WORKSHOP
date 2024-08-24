bill = ('receipt.txt', 'r')
bill.read = ('''
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

print(bill.read())
bill.close()