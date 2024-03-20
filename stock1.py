#CS175L-01
#Bryn Bijur
#stocks

#Inputs
COMMISSION_RATE = float(input("What is the commission rate?: "))
NUM_SHARES = int(input("What is the number of shares?: "))
PURCHASE_PRICE = float(input("What is the purchase price?: "))
SELLING_PRICE = float(input("What is the selling price?: "))
#Calculations
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommission = COMMISSION_RATE * stockSoldFor 
totalCommission = purchaseCommission + sellingCommission
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid
#Outputs
print ("Amount paid for stock: $", amountPaidForStock)
print ("Commission paid on the purchase: $", purchaseCommission)
print ("Amount the stock sold for: $", stockSoldFor)
print ("Commission paid on the sale: $", sellingCommission)
print ("Total commission paid: $",totalCommission)
print ("Profit (or loss if negative): $", profitOrLoss)
