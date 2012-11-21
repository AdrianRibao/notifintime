# -*- coding: utf-8 -*-
from notifintime.backends.base import NotificationBackendBase
from django.core.mail import EmailMultiAlternatives
from django.template import Context, loader
import html2text
import json
#from django.template.loader import get_template


class EmailBackend(NotificationBackendBase):
    name = 'email'

    def __init__(self, subject, template_name, *args, **kwargs):
        super(EmailBackend, self).__init__(*args, **kwargs)
        self.subject = subject
        self.template_name = template_name

    def render_template_email(self, data):
        template = loader.get_template(self.template_name)
        json_data = json.loads(data)[0]
        #import pdb
        #pdb.set_trace()
        render = template.render(Context(json_data))
        return render

    def convert_email_to_text(self, html):
        h = html2text.HTML2Text()
        #h.ignore_links = True
        #h.inline_links = True
        text = h.handle(html)
        return text

    def send(self, data, *args, **kwargs):
        """
        Sends an email with data as a context for the template.
        """
        recipients = kwargs.get('to', [])
        html_content = self.render_template_email(data)
        text_content = self.convert_email_to_text(html_content)
        msg = EmailMultiAlternatives(
                subject=self.subject,
                body=text_content,
                to=recipients)
        msg.attach_alternative(html_content, "text/html")

        msg.send()

    def subscribe(self, channel):
        """
        Subscribe the backend to a channel.

        Returns the list of channels subscribed
        """
        pass

