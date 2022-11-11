from src.views.find_all_music_view import FindAllMusicViews
from src.controllers.find_all_music_controller import FindAllMusicController


def find_all_music_process() -> None:
    find_all_music_views = FindAllMusicViews()
    find_all_music_controller = FindAllMusicController()

    music_informations = find_all_music_views.find_all_music_views()
    response = find_all_music_controller.find(music_informations)

    if response["success"]:
        find_all_music_views.find_all_music_success(response["registry"])
    else:
        find_all_music_views.find_all_music_fail(response["error"])
