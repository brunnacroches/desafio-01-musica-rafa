from typing import Dict
from src.models.music_repository import music_enrollement


class FindAllMusicController:
    def find(self, music_name: str):
        try:
            music_registry = self.__search_all_music_registry(music_name)
            registry = self.__format_registry_info(music_registry)
            return {"success": True, "registry": registry}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __search_all_music_registry(self, music_name: str) -> any:
        music_registry = music_enrollement.get_music(music_name)
        if music_registry is None:
            raise Exception("Music not found! ")

        return music_registry

    def __format_registry_info(self, music_registry: any):
        return {
            "id": music_registry.id,
            "name": music_registry.name,
            "year": music_registry.year,
            "genre": music_registry.genre,
            "playlist": music_registry.playlist,
        }
