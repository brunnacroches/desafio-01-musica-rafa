from src.views.create_music_playlist_view import CreateMusicPlaylistViews
from src.controllers.create_music_playlist_controller import (
    CreateMusicPlaylistController,
)


def create_music_playlist_process() -> None:
    create_music_playlist_view = CreateMusicPlaylistViews
    create_music_playlist_controller = CreateMusicPlaylistController

    create_music_playlist_informations = create_music_playlist_view()
    response = create_music_playlist_controller.find(create_music_playlist_informations)

    if response["Success"]:
        create_music_playlist_view.create_music_playlist_success(response["registry"])
    else:
        create_music_playlist_view.create_music_playlist_fail(response["error"])
