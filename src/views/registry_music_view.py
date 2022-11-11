import os


class RegistryMusicViews:
    def registry_music_page(self) -> str:
        self.__clear()

        print("Registry the music \n\n")
        music = input("Add the song name: ")

        return music

    def registry_music_success(self, new_music_name: any) -> None:
        self.__clear()

        message = """
            Music successfully registered!
            * Infos:
                Song id: {}
                Name song: {} 
          """.format(
            new_music_name.id, new_music_name.music
        )
        print(message)

    def registry_class_fail(self) -> None:
        self.__clear()

        message = """
              There was an error when registering the music, check the fields displayed
        """
        print(message)

    def __clear(self):
        os.system("cls|clear")
