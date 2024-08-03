import random

def initialize():
    while True:
        usr_input = input("Choose grid size 8, 16, or 32 >> ")
        try: 
            grid_size = int(usr_input)
            break
        except:
            print("Must be 8, 16, or 32!")
        
    generate_tiles(grid_size)

def generate_tiles(grid_size):
    grid = []
    gui = ""
    for i in range(grid_size * grid_size):
        grid.append(i)
        if i % grid_size == 0:
            gui = gui + "\n"
        gui = gui + " - "
    
    print(gui)

def main():
    initialize()

if __name__ == "__main__":
    main()