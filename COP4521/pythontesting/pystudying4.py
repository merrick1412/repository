import threading

bank = 1000
block = 0
def banktransaction(amnt,lock,event):
    with lock:
        global bank
        global block
        test = bank
        block = 0
        if amnt < 0:
             if (test + bank) < 0:
                 block = amnt
                 print("Cannot withdraw. Waiting for deposit")
                 event.clear()
                 event.wait()
             bank = bank + amnt
             block = 0
             return
        bank = bank + amnt
        if bank > (block * -1):
            event.set()
        return
def main():
    print("starting balance is $1000 dollars")
    lock = threading.Lock()
    withdrawal_event = threading.Event()
    withdrawal_event.set()
    threads = []
    instr = input("enter amounts seperated by commas")
    transactions = list(map(int, instr.split(',')))
    for transaction in transactions:
        threads.append(threading.Thread(target=banktransaction, args=(transaction,lock,withdrawal_event)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    global bank
    print(f"the current balance is ${bank}")
if __name__ == "__main__":
    main()
