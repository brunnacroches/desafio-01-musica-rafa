from src.views.registry_year_music_view import RegistryYearMusicViews
from src.controllers.registry_year_music_controller import RegistryYearMusicController


def registry_year_music_process() -> None:
    registry_year_music_view = RegistryYearMusicViews()
    registry_year_music_controller = RegistryYearMusicController()

    music_year = registry_year_music_view.registry_year_music_page()
    new_year_music = registry_year_music_controller.registry(music_year)

    if new_year_music is not None:
        registry_year_music_view.registry_year_music_view(new_year_music)
    else:
        registry_year_music_view.registry_year_music_fail()
