class LogisticsServices:
    @staticmethod
    def services(self,number_of_successful_delivery):
        wages_per_day = 0
        base_pay = 5000
        if 0 < number_of_successful_delivery < 50:
            amount_per_parcel = 160
            wages_per_day = number_of_successful_delivery * amount_per_parcel + base_pay
        return wages_per_day


