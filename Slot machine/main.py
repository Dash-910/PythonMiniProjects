import random

# Setting no of lines as constant
MAX_LINES = 5
# Setting max amount of bet as constant
MAX_BET = 100
# Setting min amount of bet as constant 
MIN_BET = 1
# No of rows
ROWS =3
# No of columns
COLS=3

symbol_count = {
    "A":2,
    "B":4,
    "c":6,
    "D":8
}
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}


# chech the wining amount
def check_winnings(columns,lines,bet,values):
    winnings = 0;
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]* bet
            winning_lines.append(line +1)
    # if the user dosn't win a single line
    if not winning_lines:
        print("No winning lines")

    return winnings,winning_lines


# Slot machine logic
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols =[]
    # we used .items() to get both key and value from the dic
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        # [:] is used to make a copy and not give refrence
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    if not columns:
        print("Not enough symbold to fill all reels")
        return 

    return columns
# Print slot_machine
def print_slot_machine(columns):
    # The columns is transposed 
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns)-1:
                # end tells the print state what to end the line with
                print(column[row], "|",end=" |")
            else:
                print(column[row],end=" | ")
        print()


# Deposit func
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Plese enter a number.")

    return amount
# To get the no of lines
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1- " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

#To get the bet amount
def get_bet():
     while True:
        amount = input("What would you like to bet on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} .")
        else:
            print("Plese enter a number.")

     return amount


# spin the slot machine
def spin(balance):
    lines = get_number_of_lines()
    # To check if the bet amount is bigger than the balance
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
          print("You do not have enough to bet that amount, Your current balance is :${balance}")
        else:
            break

    bet = get_bet()
    total_bet = lines * bet
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}")
    # * is spat opertor ,will print out all the values in winning_lines
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit ()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press enter to play(q to quit).")
        if ans == 'q':
            break
        balance += spin(balance)

    print("You left with ${balance}")

main()

