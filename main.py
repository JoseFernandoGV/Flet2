import flet as ft


def main(page: ft.Page):
    btn=0
    c = ft.Container(
        width=100,
        height=100,
        bgcolor="blue",
        border_radius=5,
        scale=ft.transform.Scale(scale=1),
        animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
    )

    def animate(e):
        print(btn.data)
        if btn.data ==1:
            print("Condicional")
            c.scale=1
            btn.data = 0
        else: 
            c.scale = 2
            btn.data+=1
        page.update()

    def animate3(e):
        print("Fernando el poderoso estuvo aquí")

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    btn = ft.ElevatedButton(text="Animate!", on_click=animate, data =0)
    page.add(
        c,
        btn,
    )

# open a browser tab containing the app | remove the view parameter to open in a native OS window
ft.app(target=main, view=ft.WEB_BROWSER)
