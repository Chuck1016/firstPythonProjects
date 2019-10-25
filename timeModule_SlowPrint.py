import sys, time

def slowPrint(text, delay=0.025):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print
    
slowPrint("It was a dark and stormy night.\n")
time.sleep(1)
slowPrint("Three travelers, exhausted from their long journey, see a light in the distance.\n")
time.sleep(1)
slowPrint("A castle is ahead. It could mean refuge.\n")
time.sleep(1)
slowPrint("Or it could mean doom...")
