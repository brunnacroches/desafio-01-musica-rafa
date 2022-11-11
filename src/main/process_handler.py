from .constructor.introduction_process import introduction_process
from .constructor.registry_music_process import registry_music_process
from .constructor.registry_year_music_process import registry_year_music_process
from .constructor.find_music_process import find_music_process
from .constructor.find_all_music_process import find_all_music_process
from .constructor.create_music_playlist_process import create_music_playlist_process


def start() -> None:
    while True:
        command = introduction_process()

        if command == "1":
            registry_music_process()
        if command == "2":
            registry_year_music_process()
        if command == "3":
            find_music_process()
        elif command == "4":
            find_all_music_process()
        elif command == "5":
            create_music_playlist_process()
        elif command == "6":
            exit()
        else:
            print("\nCommand not found, try again")
