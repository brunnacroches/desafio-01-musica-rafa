import os


class CreateMusicPlaylistViews:
    def create_music_playlist_view(self) -> str:
        self.__clear()

        print("Create Music Playlist \n\n")
        create_music_playlist_name = input(
            "Create the name the music playlist for search: "
        )

        return create_music_playlist_name

    def create_music_playlist_success(
        self, create_music_playlist_registry: any
    ) -> None:
        self.__clear()

        message = """
        Create Music Playlist
        * Infos:
          Playlist Music ID: {}
          Playlist Music Name: {}
          Playlist Music Year: {}
          Playlist Music Genre: {}
    """.format(
            create_music_playlist_registry["id"],
            create_music_playlist_registry["name"],
            create_music_playlist_registry["year"],
            create_music_playlist_registry["genre"],
        )
        print(message)

    def create_music_playlist_fail(self, error: str) -> None:
        self.__clear()

        message = """
          An error occurred while fetching the playlist.
          {}
        """.format(
            error
        )
        print(message)

    def __clear(self):
        os.system("cls||clear")
