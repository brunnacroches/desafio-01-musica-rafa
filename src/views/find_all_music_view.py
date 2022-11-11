import os


class FindAllMusicViews:
    def find_all_music_views(self) -> str:
        self.__clear()

        print("Search Registry Music \n\n")
        music_name = input("Set the name of the song to search: ")

        return music_name

    def find_all_music_success(self, music_registry: any) -> None:
        self.__clear()

        message = """
        Music Registration
        * Infos:
          Music ID: {}
          Music Name: {}
          Year Music: {}
          Genre Music: {}
          Playlist Music: {}
      """.format(
            music_registry["id"],
            music_registry["name"],
            music_registry["year"],
            music_registry["genre"],
            music_registry["playlist"],
        )
        print(message)

    def find_all_music_fail(self, error: str) -> None:
        self.__clear()

        message = """
          There was an error fetching the song.
          {}
      """.format(
            error
        )
        print(message)

    def __clear(self):
        os.system("cls||clear")
