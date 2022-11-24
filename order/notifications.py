import admin_notifications
def notification():
        return "<p>There are broken links on your site.</p>"

admin_notifications.register(notification)