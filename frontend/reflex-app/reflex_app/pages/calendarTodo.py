import reflex as rx
import uuid

class HomeState(rx.State):
    
    ...

def generate_id():
    return str(uuid.uuid4())
class Todo(rx.Model, table=True):
    uuid: str
    task: str

def create_icon(icon_tag):
    """Create an icon component with specified tag and styling."""
    return rx.icon(
        tag=icon_tag,
        height="1.25rem",
        display="inline-block",
        width="1.25rem",
    )


def create_icon_button(icon_tag):
    """Create a button with an icon and styling."""
    return rx.el.button(
        create_icon(icon_tag=icon_tag),
        background_color="#E5E7EB",
        _hover={"background-color": "#D1D5DB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        color="#374151",
    )


def create_heading(font_size, line_height, content):
    """Create a heading with specified font size, line height, and content."""
    return rx.heading(
        content,
        font_weight="700",
        margin_bottom="1rem",
        color="#1F2937",
        font_size=font_size,
        # line_height=line_height,
        as_="h2",
    )


def create_bold_box(content):
    """Create a box with bold font weight."""
    return rx.box(content, font_weight="600")


def create_bordered_box(content):
    """Create a box with bottom border and padding."""
    return rx.box(
        create_bold_box(content=content),
        border_bottom_width="1px",
        border_color="#E5E7EB",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
    )


def create_colored_box(background_color, text_color, content):
    """Create a colored box with specified background, text color, and content."""
    return rx.box(
        content,
        background_color=background_color,
        margin_top="0.25rem",
        padding="0.25rem",
        border_radius="0.25rem",
        color=text_color,
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_bordered_colored_box(title, background_color, text_color, content):
    """Create a bordered box with a title and colored content area."""
    return rx.box(
        create_bold_box(content=title),
        create_colored_box(
            background_color=background_color,
            text_color=text_color,
            content=content,
        ),
        border_bottom_width="1px",
        border_color="#E5E7EB",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
    )


def create_checkbox():
    """Create a checkbox input element."""
    return rx.el.input(type="checkbox", margin_right="0.5rem")


def create_text_span(content):
    """Create a text span with specified content and color."""
    return rx.text.span(content, color="#374151")


def create_todo_item(task_text):
    """Create a todo list item with a checkbox and task text."""
    return rx.el.li(
        create_checkbox(),
        create_text_span(content=task_text),
        display="flex",
        align_items="center",
        color="#555",
        width="100%",
        border_bottom="1px dotted #ccc",
        # border= 1px solid #dedede      ,
    )


def create_date_navigation():
    """Create a date navigation component with Today button and navigation arrows."""
    return rx.flex(
        rx.el.button(
            "Today",
            background_color="#3B82F6",
            _hover={"background-color": "#2563EB"},
            padding_left="1rem",
            padding_right="1rem",
            padding_top="0.5rem",
            padding_bottom="0.5rem",
            border_radius="0.5rem",
            color="#ffffff",
        ),
        create_icon_button(icon_tag="chevron-left"),
        create_icon_button(icon_tag="chevron-right"),
        display="flex",
        column_gap="0.5rem",
    )


def create_calendar_header():
    """Create a calendar header with title and date navigation."""
    return rx.flex(
        rx.heading(
            "Calendar",
            font_weight="700",
            font_size="1.875rem",
            line_height="2.25rem",
            color="#1F2937",
            as_="h1",
        ),
        create_date_navigation(),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_bottom="1.5rem",
    )


def create_daily_schedule():
    """Create a daily schedule component with time slots and events."""
    return rx.box(
        create_bordered_box(content="8:00 AM"),
        create_bordered_colored_box(
            title="9:00 AM",
            background_color="#DBEAFE",
            text_color="#1E40AF",
            content="Team Meeting",
        ),
        create_bordered_box(content="10:00 AM"),
        create_bordered_box(content="11:00 AM"),
        create_bordered_colored_box(
            title="12:00 PM",
            background_color="#D1FAE5",
            text_color="#065F46",
            content="Lunch Break",
        ),
        create_bordered_box(content="1:00 PM"),
        create_bordered_colored_box(
            title="2:00 PM",
            background_color="#FEF3C7",
            text_color="#92400E",
            content="Client Call",
        ),
        create_bordered_box(content="3:00 PM"),
        create_bordered_box(content="4:00 PM"),
        create_bordered_colored_box(
            title="5:00 PM",
            background_color="#FEE2E2",
            text_color="#991B1B",
            content="Project Deadline",
        ),
        gap="0.5rem",
        display="grid",
        grid_template_columns="repeat(1, minmax(0, 1fr))",
    )


def create_add_task_button():
    """Create an 'Add Task' button with styling."""
    return rx.el.button(
        "Add Task",
        background_color="#3B82F6",
        _hover={"background-color": "#2563EB"},
        margin_top="0.5rem",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        color="#ffffff",
        width="100%",
    )


def create_task_input_form():
    """Create a form for adding new tasks with input field and submit button."""
    return rx.box(
        rx.el.input(
            type="text",
            placeholder="Add new task",
            border_width="1px",
            border_color="#D1D5DB",
            padding="0.5rem",
            border_radius="0.25rem",
            width="100%",
        ),
        create_add_task_button(),
        margin_top="1rem",
    )


def create_blank_input_form(bg_color, _rowsCount, _placeholder):
    return rx.flex(
        rx.el.textarea(
            type="text",
            style={
                "background_color": bg_color,
                "color": "#000000",
            },
            placeholder=_placeholder,
            border_width="1px",
            border_color="#D1D5DB",
            padding="0.5rem",
            border_radius="0.25rem",
            # height="100%,",
            width="100%",
            rows=_rowsCount,
        ),
        # height="100%,",
        width="100%",
        margin_top="1rem",
    )


def create_todo_list_component():
    """Create a todo list component with title, tasks, and add task form."""
    return rx.box(
        create_heading(
            font_size="1.25rem",
            line_height="1.75rem",
            content="Todo List",
        ),
        rx.list(
            create_todo_item(task_text="Prepare presentation"),
            create_todo_item(task_text="Review project timeline"),
            create_todo_item(task_text="Send follow-up emails"),
            create_todo_item(task_text="Update team on progress"),
            create_todo_item(task_text="Schedule next week's meetings"),
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
        create_task_input_form(),
        background_color="#f5f5f5",
        padding="1rem",
        border_radius="0.5rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        width="100%",
    )


def create_main_content():
    """Create the main content area with calendar and todo list."""
    return rx.hstack(
        rx.box(
            rx.flex(
                create_heading(
                    font_size="1rem",
                    line_height="2rem",
                    content="June 1, 2023",
                ),
                create_date_navigation(),
                display="flex",
                align_items="center",
                justify_content="space-between",
            ),
            create_todo_list_component(),
            background_color="#ffffff",
            flex_grow="1",
            padding="1rem",
            border_radius="0.5rem",
            box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
            height="45rem",
            width="40%",
        ),
        rx.box(
            rx.vstack(
                rx.box(
                    create_blank_input_form("#dbffea", _rowsCount="13", _placeholder="I will remember today"),
                    height="50%",
                    width="100%",
                    background_color="#dbffea",
                    border_radius="0.5rem",
                    box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                ),
                rx.box(
                    create_blank_input_form("#ffdbdb", _rowsCount="13", _placeholder="random question"),
                    height="50%",
                    width="100%",
                    background_color="#ffdbdb",
                    border_radius="0.5rem",
                    box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                ),
                # flex_grow="1",
                border_radius="0.5rem",
                height="45rem",
            ),
            width="30%",
        ),
        rx.box(
            create_blank_input_form("#dbdbff", _rowsCount="25", _placeholder="chatbot"),
            height="720px",
            width="30%",
            background_color="#dbdbff",
            border_radius="0.5rem",
            box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        ),
        width="100%",
    )


def create_app_layout():
    """Create the overall app layout with responsive design."""
    return rx.box(
        rx.box(
            # create_calendar_header(),
            create_main_content(),
            width="100%",
            height="1440px",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding="1rem",
        ),
        background_color="#F3F4F6",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
    )


def create_app():
    """Create the complete app with styles and main content."""
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
        body {
            font-family: 'Courier', monospace;
        }        
    """
        ),
        create_app_layout(),
    )
