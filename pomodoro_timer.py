import time

def pomodoro_timer(pomodoro_duration, break_duration, cycles):
    for cycle in range(cycles):
        print(f"Pomodoro {cycle + 1}/{cycles}")
        countdown(pomodoro_duration)
        print("\nTime's up! Take a break.")
        time.sleep(1)
        countdown(break_duration)
        print("\nBreak's over!")

def countdown(duration):
    for minute in range(duration, 0, -1):
        print(f"Time left: {minute} minutes", end="\r")
        time.sleep(60)

if __name__ == "__main__":
    pomodoro_duration = 25  
    break_duration = 5      
    cycles = 4              
    
    pomodoro_timer(pomodoro_duration, break_duration, cycles)
