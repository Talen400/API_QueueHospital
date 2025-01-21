class Patient:
    def __init__(self, name, age, urgency):
        self.name = name
        self.age = age
        self.urgency = urgency

class HospitalQueue:
    def __init__(self):
        # Initializes the patient queue, which is a dict with 3 lists
        # for each urgency level
        self.queue = {"high": [], "medium": [], "low": []}

    def add_patient(self, patient):
        # Adds patients to the queue according to their urgency level
        for p in self.queue[patient.urgency]:
            if p.name == patient.name and p.age == patient.age and p.urgency == patient.urgency:
                return

        self.queue[patient.urgency].append(patient)

        self.queue[patient.urgency].sort(key=lambda p: p.age, reverse=True)

    def display_queue(self):
        """
        Displays the queue organized by urgency level and age.
        """
        formatted_queue = {}

        for urgency in ["high", "medium", "low"]:
            if urgency in self.queue:
                patients = [{"name": patient.name, "age": patient.age} for patient in self.queue[urgency]]
                formatted_queue[urgency] = patients

        return formatted_queue  # Blank line between urgency categories

    def next_patient(self):
        """
        Removes and returns the next patient in the order of attendance.
        """
        for urgency in ["high", "medium", "low"]:
            if self.queue[urgency]:  # Checks if there are patients in the urgency level
                next_patient = self.queue[urgency].pop(0)
                return {"name": next_patient.name, "age": next_patient.age}

        # Another good practice: checks if the list is empty and returns a message "The queue is empty"
        raise IndexError("The queue is empty.")
