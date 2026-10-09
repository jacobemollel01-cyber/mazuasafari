
import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import SafariInquiryForm, ContactMessageForm


logger = logging.getLogger(__name__)


def send_inquiry_notification(inquiry, inquiry_type):
    """
    Notify Mazua Safaris about a saved booking or contact inquiry.

    An email failure must not undo the saved inquiry.
    """

    recipient = getattr(
        settings,
        "ADMIN_NOTIFICATION_EMAIL",
        "mazuarobert@gmail.com",
    )

    subject = (
        f"New Mazua Safaris {inquiry_type} "
        f"from {inquiry.full_name}"
    )

    fields = [
        ("Name", "full_name"),
        ("Customer email", "email"),
        ("Country", "country"),
        ("Phone", "phone"),
        ("Number of travellers", "travellers"),
        ("Number of days", "days"),
        ("Arrival date", "arrival"),
        ("Departure date", "departure"),
        ("Destination", "destination"),
        ("Accommodation", "accommodation"),
        ("Budget", "budget"),
        ("Message / special requests", "requests"),
    ]

    lines = [
        f"New {inquiry_type} received on the Mazua Safaris website.",
        "",
    ]

    for label, field_name in fields:
        value = getattr(inquiry, field_name, None)

        if value not in (None, ""):
            lines.append(f"{label}: {value}")

    lines.extend([
        "",
        "This inquiry has been saved in the website database.",
        "You can review it in the Django admin panel.",
        "",
        "To reply, use the customer's email address shown above.",
    ])

    try:
        sent_count = send_mail(
            subject=subject,
            message="\n".join(lines),
            from_email=None,
            recipient_list=[recipient],
            fail_silently=False,
        )

        if sent_count == 1:
            logger.info(
                "Email notification accepted by backend: "
                "type=%s recipient=%s",
                inquiry_type,
                recipient,
            )
            print(
                f"EMAIL NOTIFICATION ACCEPTED: "
                f"{inquiry_type} -> {recipient}"
            )
        else:
            logger.warning(
                "Email backend did not accept notification: "
                "type=%s recipient=%s",
                inquiry_type,
                recipient,
            )
            print(
                f"EMAIL NOTIFICATION NOT SENT: {inquiry_type}"
            )

    except Exception:
        logger.exception(
            "Failed to send %s notification to %s",
            inquiry_type,
            recipient,
        )
        print(
            f"EMAIL NOTIFICATION FAILED: {inquiry_type}. "
            "Check the server output for details."
        )


def home(request):
    if request.method == "POST":
        form = SafariInquiryForm(request.POST)

        if form.is_valid():
            inquiry = form.save()

            send_inquiry_notification(
                inquiry,
                "safari booking inquiry",
            )

            messages.success(
                request,
                "Thank you! Your safari inquiry has been received. "
                "Our team will get back to you shortly.",
            )

            return redirect("home")

        messages.error(
            request,
            "Please correct the highlighted errors below.",
        )

        return render(
            request,
            "website/home.html",
            {
                "form": form,
                "show_booking_errors": True,
            },
        )

    form = SafariInquiryForm()

    return render(
        request,
        "website/home.html",
        {"form": form},
    )


def about(request):
    return render(request, "website/about.html")


def safaris(request):
    return render(request, "website/safaris.html")


def destinations(request):
    return render(request, "website/destinations.html")


def packages(request):
    return render(request, "website/packages.html")


def gallery(request):
    return render(request, "website/gallery.html")


def contact(request):
    if request.method == "POST":
        contact_form = ContactMessageForm(request.POST)

        if contact_form.is_valid():
            inquiry = contact_form.save()

            send_inquiry_notification(
                inquiry,
                "contact inquiry",
            )

            messages.success(
                request,
                "Thank you for contacting Mazua Safaris! "
                "Your message has been received. "
                "Our team will get back to you soon.",
            )

            return redirect("contact")

        messages.error(
            request,
            "Please correct the highlighted errors below.",
        )

    else:
        contact_form = ContactMessageForm()

    return render(
        request,
        "website/contact.html",
        {
            "contact_form": contact_form,
            "show_contact_errors": (
                request.method == "POST"
                and not contact_form.is_valid()
            ),
        },
    )