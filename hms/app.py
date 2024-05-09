from datetime import datetime

import flet as ft
from sqlmodel import Field, Session, SQLModel, create_engine, select

engine = create_engine("sqlite:///database.db")


class Client(SQLModel, table=True):
    id: int = Field(primary_key=True)
    first_name: str
    last_name: str
    room_number: int
    room_type: str
    status: str
    payment: str
    date: datetime
    email: str
    password: str = Field(default="111")


ROOM_TYPES = ["Single", "Double", "Family", "Suite"]
PAYMENT_STATUS = ["Paid", "Pending"]
STATUS = ["Booked", "Checked In", "Checked Out", "Cancelled"]


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def home_view(page: ft.Page) -> ft.View:
    admin_button = ft.ElevatedButton(
        "Continue as Admin", on_click=lambda _: page.go("/admin"), height=50, width=200
    )
    client_button = ft.ElevatedButton(
        "Continue as Client",
        on_click=lambda _: page.go("/client"),
        height=50,
        width=200,
    )

    view = ft.View(
        appbar=ft.AppBar(title=ft.Text("Hotel Management System")),
        route="/",
        controls=[
            ft.Row(
                spacing=30,
                controls=[admin_button, client_button],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
    )

    return view


def admin_login_view(page: ft.Page):
    text = ft.Text("Login as Admin", size=24, text_align=ft.TextAlign.CENTER)
    password = ft.TextField(password=True, label="Password", width=400)
    message = ft.Text("", size=14)
    submit_button = ft.FilledButton("Login", width=150, height=40)

    view = ft.View(
        appbar=ft.AppBar(title=ft.Text("Admin Login")),
        route="/admin",
        controls=[
            ft.Column(
                spacing=40,
                controls=[text, password, message, submit_button],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def on_submit_click(e):
        if password.value == "000":
            page.go("/admin/dashboard")
        else:
            message.value = "Invalid password"
            page.update()

    submit_button.on_click = on_submit_click

    return view


def admin_dashboard_view(page: ft.Page):
    app_bar = ft.AppBar(title=ft.Text("Admin Dashboard"))

    new_client_button = ft.FilledButton(
        "New Client",
        on_click=lambda _: page.go("/admin/dashboard/client/new"),
        icon="add",
    )

    columns = [
        ft.DataColumn(ft.Text("ID")),
        ft.DataColumn(ft.Text("First Name")),
        ft.DataColumn(ft.Text("Last Name")),
        ft.DataColumn(ft.Text("Email")),
        ft.DataColumn(ft.Text("Room Number")),
        ft.DataColumn(ft.Text("Room Type")),
        ft.DataColumn(ft.Text("Status")),
        ft.DataColumn(ft.Text("Payment")),
        ft.DataColumn(ft.Text("Date")),
        ft.DataColumn(ft.Text("Actions")),
    ]

    rows = []
    with Session(engine) as session:
        query = select(Client).order_by(Client.id)
        clients = session.exec(query).all()

        for client in clients:
            rows.append(
                ft.DataRow(
                    [
                        ft.DataCell(ft.Text(str(client.id))),
                        ft.DataCell(ft.Text(client.first_name)),
                        ft.DataCell(ft.Text(client.last_name)),
                        ft.DataCell(ft.Text(client.email)),
                        ft.DataCell(ft.Text(str(client.room_number))),
                        ft.DataCell(ft.Text(client.room_type)),
                        ft.DataCell(ft.Text(client.status)),
                        ft.DataCell(ft.Text(client.payment)),
                        ft.DataCell(ft.Text(client.date.strftime("%Y-%m-%d %H:%M:%S"))),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        "Edit",
                                        on_click=(
                                            lambda current_id=client.id: lambda _: page.go(
                                                f"/admin/dashboard/client/{current_id}/edit"
                                            )
                                        )(),
                                    )
                                ],
                                spacing=10,
                                alignment=ft.MainAxisAlignment.CENTER,
                            )
                        ),
                    ]
                )
            )

    clients_table = ft.DataTable(columns=columns, rows=rows, expand_loose=True)

    top_row = ft.Row(
        controls=[new_client_button],
        alignment=ft.MainAxisAlignment.END,
        spacing=10,
    )

    view = ft.View(
        appbar=app_bar,
        route="/admin/dashboard",
        controls=[
            ft.Column(
                controls=[top_row, clients_table],
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS,
                expand=True,
            )
        ],
    )

    return view


def admin_dashboard_client_edit_view(page: ft.Page, client_id: int):
    app_bar = ft.AppBar(title=ft.Text("Edit Client"))

    client = None
    with Session(engine) as session:
        statement = select(Client).where(Client.id == client_id)
        client = session.exec(statement).one()

    first_name = ft.TextField(label="First Name", value=client.first_name)
    last_name = ft.TextField(label="Last Name", value=client.last_name)
    email = ft.TextField(label="Email", value=client.email)
    room_number = ft.TextField(label="Room Number", value=client.room_number)
    room_type = ft.Dropdown(
        label="Room Type",
        options=[ft.dropdown.Option(room_type) for room_type in ROOM_TYPES],
        value=client.room_type,
    )
    status = ft.Dropdown(
        label="Status",
        options=[ft.dropdown.Option(status) for status in STATUS],
        value=client.status,
    )
    payment = ft.Dropdown(
        label="Payment",
        options=[ft.dropdown.Option(payment) for payment in PAYMENT_STATUS],
        value=client.payment,
    )

    error_message = ft.Text("")

    submit_button = ft.ElevatedButton("Update")

    delete_button = ft.ElevatedButton("Delete")

    def delete_client(e):
        with Session(engine) as session:
            session.delete(client)
            session.commit()

            page.go("/admin/dashboard")

    delete_button.on_click = delete_client

    view = ft.View(
        appbar=app_bar,
        route=f"/admin/dashboard/client/{client_id}/edit",
        controls=[
            ft.Column(
                width=400,
                controls=[
                    first_name,
                    last_name,
                    email,
                    room_number,
                    room_type,
                    status,
                    payment,
                    error_message,
                    ft.Row(
                        controls=[submit_button, delete_button],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
    )

    def on_submit_click(e):
        message = validate_client_data(
            first_name.value,
            last_name.value,
            email.value,
            room_number.value,
            room_type.value,
            status.value,
            payment.value,
        )

        if message:
            error_message.value = message
            page.update()
            return

        with Session(engine) as session:
            client.first_name = first_name.value
            client.last_name = last_name.value
            client.email = email.value
            client.room_number = room_number.value
            client.room_type = room_type.value
            client.status = status.value
            client.payment = payment.value

            session.add(client)

            session.commit()
            page.go("/admin/dashboard")

    submit_button.on_click = on_submit_click

    return view


def validate_client_data(
    first_name, last_name, email, room_number, room_type, status, payment
):
    if not first_name:
        return "First Name is required"

    if not last_name:
        return "Last Name is required"

    if not email:
        return "Email is required"

    if not room_number:
        return "Room Number is required"

    if not room_type:
        return "Room Type is required"

    if not status:
        return "Status is required"

    if not payment:
        return "Payment is required"

    return ""


def admin_dashboard_client_new_view(page: ft.Page):
    app_bar = ft.AppBar(title=ft.Text("New Client"))

    first_name = ft.TextField(label="First Name")
    last_name = ft.TextField(label="Last Name")
    email = ft.TextField(label="Email")
    room_number = ft.TextField(label="Room Number")
    room_type = ft.Dropdown(
        label="Room Type",
        options=[ft.dropdown.Option(room_type) for room_type in ROOM_TYPES],
    )
    status = ft.Dropdown(
        label="Status",
        options=[ft.dropdown.Option(status) for status in STATUS],
    )
    payment = ft.Dropdown(
        label="Payment",
        options=[ft.dropdown.Option(payment) for payment in PAYMENT_STATUS],
    )
    error_message = ft.Text("")

    submit_button = ft.ElevatedButton("Create")

    heading = ft.Text("Create New Client", size=24, text_align=ft.TextAlign.CENTER)

    view = ft.View(
        appbar=app_bar,
        route="/admin/dashboard/client/new",
        controls=[
            ft.Column(
                width=400,
                spacing=20,
                controls=[
                    heading,
                    first_name,
                    last_name,
                    email,
                    room_number,
                    room_type,
                    status,
                    payment,
                    error_message,
                    ft.Row(
                        controls=[submit_button],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def on_submit_click(e):
        message = validate_client_data(
            first_name.value,
            last_name.value,
            email.value,
            room_number.value,
            room_type.value,
            status.value,
            payment.value,
        )

        if message:
            error_message.value = message
            page.update()
            return

        with Session(engine) as session:
            client = Client(
                first_name=first_name.value,
                last_name=last_name.value,
                email=email.value,
                room_number=room_number.value,
                room_type=room_type.value,
                status=status.value,
                payment=payment.value,
                date=datetime.now(),
            )

            session.add(client)
            session.commit()

            page.go("/admin/dashboard")

    submit_button.on_click = on_submit_click

    return view


def client_login_view(page: ft.Page):
    text = ft.Text("Welcome, Please Enter your Email and Password", size=24)
    email = ft.TextField(label="Email", width=400)
    password = ft.TextField(password=True, label="Password", width=400)
    message = ft.Text("", size=14)
    submit_button = ft.FilledButton("Continue")

    view = ft.View(
        appbar=ft.AppBar(title=ft.Text("Login")),
        route="/client",
        controls=[
            ft.Column(
                spacing=30,
                controls=[text, email, password, message, submit_button],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def on_submit_click(e):
        with Session(engine) as session:
            statement = select(Client).where(Client.email == email.value)
            client = session.exec(statement).first()

            if client and client.password == password.value:
                page.go(f"/client/{client.id}")
            else:
                message.value = "Invalid email or password"
                page.update()

    submit_button.on_click = on_submit_click

    return view


def client_home_view(page: ft.Page, client_id: int):
    client = None
    with Session(engine) as session:
        statement = select(Client).where(Client.id == client_id)
        client = session.exec(statement).first()

    app_bar = ft.AppBar(
        title=ft.Text(f"Welcome {client.first_name} {client.last_name}", size=24)
    )

    current_status = ft.Text(
        f"Current Status: {client.status}", size=24, text_align=ft.TextAlign.CENTER
    )

    # Check In Button
    check_in_button = ft.FilledButton(
        "Check In", height=50, width=200, disabled=client.status == "Checked In"
    )

    # Check Out Button
    check_out_button = ft.FilledButton(
        "Check Out", height=50, width=200, disabled=client.status == "Checked Out"
    )

    # Cancel Booking Button
    cancel_booking_button = ft.FilledButton(
        "Cancel Booking", height=50, width=200, disabled=client.status == "Cancelled"
    )

    def on_check_in_click(e):
        with Session(engine) as session:
            client.status = "Checked In"
            client.date = datetime.now()
            session.add(client)
            session.commit()

            page.go(f"/client/{client_id}/room")

    def on_check_out_click(e):
        with Session(engine) as session:
            client.status = "Checked Out"
            client.date = datetime.now()
            session.add(client)
            session.commit()

            page.go("/")

    def on_cancel_booking_click(e):
        with Session(engine) as session:
            client.status = "Cancelled"
            client.date = datetime.now()
            session.add(client)
            session.commit()

            page.go("/")

    check_in_button.on_click = on_check_in_click
    check_out_button.on_click = on_check_out_click
    cancel_booking_button.on_click = on_cancel_booking_click

    # Button Row
    button_row = ft.Row(
        controls=[check_in_button, check_out_button, cancel_booking_button],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    view = ft.View(
        appbar=app_bar,
        route=f"/client/{client_id}",
        controls=[
            ft.Column(
                controls=[current_status, button_row],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )

    return view


def client_room_view(page: ft.Page, client_id: int):
    client = None
    with Session(engine) as session:
        statement = select(Client).where(Client.id == client_id)
        client = session.exec(statement).first()

    app_bar = ft.AppBar(title=ft.Text(f"Welcome to Room {client.room_number}"))

    payment_status = ft.Text(f"Payment Status: {client.payment}", size=24)

    last_action = ft.Text(
        f"Last Action At: {client.date.strftime('%Y-%m-%d %H:%M:%S')}", size=24
    )

    current_status = ft.Text(f"Current Status: {client.status}", size=24)

    view = ft.View(
        appbar=app_bar,
        route=f"/client/{client_id}/room",
        controls=[payment_status, last_action, current_status],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )

    return view


def main(page: ft.Page):
    create_db_and_tables()

    page.window_maximized = True
    page.title = "Hotel Management System"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.fonts = {
        "Montserrat": "https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap"
    }

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()

        page.views.append(
            home_view(page),
        )

        if e.route == "/admin":
            page.views.append(admin_login_view(page))

        if e.route == "/admin/dashboard":
            page.views.append(admin_dashboard_view(page))

        if e.route == "/admin/dashboard/client/new":
            page.views.append(admin_dashboard_client_new_view(page))

        if e.route == "/client":
            page.views.append(client_login_view(page))

        troute = ft.TemplateRoute(page.route)

        if troute.match("/admin/dashboard/client/:id/edit"):
            page.views.append(admin_dashboard_client_edit_view(page, troute.id))

        if troute.match("/client/:id"):
            page.views.append(client_home_view(page, troute.id))

        if troute.match("/client/:id/room"):
            page.views.append(client_room_view(page, troute.id))

        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")


ft.app(main)
