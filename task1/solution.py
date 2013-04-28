ASTRO_SIGNS = (
    (18, 'Водолей'),
    (20, 'Риби'),
    (20, 'Овен'),
    (20, 'Телец'),
    (20, 'Близнаци'),
    (21, 'Рак'),
    (22, 'Лъв'),
    (22, 'Дева'),
    (22, 'Везни'),
    (21, 'Скорпион'),
    (21, 'Стрелец'),
    (19, 'Козирог')
)


def what_is_my_sign(day, month):
    """ Return the horoscope sign according to the day and month. """
    return ASTRO_SIGNS[month - 1 - (ASTRO_SIGNS[month-2][0] >= day)][1]
