from src.models.music_repository import music_enrollement
from src.models.entities.music_registry import RegistryMusic


class RegistryYearMusicController:
    def registry(self, music: str):
        try:
            music_count = music_enrollement.count_musics()
            new_year_music_id = str(music_count + 1)

            new_year_music = RegistryMusic(new_year_music_id, music)
            music_enrollement.registry_year_music_controller(new_year_music)

            return new_year_music
        except:
            return None
