import os


class RegistryYearMusicViews:
    def registry_year_music_page(self) -> str:
        self.__clear()

        print("Registry year the music \n\n")
        music_year = input("Add the year song: ")

        return music_year

    def registry_year_music_success(self, new_year_music: any) -> None:
        self.__clear()

        message = """
            Music year successfully registered!
            * Infos:
                Song id: {}
                Name song: {}
                Year song: {}
          """.format(
            new_year_music.id, new_year_music.music
        )
        print(message)

    def registry_year_music_fail(self) -> None:
        self.__clear()

        message = """
              There was an error when registering the year music, check the fields displayed
        """
        print(message)

    def __clear(self):
        os.system("cls|clear")
