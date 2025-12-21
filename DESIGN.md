# Splitwise clone

## AIM:
To track shared expenses within groups and compute who owes whom, allowing users to settle balances.

## IN SCOPE:
1) Create groups
2) Add members to groups
3) Add shared expenses
4) Support equal and exact amount split
5) Compute balances (owe / owed)
6) View per-group balances 

## OUT OF SCOPE:
1) Recording settlements/payments
2) Authentication & authorization
3) Notifications
4) Editing or deleting expenses

## CORE USE CASES:
1) User creates a group
2) User adds members to group
3) User adds an expense
4) System calculates balances
5) User views balances
6) User views expense-level split details

## PAGES:
1) (/home)home - shows groups, button to add group,
2) (/newgroup/)new group - name, existing users(members)
3) (/group/<id>/)grouppage - show expenses, button to add expense
4) (/group/<id>/about) groupdetails - show group members and net balance per member
5) (/newexpense/)new expense - name, paid_by, amount, split type, add members 
6) (/expense/<id>/)expensepage - show amount paid by user and split amounts of each member
7) (/profile/) profile page - name, account, logout, delete account (later)

## CORE ENTITIES:
- User: represents a registered user
- Group: represents a collection of users
- GroupMember: mapping between user and group
- Expense: represents a payment made by a user in a group
- ExpenseSplit: represents how an expense is shared among members (equal split, exact amount split)