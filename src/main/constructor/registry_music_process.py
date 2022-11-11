from src.views.registry_music_view import RegistryMusicViews
from src.controllers.registry_music_controller import RegistryMusicController


def registry_music_process() -> None:
    registry_music_view = RegistryMusicViews()
    registry_music_controller = RegistryMusicController()

    music = registry_music_view.registry_music_page()
    new_music = registry_music_controller.registry(music)

    if new_music is not None:
        registry_music_view.registry_music_success(new_music)
    else:
        registry_music_view.registry_music_fail()
