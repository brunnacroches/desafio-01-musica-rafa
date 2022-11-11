class __MusicEnrollement:
    def __init__(self) -> None:
        self.musics = []
        self.music_name = []
        self.music_year = []

        def count_musics(self) -> int:
            return len(self.musics)

        def count_music_name(self) -> int:
            return len(self.music_name)

        def count_music_year(self) -> int:
            return len(self.music_year)

        def registry_music(self, musics: any) -> None:
            self.musics.append(musics)

        def registry_music_name(self, music_name: any) -> None:
            self.music_name.append(music_name)

        def registry_music_year(self, music_year: any) -> None:
            self.music_year.append(music_year)

        def get_musics(self, musics_id: str) -> any:
            for registry in self.musics:
                if registry.name == musics_id:
                    return registry

            return None

        def get_music_name(self, music_name: str) -> any:
            for registry in self.music_name:
                if registry.name == music_name:
                    return registry

                return None

        def get_music_year(self, music_year: str) -> any:
            for registry in self.music_year:
                if registry.number == music_year:
                    return registry

        def get_music_by_id(self, music_id: str):
            musics = []
            for registry in self.musics:
                if registry.musics.id == music_id:
                    musics.append(registry)

            return musics


music_enrollement = __MusicEnrollement()
