import curses
import random

# Initialize the game screen
def init_screen():
    screen = curses.initscr()  # Initialize the curses screen
    curses.curs_set(0)  # Hide the cursor
    screen.nodelay(1)  # Make getch() non-blocking
    screen.timeout(150)  # Set timeout for input
    return screen

# Generate a random position for food, avoiding the snake and obstacles
def generate_food(snake, obstacles, screen, is_special=False):
    food_symbol = 'X' if is_special else 'π'  # Choose symbol based on food type
    while True:
        food = [random.randint(1, screen.getmaxyx()[0] - 2),  # Generate random y position
                random.randint(1, screen.getmaxyx()[1] - 2)]  # Generate random x position
        if food not in snake and food not in obstacles:  # Ensure food doesn't spawn on snake or obstacles
            screen.addch(food[0], food[1], food_symbol)  # Display the food on screen
            return food  # Return the food position

# Generate obstacles randomly on the screen
def generate_obstacles(screen):
    obstacles = []  # List to store obstacle positions
    total_cells = (screen.getmaxyx()[0] - 2) * (screen.getmaxyx()[1] - 2)  # Calculate total cells
    obstacle_cells = total_cells // 20  # 5% of the game area
    while len(obstacles) < obstacle_cells:  # Loop until the required number of obstacles is generated
        is_vertical = random.choice([True, False])  # Randomly decide if obstacle is vertical or horizontal
        start_x = random.randint(1, screen.getmaxyx()[0] - 2)  # Random start position x
        start_y = random.randint(1, screen.getmaxyx()[1] - 2)  # Random start position y
        length = random.randint(5, 10)  # Random length of obstacle
        for i in range(length):
            x = start_x + i if is_vertical else start_x  # Calculate x position
            y = start_y if is_vertical else start_y + i  # Calculate y position
            if 1 <= x < screen.getmaxyx()[0] - 1 and 1 <= y < screen.getmaxyx()[1] - 1:  # Ensure position is within bounds
                obstacles.append([x, y])  # Add obstacle to list
                screen.addch(x, y, ' ', curses.A_REVERSE)  # Display the obstacle on screen
    return obstacles  # Return the list of obstacles

# Calculate the new position of the snake's head based on the current direction
def get_new_head(direction, head, max_y, max_x):
    if direction == curses.KEY_DOWN:
        new_head = [head[0] + 1, head[1]]  # Move down
    elif direction == curses.KEY_UP:
        new_head = [head[0] - 1, head[1]]  # Move up
    elif direction == curses.KEY_LEFT:
        new_head = [head[0], head[1] - 1]  # Move left
    elif direction == curses.KEY_RIGHT:
        new_head = [head[0], head[1] + 1]  # Move right
    new_head[0] = new_head[0] % max_y  # Wrap around the screen vertically
    new_head[1] = new_head[1] % max_x  # Wrap around the screen horizontally
    return new_head  # Return the new head position

# Main game logic
def main(screen):
    # Initialize snake and food
    snake = [[5, 10], [5, 9], [5, 8]]  # Initial snake position
    direction = curses.KEY_RIGHT  # Initial direction
    food = generate_food(snake, [], screen)  # Generate initial food
    special_food = generate_food(snake, [food], screen, is_special=True)  # Generate initial special food
    obstacles = generate_obstacles(screen)  # Generate initial obstacles
    normal_food_eaten = 0  # Counter for normal food eaten
    special_food_eaten = 0  # Counter for special food eaten

    while True:
        # Get user input for direction change
        next_key = screen.getch()  # Get the next key pressed
        if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:  # Check if it is a direction key
            direction = next_key  # Update direction

        # Calculate the new position of the snake's head
        new_head = get_new_head(direction, snake[0], screen.getmaxyx()[0], screen.getmaxyx()[1])

        # Check for game over conditions
        if new_head in snake or new_head in obstacles:  # If the snake hits itself or an obstacle
            break  # End the game

        # Update the position of the snake
        snake.insert(0, new_head)  # Add the new head position to the snake
        if new_head == food:  # If the snake eats normal food
            normal_food_eaten += 1  # Increment normal food counter
            food = generate_food(snake, obstacles, screen)  # Generate new food
        elif new_head == special_food:  # If the snake eats special food
            special_food_eaten += 1  # Increment special food counter
            special_food = generate_food(snake, obstacles, screen, is_special=True)  # Generate new special food
            if len(snake) > 1:
                print(len(snake))  # Debug print statement for the snake's length
                snake.pop()  # Remove the last segment if the snake ate special food
        else:
            snake.pop()  # Remove the last segment if the snake didn't eat food

        # Draw the snake, food, and obstacles on the screen
        screen.clear()  # Clear the screen
        for segment in snake:  # Draw each segment of the snake
            screen.addch(segment[0], segment[1], '*')
        screen.addch(food[0], food[1], 'π')  # Draw normal food
        screen.addch(special_food[0], special_food[1], 'X')  # Draw special food
        for obstacle in obstacles:  # Draw each obstacle
            screen.addch(obstacle[0], obstacle[1], ' ', curses.A_REVERSE)
        screen.refresh()  # Refresh the screen to show updates

    # Display game over message
    screen.clear()  # Clear the screen
    screen.addstr(screen.getmaxyx()[0] // 2, screen.getmaxyx()[1] // 2 - 10, f"Game Over! Normal: {normal_food_eaten} Special: {special_food_eaten}")  # Show game over message
    screen.refresh()  # Refresh the screen to show the message
    screen.timeout(-1)  # Wait indefinitely for a key press
    screen.getch()  # Wait for a key press

# Start the game
curses.wrapper(main)  # Wrap the main function in curses.wrapper to initialize and clean up curses properly
