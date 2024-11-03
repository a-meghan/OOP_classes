class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count
    
# Create an instance
event_con = Event("Python Conference", "01-01-2025")

# Add participants
event_con.add_participant()
event_con.add_participant()
event_con.add_participant()

# See current count
print(event_con.get_participant_count())