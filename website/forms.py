
from django import forms
from django.utils import timezone

from .models import SafariInquiry, ContactMessage


class SafariInquiryForm(forms.ModelForm):
    class Meta:
        model = SafariInquiry
        fields = [
            "full_name",
            "email",
            "country",
            "phone",
            "travellers",
            "days",
            "arrival",
            "departure",
            "destination",
            "accommodation",
            "budget",
            "requests",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Your full name",
                "autocomplete": "name",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }),
            "country": forms.TextInput(attrs={
                "placeholder": "Your country",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Your phone number",
                "autocomplete": "tel",
            }),
            "travellers": forms.NumberInput(attrs={
                "min": 1,
                "max": 100,
            }),
            "days": forms.NumberInput(attrs={
                "min": 1,
                "max": 365,
            }),
            "arrival": forms.DateInput(attrs={
                "type": "date",
            }),
            "departure": forms.DateInput(attrs={
                "type": "date",
            }),
            "destination": forms.TextInput(attrs={
                "placeholder": "e.g. Serengeti, Zanzibar",
            }),
            "accommodation": forms.TextInput(attrs={
                "placeholder": "e.g. Lodge, hotel, camping",
            }),
            "budget": forms.TextInput(attrs={
                "placeholder": "Your approximate budget",
            }),
            "requests": forms.Textarea(attrs={
                "placeholder": "Tell us about your safari plans",
                "rows": 4,
            }),
        }

    def clean_full_name(self):
        name = self.cleaned_data["full_name"].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "Please enter your full name."
            )

        return name

    def clean_travellers(self):
        travellers = self.cleaned_data["travellers"]

        if travellers < 1 or travellers > 100:
            raise forms.ValidationError(
                "Travellers must be between 1 and 100."
            )

        return travellers

    def clean_days(self):
        days = self.cleaned_data.get("days")

        if days is not None and not 1 <= days <= 365:
            raise forms.ValidationError(
                "Safari duration must be between 1 and 365 days."
            )

        return days

    def clean(self):
        cleaned_data = super().clean()

        arrival = cleaned_data.get("arrival")
        departure = cleaned_data.get("departure")
        today = timezone.localdate()

        if arrival and arrival < today:
            self.add_error(
                "arrival",
                "Arrival date cannot be in the past."
            )

        if departure and departure < today:
            self.add_error(
                "departure",
                "Departure date cannot be in the past."
            )

        if arrival and departure and departure <= arrival:
            self.add_error(
                "departure",
                "Departure must be after the arrival date."
            )

        return cleaned_data


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage

        fields = [
            "full_name",
            "email",
            "country",
            "phone",
            "travellers",
            "days",
            "arrival",
            "departure",
            "destination",
            "accommodation",
            "budget",
            "requests",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "id": "contact-name",
                "placeholder": "Your full name",
                "autocomplete": "name",
            }),
            "email": forms.EmailInput(attrs={
                "id": "contact-email",
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }),
            "country": forms.TextInput(attrs={
                "id": "contact-country",
                "placeholder": "Your country",
                "autocomplete": "country-name",
            }),
            "phone": forms.TextInput(attrs={
                "id": "contact-phone",
                "placeholder": "+255...",
                "autocomplete": "tel",
            }),
            "travellers": forms.NumberInput(attrs={
                "id": "contact-travellers",
                "min": 1,
                "max": 100,
                "placeholder": "e.g. 2",
            }),
            "days": forms.NumberInput(attrs={
                "id": "contact-days",
                "min": 1,
                "max": 365,
                "placeholder": "e.g. 7",
            }),
            "arrival": forms.DateInput(attrs={
                "id": "contact-arrival",
                "type": "date",
            }),
            "departure": forms.DateInput(attrs={
                "id": "contact-departure",
                "type": "date",
            }),
            "destination": forms.Select(
                attrs={
                    "id": "contact-destination",
                },
                choices=[
                    ("", "Select destination"),
                    ("Northern Tanzania", "Northern Tanzania"),
                    ("Southern Tanzania", "Southern Tanzania"),
                    ("Zanzibar", "Zanzibar"),
                    ("Safari and Zanzibar", "Safari & Zanzibar"),
                    ("Custom", "Custom Journey"),
                ],
            ),
            "accommodation": forms.Select(
                attrs={
                    "id": "contact-accommodation",
                },
                choices=[
                    ("", "Select preference"),
                    ("Budget", "Budget"),
                    ("Mid-range", "Mid-range"),
                    ("Luxury", "Luxury"),
                    ("Not sure", "Not sure yet"),
                ],
            ),
            "budget": forms.TextInput(attrs={
                "id": "contact-budget",
                "placeholder": "e.g. USD 2,000 per person",
            }),
            "requests": forms.Textarea(attrs={
                "id": "contact-requests",
                "rows": 5,
                "placeholder": (
                    "Tell us about your travel plans "
                    "or ask us a question..."
                ),
            }),
        }

    def clean_full_name(self):
        name = self.cleaned_data["full_name"].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "Please enter your full name."
            )

        return name

    def clean_travellers(self):
        travellers = self.cleaned_data.get("travellers")

        if travellers is not None and not 1 <= travellers <= 100:
            raise forms.ValidationError(
                "Enter between 1 and 100 travellers."
            )

        return travellers

    def clean_days(self):
        days = self.cleaned_data.get("days")

        if days is not None and not 1 <= days <= 365:
            raise forms.ValidationError(
                "Enter a duration between 1 and 365 days."
            )

        return days

    def clean(self):
        cleaned_data = super().clean()

        arrival = cleaned_data.get("arrival")
        departure = cleaned_data.get("departure")
        today = timezone.localdate()

        if arrival and arrival < today:
            self.add_error(
                "arrival",
                "Arrival date cannot be in the past."
            )

        if departure and departure < today:
            self.add_error(
                "departure",
                "Departure date cannot be in the past."
            )

        if arrival and departure and departure <= arrival:
            self.add_error(
                "departure",
                "Departure must be after the arrival date."
            )

        return cleaned_data