from src.models.music_repository import music_enrollement
from src.models.entities.music_registry import RegistryMusic


class RegistryMusicController:
    def registry(self, music: str):
        try:
            music_count = music_enrollement.count_musics()
            new_music_id = str(music_count + 1)

            new_music = RegistryMusic(new_music_id, music)
            music_enrollement.registry_music(new_music)

            return new_music
        except:
            return None
