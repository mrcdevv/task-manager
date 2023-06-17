from django import forms
from .models import TasksRoom, Task


class TaskRoomForm(forms.ModelForm):
    class Meta:
        model = TasksRoom
        fields = ["title", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        new_data = {
            "cols": 80,
            "rows": 5,
            "style": "resize:none;",
        }

        for field in self.fields:
            self.fields[str(field)].widget.attrs["class"] = "form-control"

        self.fields["description"].widget.attrs = new_data
