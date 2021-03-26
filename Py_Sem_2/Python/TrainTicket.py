class TicketInfo:
    def __init__(self,pnr, source, destination, name, dateofjourny, ):
        self.pnr = pnr
        self.source = source
        self.destination = destination
        self.name = name
        self.doj = dateofjourny

    def __str__(self):
        return (
            f"PNR:{self.pnr}  Source:{self.source}  Destination:{self.destination}  Name:{self.name}  Date of Journey:{self.doj}")


pessengers = []
pessengers.append(TicketInfo(7563, "Delhi", "Karnatka", "Vishal", "02-01-21"))
pessengers.append(TicketInfo(7652, "Varanasi", "Lucknow", "Shiv", "03-04-21"))
pessengers.append(TicketInfo(4252, "Mumbai", "Bihar", "Mayank", "21-01-21"))
pessengers.append(TicketInfo(3563, "Patna", "Odisa", "Ronit", "12-01-21"))
pessengers.append(TicketInfo(4534, "Bihar", "Delhi", "Abhishek", "21-01-21"))
pessengers.append(TicketInfo(7644, "Odisa", "Ghazipur", "Shivam", "31-01-21"))
pessengers.append(TicketInfo(2354, "Ghazipur", "Karnatka", "Nitin", "16-42-21"))
pessengers.append(TicketInfo(4635, "Delhi", "Hariharpur", "Kashav", "18-01-21"))
pessengers.append(TicketInfo(9867, "Hariharpur", "Patna", "Sachin", "28-01-21"))
pessengers.append(TicketInfo(3463, "Patna", "Faridabad", "Ambuj", "16-01-21"))
pessengers.append(TicketInfo(1323, "Ahemdabad", "Goa", "Krishna", "10-12-21"))
f = open("TicketInfo.txt", "a")
for i in pessengers:
    f.write(str(i)+"\n")
print("File Successfully saved.....")
f.close()