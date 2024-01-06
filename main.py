import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!", style="center")))

    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)

    file_picker = ft.FilePicker(on_result=on_dialog_result)

    def upload_files(e):
        upload_list = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                upload_list.append(
                    ft.FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(upload_list)
        page.add(ft.ElevatedButton("Click me!", on_click=upload_files))


ft.app(main)
