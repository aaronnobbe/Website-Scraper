class OnlineOrder:
    def __init__(self, customerInfo, items, shippingAddress):
        self.customerInfo = customerInfo
        self.items = items
        self.shippingAddress = shippingAddress
#write defined functions for SPR
class OrderCostCalculator:
    def calculateTotalCost(self, items, taxes, discounts):
        print("Total order cost is:")

class OrderValidator:
    def validateOrder(self, items, customerAddress):
        print("Validating online order...")

class OrderConfirmationSender:
    def sendConfirmationEmail(self, customerEmail):
        print("A confirmation email has been sent to:", customerEmail)

class InventoryUpdater:
    def updateInventory(self, items):
        print("Updating inventory...")

def main():
    #testing individual functions
    orderDetails = OnlineOrder("The Big Ron", "Jetpacks", "Mi Casa")

    calculator = OrderCostCalculator()
    calculator.calculateTotalCost(orderDetails.items, 22.22, 1111)

    validator = OrderValidator()
    validator.validateOrder(orderDetails.items, orderDetails.shippingAddress)

    sender = OrderConfirmationSender()
    sender.sendConfirmationEmail(orderDetails.customerInfo)

    inventoryUpdater = InventoryUpdater()
    inventoryUpdater.updateInventory(orderDetails.items)

if __name__ == "__main__":
    main()
