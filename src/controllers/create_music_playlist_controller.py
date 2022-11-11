from typing import Dict
from src.models.music_repository import music_enrollement


class CreateMusicPlaylistController:
    def create_music_playlist_controller(self, playlist_name: str):
        try:
            create_music_playlist_registries = (
                self.__search_create_music_playlist_registries_by_class_id(
                    playlist_name
                )
            )
            registries = self.__format_registries_info(create_music_playlist_registries)
            return {"success": True, "registries": registries}

        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __search_create_music_playlist_by_class_id(self, class_id: str) -> any:
        create_music_playlist_registries = (
            music_enrollement.get_create_music_playlist_by_class_id(class_id)
        )
        if create_music_playlist_registries is None:
            raise Exception("Empty Playlist")

        return create_music_playlist_registries

    def __format_registries_info(self, create_music_playlist_registries: any):

        class_id = create_music_playlist_registries[0].create_music.id
        class_create_music_playlist = create_music_playlist_registries[
            0
        ].create_music.musics

        registries = []
        for musics in create_music_playlist_registries:
            create_music_playlist_registries.append(
                {
                    "id": musics.id,
                    "name": musics.name,
                    "year": musics.year,
                    "genre": musics.genre,
                    "playlist": musics.playlist,
                }
            )

        return {
            "class_id": class_id,
            "class_create_music_playlist": class_create_music_playlist,
            "registries": registries,
        }
