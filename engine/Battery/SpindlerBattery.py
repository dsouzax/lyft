

class SpindlerBattery():
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date

    # def engine_should_be_serviced(self):
    #     return self.current_mileage - self.last_service_mileage > 30000

    def needs_service(self):
        return self.current_date - self.last_service_date > 2