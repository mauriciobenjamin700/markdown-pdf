from flet import (
    Colors,
    FontWeight,
    TextAlign,
    TextField,
    TextStyle
)

from src.frontend.styles import (
    HINT_STYLE,
    LABEL_STYLE,
    TEXT_STYLE
)

class Input(TextField):
    """
    
    """
    def __init__(
        self,
        label="Input",
        helper_text="Enter text",
        hint_text="Enter text here",
        value="",
        read_only=False
    ):
        super().__init__(
            read_only=read_only,
            label=label,
            helper_text=helper_text,
            value=value,
            bgcolor=Colors.GREY_700,
            width=500,
            height=50,
            text_align=TextAlign.CENTER,
            align_label_with_hint=True,
            label_style=LABEL_STYLE,
            text_style=TEXT_STYLE,
            hint_text=hint_text,
            hint_style=HINT_STYLE,
        )

    def get(self):
        """
        Get the current value of the input field.

        Args:
            None

        Returns:
            str: The current value of the input field.
        """
        return self.value
    
    def set(self, value: str):
        """
        Set the value of the input field.

        Args:
            value (str): The new value to set for the input field.
        
        Returns:
            None
        """
        self.value = value
        self.update()

    def clear(self):
        """
        Clear the value of the input field.

        Args:
            None

        Returns:
            None
        """
        self.value = ""
        self.update()

    def enable(self):
        """
        Enable the input field.

        Args:
            None

        Returns:
            None
        """
        self.read_only = False
        self.update()

    def disable(self):
        """
        Disable the input field.

        Args:
            None

        Returns:
            None
        """
        self.read_only = True
        self.update()