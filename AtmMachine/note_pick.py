class Sample:

    def note_pick(amount):
        notes=(1000,500,100,1)
        output={}
        noteOf500=0
        noteOf1=0
        noteOf1000=0
        noteOf100=0

        if(amount>1000):
            noteOf1000 =amount//1000
            amount=amount-noteOf1000*1000
        

        if(amount>500):
            noteOf500 =amount//500
            amount=amount-noteOf500*500
            
        if(amount>100):
            noteOf100 =amount//100
            amount=amount-noteOf100*100
            

        if(amount>1):
            noteOf1 =amount//1
            amount=amount-noteOf1*1
            
        output = {1000: noteOf1000, 500: noteOf500, 100: noteOf100,  1: noteOf1}
        return output

    if __name__=="__main__":
        amount=int(input("enter a amounnt:"))
        print(note_pick(amount))
