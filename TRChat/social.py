from django.http import HttpResponse


def save_profile(backend, user, response, *args, **kwargs):
    """
    Обработчик для социальных профилей во время успешной авторизации
    """
    print(backend, user, response)  # изучаем что нам пришло


def oauth2login_view(request, **kwargs):
    """
    Вьюха после социальной авторизации
    В современных условиях - закрыть нахуй новую вкладку (в ней же открывать авторизацию)
    И через js просигналить на основной пейдж о изменениях
    (<social.backends.vk.VKOAuth2 object at 0x7f844805e1d0>, None,
    {u'first_name': u'Ivan', u'last_name': u'Maslov', u'user_id': 215944181,
    u'uid': 215944181, u'access_token':
    u'huypizdatoken',
    u'photo': u'https://pp.vk.me/c620218/v620218181/fe40/8s1p8CToXC0.jpg', u'expires_in': 86399,
    'user_photo': u'https://pp.vk.me/c620218/v620218181/fe40/8s1p8CToXC0.jpg', u'nickname': u'',
    u'screen_name': u'dr.tranquility'})
    :param request:
    :param kwargs:
    :return:
    """
    return HttpResponse('<html><body><script>window.close();</script>please wait for authenticate...</body></html>')