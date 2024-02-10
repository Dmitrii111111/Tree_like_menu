import re
from django import template
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch
from ..models import TreeMenu

# регистрации пользовательского тега
register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = '', parent: int = 0):

    """
     если значение parent равно 0 (или не указано, так как у него есть значение по умолчанию),
     и ключ 'menu' присутствует в контексте, это означает,
     что меню уже было отрисовано и сохранено в контексте.
     В этом случае, значение menu из контекста присваивается переменной menu внутри функции draw_menu,
     чтобы использовать кэшированное меню и избежать повторной отрисовки.
    """
    # позволяет использовать кэшированное меню, если оно уже было ранее отрисовано
    if parent != 0 and 'menu' in context:
        menu = context['menu']

    else:
        # создается регулярное выражение для проверки, является ли строка URL-адресом.
        is_url = re.compile(r'^http[s]?://')

        # Получаем путь, если запрос существует
        """
        получается текущий путь (URL) из объекта запроса,
        если он существует в контексте и является экземпляром класса HttpRequest. 
        В противном случае, присваивается пустая строка.
        """
        current_path = context['request'].path \
            if 'request' in context and isinstance(context['request'], HttpRequest) \
            else ''

        """
        выполняется запрос к модели TreeMenu, чтобы получить данные элементов меню,
        относящихся к указанной категории (name).
        Результаты сортируются по полю pk
        """
        data = TreeMenu.objects.select_related()\
            .filter(category__name=name)\
            .order_by('pk')

        menu = []

        for item in data:
            path = item.path.strip()  # удаляются лишние пробелы в начале и конце строки элемента меню.
            target = '_self'  #  устанавливается значение переменной target по умолчанию равным '_self'
            # (открывать ссылку в текущем окне/вкладке)

            if is_url.match(path):  #  проверяется, является ли path URL-адресом.
                url = path  # присваивается значение path переменной url

                target = '_blank'  #  устанавливается значение переменной target равным '_blank'
                # (открывать ссылку в новом окне/вкладке), если path является URL-адресом

            else:
                try:
                    url = reverse(path)  # пытается получить URL-адрес, соответствующий path
                    # Если URL-адрес не найден, возникает исключение NoReverseMatch

                except NoReverseMatch:
                    url = path  # если возникает исключение NoReverseMatch,
                    # то присваивается значение path переменной url

            menu.append({
                'id': item.pk,
                'url': url,
                'target': target,
                'name': item.name,
                'parent': item.parent_id or 0,
                'active': True if url == current_path else False,
                # если текущий путь совпадает с URL-адресом элемента меню,
                # то значение 'active' будет True, что позволяет указать,
                # что данный элемент меню является активным.
                # В противном случае, значение 'active' будет False
            })

    return {
        'menu': menu,

        # current_menu
        # позволяет получить только те элементы меню,
        # которые являются дочерними для определенного родительского элемента.
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }
