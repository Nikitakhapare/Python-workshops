class Sample:

    def bill_calculator(unit):
        """
        Description:
            Function to calculate electric bill
        Parameter:
            no of unit as a parameter
        Return:
            returning Electic bill 
        """ 
        if unit > 0  and unit <= 50:  
            electricBill=unit*0
            return electricBill

        if unit > 51 and unit <= 150:    
            electricBill=((unit-50)*1)  
            return electricBill


        if unit > 151 and unit <= 250:
            electricBill=(50*0)+((150-50)*1+(unit-150)*3)   
        
            return electricBill 

        if unit > 251:
            electricBill=(50*0)+(150-50)*1+(250-150)*3+((unit-250)*5)
            
            return electricBill


    if __name__=="__main__":
        unit=int(input("Enter Unit: "))   
        print(bill_calculator(unit))