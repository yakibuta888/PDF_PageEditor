import os
import datetime


class File():
    def __init__(self, input_file_path: str, output_file_path: str) -> None:
        if input_file_path:
            self.__input_file_path = input_file_path
        else:
            raise ValueError('不正なファイルパスです。')

        if output_file_path:
            self.__output_file_path = output_file_path
        else:
            now: str = datetime.datetime.now(
                datetime.timezone(datetime.timedelta(hours=9))
            ).strftime('%Y%m%d_%H%M%S')
            file_name: str = os.path.splitext(
                os.path.basename(self.__input_file_path)
            )[0]
            output_file_name: str = f'{file_name}_edited{now}.pdf'
            self.__output_file_path: str = os.path.normpath(
                os.path.join(
                    os.path.dirname(self.__input_file_path),
                    output_file_name
                )
            )

    @property
    def input_file_path(self) -> str:
        return self.__input_file_path

    @property
    def output_file_path(self) -> str:
        return self.__output_file_path
