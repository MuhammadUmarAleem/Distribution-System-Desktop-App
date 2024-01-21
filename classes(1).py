from datetime import datetime
class Email:
    def __init__(self,email):
        self.email = email
        self.subject = None
        self.content = None

    
class Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class EmployeeNode(Account):
    def __init__(self,ID,name,phoneNo,salary,email):
        now = datetime.now()
        self.ID = ID
        self.name = name
        self.phoneNo = phoneNo
        self.salary = salary
        self.dateOfJoining = now.strftime("%d/%m/%Y %H:%M:%S")
        self.username = email
        self.password = ''
        self.next = None
        return

class Employee:
    def __init__(self):        
        self.head = None
        self.tail = None
        return

    def addEmployee(self, item):       
        if not isinstance(item, EmployeeNode):
            item = EmployeeNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return

    # def length(self):
    #     count = 0
    #     CurrentNode = self.head
        
    #     while CurrentNode is not None:
    #         count = count + 1
    #         CurrentNode = CurrentNode.next        
    #     return count


    # def output(self):
    #     CurrentNode = self.head 
    #     while CurrentNode is not None:
    #         print(CurrentNode.ID,CurrentNode.name,CurrentNode.phoneNo,CurrentNode.salary,CurrentNode.dateOfJoining)
    #         CurrentNode = CurrentNode.next
            
    #     return

    def deleteEmployee(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.ID == item.ID and CurrentNode.phoneNo == item.phoneNo and CurrentNode.name == item.name and CurrentNode.username == item.username:
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return


class Address:
    def __init__(self,lattitude,longitude):
        self.lattitude = lattitude
        self.longitude = longitude


class MedicalStoreNode(Address):
    def __init__(self, lattitude, longitude,mName,mPhoneNo,mEmail):
        super().__init__(lattitude, longitude)
        self.mName = mName
        self.MphoneNo = mPhoneNo
        self.mEmail = mEmail
        self.bill = 0
        self.next = None


class MedicalStore:
    def __init__(self):        
        self.head = None
        self.tail = None
        return

    def addMedicalStore(self, item):       
        if not isinstance(item, MedicalStoreNode):
            item = MedicalStoreNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return

    def deleteMedicalStore(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.mName == item.mName and CurrentNode.MphoneNo == item.MphoneNo and CurrentNode.mEmail == item.mEmail and CurrentNode.lattitude == item.lattitude and CurrentNode.longitude == item.longitude:
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return



class RiderNode(EmployeeNode):
    def __init__(self, ID, name, phoneNo, salary, email):
        super().__init__(ID, name, phoneNo, salary, email)
        self.bonus = 0

class Rider:
    def __init__(self):        
        self.head = None
        self.tail = None
        return

    def addRider(self, item):       
        if not isinstance(item, RiderNode):
            item = RiderNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return

    def deleteRider(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.ID == item.ID and CurrentNode.phoneNo == item.phoneNo and CurrentNode.name == item.name and CurrentNode.username == item.username:
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return


class RiderApprovalNode(RiderNode):
    def __init__(self, ID, name, phoneNo, salary, email,status):
        super().__init__(ID, name, phoneNo, salary, email)
        self.status = status


class RiderApproval:
    def __init__(self):        
        self.head = None
        self.tail = None
        return

    def addRiderApproval(self, item):       
        if not isinstance(item, RiderApprovalNode):
            item = RiderApprovalNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return

    def deleteRiderApproval(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.ID == item.ID and CurrentNode.phoneNo == item.phoneNo and CurrentNode.name == item.name and CurrentNode.username == item.username:
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return
