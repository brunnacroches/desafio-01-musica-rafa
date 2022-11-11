from src.views.find_music_view import FindMusicViews
from src.controllers.find_music_controller import FindMusicController


def find_music_process() -> None:
    find_music_views = FindMusicViews()
    find_music_controller = FindMusicController()

    music_informations = find_music_views.find_music_view()
    response = find_music_controller.find(music_informations)

    if response["success"]:
        find_music_views.find_music_success(response["registry"])
    else:
        find_music_views.find_music_fail(response["error"])
