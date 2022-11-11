def introduction_page():
    message = """
        Music System

        * Register Music - 1 
        * Find Music - 2
        * Find All Music - 3
        * Create Playlist Music - 4
        * Exit - 5 
    """
    print(message)
    command = input("Command: ")

    return command
