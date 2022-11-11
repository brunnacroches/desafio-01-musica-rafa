import os


class FindMusicViews:
    def find_music_view(self) -> str:
        self.__clear()

        print("Class Registration Search \n\n")
        music_id = input("Set the class id to search")

        return music_id

    def find_music_success(self, music_registry: any) -> None:
        self.__clear()

        message = """
        Turna {} - Music {}
        * Infos:
      """.format(
            music_registry["music_id"], music_registry["music_class"]
        )

        for registry in music_registry["registries"]:
            message += """ \n
          Music ID: {}
          Music Name: {}
          Year Music: {}
          Genre Music
          Music Playlist: {}
        """.format(
                registry["id"],
                registry["name"],
                registry["year"],
                registry["genre"],
                registry["playlist"],
            )

        print(message)

    def find_music_fail(self, error: str) -> None:
        self.__clear()

        message = """
            There was an error searching for the song
            {}
      """.format(
            error
        )
        print(message)

    def __clear(self):
        os.system("cls||clear")
