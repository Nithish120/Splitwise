# Splitwise clone

## AIM:
To track shared expenses within groups and compute who owes whom, allowing users to settle balances.


## SCOPE:
1) Create groups
2) Add members to groups
3) Add shared expenses
4) Support equal and unequal split (initially)
6) Compute balances (owe / owed)
7) View per-group balances 


## CORE USE CASES:
1) User creates a group
2) User adds members to group
3) User adds an expense
4) System calculates balances
5) User views balances


## PAGES:
1) (/home)home - shows groups, button to add group,
2) (/newgroup/)new group - name,members,
3) (/group/<id>/)grouppage - show expenses, button to add expense,
4) (/group/<id>/about) groupdetails - show group members, how much they owe/to be receive
5) (/newexpense/)new expense - name, amount, split type, add members 
6) (/expense/<id>/)expensepage - show members paid/not status, show tot amt and rem bal,
