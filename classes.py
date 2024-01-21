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
        self.dateOfJoining = now.strftime("%d/%m/%Y")
        self.username = email
        self.password = ''
        self.next = None

class Employee:
    def __init__(self):        
        self.head = None
        self.tail = None

    def addEmployee(self, item):  
        if not isinstance(item, EmployeeNode):
            item = EmployeeNode(item)

        if self.head is None:
            # print("if")
            self.tail = self.head = item
        else:
            # print("else")
            # print(str(self.tail.next))
            self.tail.next = item
            # print(str(self.tail.next.name))
            # print(str(item.name))
            self.tail = self.tail.next
            # print ("done")     
            # print(self.tail.name)
            # item.next = self.head
            # self.head = item
         
        return True

    def length(self):
        count = 0
        CurrentNode = self.head
        
        while CurrentNode is not None:
            count = count + 1
            CurrentNode = CurrentNode.next        
        return count


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
            if CurrentNode.phoneNo == item.phoneNo and CurrentNode.name == item.name and CurrentNode.username == item.username:
                if CurrentNode.next == None:
                    self.tail = previous_node
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return True
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return True

    def updateEmployee(self,updated,item):
        CurrentNode = self.head
        while CurrentNode is not None:
            if CurrentNode.phoneNo == item.phoneNo and CurrentNode.name == item.name and CurrentNode.username == item.username:
                CurrentNode.name = updated.name
                CurrentNode.username = updated.username
                CurrentNode.phoneNo = updated.phoneNo
                CurrentNode.salary = updated.salary

            CurrentNode = CurrentNode.next 
        return True


class RiderNode(EmployeeNode):
    def __init__(self, ID, name, phoneNo, salary, email):
        super().__init__(ID, name, phoneNo, salary, email)
        self.bonus = 0

class Rider:
    def __init__(self):        
        self.head = None
        self.tail = None

    def addRider(self, item):       
        if not isinstance(item, RiderNode):
            item = RiderNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return True

    def deleteRider(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.phoneNo == item.phoneNo and CurrentNode.name == item.name and CurrentNode.username == item.username:
                if CurrentNode.next == None:
                    self.tail = previous_node
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return True
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return True

    def updateRider(self,updated,item):
        CurrentNode = self.head
        while CurrentNode is not None:
            if CurrentNode.phoneNo == item.phoneNo and CurrentNode.name == item.name and CurrentNode.username == item.username:
                CurrentNode.name = updated.name
                CurrentNode.username = updated.username
                CurrentNode.phoneNo = updated.phoneNo
                CurrentNode.salary = updated.salary

            CurrentNode = CurrentNode.next 
        return True



class RiderApprovalNode(RiderNode):
    def __init__(self, ID, name, phoneNo, salary, email,status):
        super().__init__(ID, name, phoneNo, salary, email)
        self.status = status


class RiderApproval:
    def __init__(self):        
        self.head = None
        self.tail = None

    def addRiderApproval(self, item):       
        if not isinstance(item, RiderApprovalNode):
            item = RiderApprovalNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return True

    def deleteRiderApproval(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.ID == item.ID and CurrentNode.phoneNo == item.phoneNo and CurrentNode.name == item.name and CurrentNode.username == item.username:
                if CurrentNode.next == None:
                    self.tail = previous_node
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return True


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


    def addMedicalStore(self, item):       
        if not isinstance(item, MedicalStoreNode):
            item = MedicalStoreNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return True

    def deleteMedicalStore(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.mName == item.mName and CurrentNode.MphoneNo == item.MphoneNo and CurrentNode.mEmail == item.mEmail and CurrentNode.lattitude == item.lattitude and CurrentNode.longitude == item.longitude:
                if CurrentNode.next == None:
                    self.tail = previous_node
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return True
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return True


class ProductNode:
    def __init__(self,medicine,supplier,price,quantity,description):
        self.medicine = medicine
        self.supplier = supplier
        self.price = price
        self.quantity = quantity
        self.description = description
        self.next = None


class Product:
    def __init__(self):        
        self.head = None
        self.tail = None


    def addProduct(self, item):       
        if not isinstance(item, ProductNode):
            item = ProductNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return True

    def deleteProduct(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.medicine == item.medicine and CurrentNode.supplier == item.supplier and CurrentNode.price == item.price and CurrentNode.quantity == item.quantity and CurrentNode.description == item.description:
                if CurrentNode.next == None:
                    self.tail = previous_node
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return True
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return True

class OrderNode(ProductNode):
    def __init__(self, medicine, supplier, price, quantity, description,medicalStore):
        super().__init__(medicine, supplier, price, quantity, description)
        self.medicalStore = medicalStore
        self.status = "Not Delivered"
        now = datetime.now()
        self.orderDate = now.strftime("%d/%m/%Y %H:%M:%S")
        self.isAssigned = False
        self.next = None

class Order:
    def __init__(self):        
        self.head = None
        self.tail = None


    def addOrder(self, item):       
        if not isinstance(item, OrderNode):
            item = OrderNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return True

    def deleteOrder(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.medicalStore == item.medicalStore and CurrentNode.orderDate == item.orderDate and CurrentNode.price == item.price and CurrentNode.medicine == item.medicine and CurrentNode.supplier == item.supplier:
                if CurrentNode.next == None:
                    self.tail = previous_node
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return True
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return True

class RouteNode:
    def __init__(self,Distance,route):
        now = datetime.now()
        self.Distance = Distance
        self.Fuel = 0
        self.Vehicle = None
        self.Price = 0
        self.rider = None
        self.trackname = None
        self.route = route
        self.datetime = now.strftime("%d/%m/%Y %H:%M:%S")
        self.next = None

class Route:
    def __init__(self):        
        self.head = None
        self.tail = None


    def addRoute(self, item):       
        if not isinstance(item, RouteNode):
            item = RouteNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item          
        return True

    def deleteRoute(self, item):
        CurrentNode = self.head
        previous_node = None   
        while CurrentNode is not None:
            if CurrentNode.route == item.route and CurrentNode.datetime == item.datetime and CurrentNode.Distance == item.Distance:
                if CurrentNode.next == None:
                    self.tail = previous_node
                if previous_node is not None:
                    previous_node.next = CurrentNode.next
                else:
                    self.head = CurrentNode.next
                    return
            
            previous_node = CurrentNode
            CurrentNode = CurrentNode.next       
        return True






































# # create four single nodes
# node1 = RiderNode("emp123","Umar","1313123",241214,"@gmail.com")
# node2 = RiderNode("emp456","Umar","1313123",241214,"@gmail.com")
# # item3 = "Berlin"
# node4 = RiderNode("emp789","Umar","1313123",241214,"@gmail.com")

# track = Rider()
# # print("track length: %i" % track.length())

# for current_item in [node1, node2,node4]:
#     track.addRider(current_item)
#     # print("track length: %i" % track.length())
#     print()
#     track.output()

# track.deleteRider(RiderNode("emp456","Umar","1313123",241214,"@gmail.com"))
# print()
# track.output()
