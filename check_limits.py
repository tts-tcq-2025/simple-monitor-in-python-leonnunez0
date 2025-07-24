def battery_is_ok(temperature, soc, charge_rate):
    isTempOk = is_within_range(temperature, 0, 45)
    isSocOk = is_within_range(soc, 20, 80)
    isChargeRateOk = is_within_limt(charge_rate, 0.8)

    if not isTempOk:
        print('Temperature is out of range!')
    if not isSocOk:
        print('State of Charge is out of range!')
    if not isChargeRateOk:
        print('Charge rate is out of range!')
    return isTempOk and isChargeRateOk and isSocOk


def is_within_range(val, lower_limit, upper_limit):
    return lower_limit < val and is_within_limt(val, upper_limit)


def is_within_limt(val, limit):
    return val < limit


if __name__ == '__main__':
    assert (battery_is_ok(25, 70, 0.7) is True)
    assert (battery_is_ok(50, 85, 0) is False)
