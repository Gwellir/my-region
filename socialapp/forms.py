from django import forms

from socialapp.models import TripComment


class TripCommentCreateForm(forms.ModelForm):
    """
    Форма создания комментария к походу по маршруту.
    """

    photos = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = TripComment
        fields = ["trip", "content", "score", "photos"]
