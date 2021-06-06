import csv

def parsecsv(info):
    with open("students.csv", "a",newline="") as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact No.", "Email ID"])

        writer.writerow(info)

class students:

    name, age, contact_no, email_id = "ABCD"

    def getrecord(self,i):
        print("\nENTER STUDENT#{} INFO".format(i))
        self.name = input("\tEnter Name : ")
        self.age = int(input("\tEnter Age : "))
        self.contact_no = int(input("\tEnter No. : "))
        self.email_id = input("\tEnter email id : ")

    def saverecord(self,i):
        print("\nSTUDENT#{} INFO\n\tName : {}\n\tAge : {}\n\tNo. : {}\n\temail id : {}"
            .format(i,self.name, self.age, self.contact_no, self.email_id))

        choice_check = input("\nDo you wanna save this record ? (yes/no): ")
        if choice_check=="yes":
            parsecsv([self.name, self.age, self.contact_no, self.email_id])
            return True
        elif choice_check=="no":
            print("\nEnter the correct info\n")
            return False

s1 = students( )
i = 1
while True:

    s1.getrecord(i)
    if s1.saverecord(i):
        i = i + 1
        if input("\nDo you wanna add another student ? (yes/no): ")=="no" :
            exit()
    else:
        pass
