def services(number_of_successful_delivery):
    base_pay = 5000
    wages_per_day = 0
    if 0 < number_of_successful_delivery < 50:
        amount_per_parcel = 160
        wages_per_day = number_of_successful_delivery * amount_per_parcel + base_pay

    elif 50 <= number_of_successful_delivery <= 59:
        amount_per_parcel = 200
        wages_per_day = number_of_successful_delivery * amount_per_parcel + base_pay

    elif 60 <= number_of_successful_delivery <= 69:
        amount_per_parcel = 250
        wages_per_day = number_of_successful_delivery * amount_per_parcel + base_pay
    elif number_of_successful_delivery >= 70:
        amount_per_parcel = 500
        wages_per_day = number_of_successful_delivery * amount_per_parcel + base_pay
    if 0 > number_of_successful_delivery > 100:
        raise ValueError("Invalid number of successful delivery")
    return wages_per_day
