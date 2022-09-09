from datetime import datetime

class Vehicle:
    def __init__(self,hgs_num,owner,balance) -> None:
        self.hgs_num = hgs_num
        self.owner = owner
        self.balance = balance
        self.logs = []

class Automobile(Vehicle):
    def __init__(self, hgs_num, owner, balance) -> None:
        super().__init__(hgs_num, owner, balance)
        self.type = "automobile"

class Minibus(Vehicle):
    def __init__(self, hgs_num, owner, balance) -> None:
        super().__init__(hgs_num, owner, balance)
        self.type = "minibus"

class Bus(Vehicle):
    def __init__(self, hgs_num, owner, balance) -> None:
        super().__init__(hgs_num, owner, balance)
        self.type = "bus"

class Gate:
    def __init__(self,auto_price,minibus_price,bus_price) -> None:
        self.records = {}
        self.prices = {
        "automobile": auto_price,
        "minibus":  minibus_price,
        "bus": bus_price
        }
    
    def payment(self,vehicle:Vehicle):
        if vehicle.balance - self.prices[vehicle.type] >= 0:
            return [vehicle.balance - self.prices[vehicle.type]]
        else:
            print(f"insufficent funds for the {vehicle.type} of {vehicle.owner}\ncost:{self.prices[vehicle.type]} balance:{vehicle.balance}")
            return [vehicle.balance,'payment_failed']

    def accept_vehicle(self,vehicle:Vehicle):
        result = self.payment(vehicle)
        vehicle.balance = result[0]
        if 'payment_failed' not in result:
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            date = datetime.now().strftime("%d/%m/%Y")

            vehicle.logs.append(now)

            if date not in self.records.keys():
                self.records[date] = [vehicle]
            else:
                self.records[date].append(vehicle)
        
class Management:
    def view_daily_spending(self, date, gate):
        total = 0
        if gate.records:
            for entry in gate.records[date]:
                total += gate.prices[entry.type]
        print(total)
