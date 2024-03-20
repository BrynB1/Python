#CS175L-01
#Bryn Bijur
#stocks

#Inputs
COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

#Calculations
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommission = COMMISSION_RATE * stockSoldFor 
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid
#Outputs
print ("Amount paid for stock: $", amountPaidForStock)
print ("Commission paid on the purchase: $", purchaseCommission)
print ("Amount the stock sold for: $", stockSoldFor)
print ("Commission paid on the sale: $", sellingCommission)
print ("Profit (or loss if negative): $", profitOrLoss)
