# Part 1 and Part 2
# Zheng Lin Lei


from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "../input.txt")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        elf_meals = f.read().split("\n\n") # split on empty lines
    
    elf_calories = [] # store total calories for each elf
    for elf in elf_meals:
        calories = sum(map(int, elf.splitlines()))
        elf_calories.append(calories)
        
    print(f"Part 1: {max(elf_calories)}")
    
    elf_calories = sorted(elf_calories)
    print(f"Part 2: {elf_calories[-3:]}")
    print(f"Part 2: {sum(elf_calories[-3:])}")
    

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")