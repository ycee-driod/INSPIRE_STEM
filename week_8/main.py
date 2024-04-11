import flet as ft

def main(page: ft.page):
    page.title = "Learning FLET"
    content = ft.column(
        spacing=20,
        controls=[
        ft.Text("This is a sample flet application", size=32, weight="w600"),
        ft.Text("Welcome to learning flet", size=16),
        ft.Row(
            spacing=20,
            controls=[
                ft.Text("This is a row in flet"),
                ft.ElevatedButton("Click Me")
            ]
        )
    ]
)

    #DISPLAY OUT SCREEN
    page.add()
