#class Reminders:
#   

class Daily:
    log_dir = Settings.daily_logdir

    def __init__(self, date):
        self.date = date  # yyyy, mm, dd (tuple)
        self.log = Daily.log_dir + '/' + (Settings.daily_logfmt % self.date[0:3]) + '.' + Settings.daily_logext

        self.events = Daily.readDate(self.date)
        self.daily_log = Daily.parseLog(self.events)
        self.rem_completed, self.rem_pending = Daily.parseReminders(self.events)


