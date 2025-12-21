Splitwise clone

AIM:
To track shared expenses within groups and compute who owes whom, allowing users to settle balances.


SCOPE:
Create groups
Add members to groups
Add shared expenses
Support equal split (initially)
Compute balances (owe / owed)
View per-group balances 


CORE USE CASES:
User creates a group
User adds members to group
User adds an expense
System calculates balances
User views balances


PAGES:
(/home)home - shows groups, button to add group, 
(/newgroup/)new group - name,members,
(/group/<id>/)grouppage - show expenses, button to add expense,
(/group/<id>/about) groupdetails - show group members, how much they owe/to be receive
(/newexpense/)new expense - name, amount, split type, add members 
(/expense/<id>/)expensepage - show members paid/not status, show tot amt and rem bal,
