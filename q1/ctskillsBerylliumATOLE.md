# Computational Thinking Exercise 
## Smart Vending Machine 
**Name:** Nathalie Pauline P. Atole 
**Section:** Beryllium   
**Last Name:** Atole 
**Date:** 08/21/26   
--- ## Step 1: Identify the Big Problem 
### Main Problem 
The school vending machince is inefficient and prone to errors, leading to incorrect change calculation, poor inventory tracking, user selection mistakes, and slow processing times during peak usage.
--- 
## Step 2: Identify the Sub-Problems 
1. INCORRECT CHANGE: Calculating and dispensing accurate change based on money inserted and the item price.
2. INVENTORY TRACKING: Detecting out-of-stock items and sending notifications alert to staff.
3. SELECTION VERIFICATION: Preventing user error by confirming item selection before dispensing.
4. SYSTEM LAG: Streamlining transaction steps to process mulltiple users efficiently.
--- 
## Step 3: Apply Computational Thinking Skills 
| Sub-Problem | CT Skill | Proposed Solution | 
|---|---|---| 
| INCORRECT CHANGE | Algorithm Design | Create an explicit mathematical rule: Change = Amount inserted - Item price, and dispense coins starting from highest denomination| 
| INVENTORY TRACKING | Pattern recognition and Abstraction | Use sensors to log stock; trigger an automated alert when stock count drops below a threshold (N ≤ 2) | 
| SELECTION VERIFICATION | Abstraction | Display a simple visual confirmation ("Confirm: Soda for ₱20? [Yes/No]") | 
| SYSTEM LAG | Decomposition | Break payment and dispensing into parallel asynchronous processes so the next student can queue their order while dispensing finishes. | 
--- 
## Step 4: Algorithmic Solution 
### Selected Sub-Problem 
I select Sub-Problem 1, INCORRECT CHANGE 
### Pseudocode 
  
  Input: item_price, money_inserted

  IF money_inserted < item_price THEN
    PRINT "Insufficient funds. Please insert more money."
  ELSE
    change_due = money_inserted - item_price

    IF change_due == 0 THEN
      PRINT "Exact amount received. Dispensing item..."
    ELSE 
      PRINT "Dispensing item..."
      PRINT "Dispensing change: ₱" + change_due
    ENDIF

    Dispense_Item()
    Dispense_Change(change_due)
  ENDIF
END 
--- 