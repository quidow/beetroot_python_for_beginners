"""
1. Напишите функцию draw_tag которая вернет указанный html тег и его атрибуты 
например

print(draw_tag(name="a", inner="google link", href="http://google.com",
                                                       target="_blank")) 
               
вернет

<a href="http://google.com" target="_blank">google link</a>

а такой вызов

print(draw_tag(name="span", inner="my text")) вернет <span>my text</span>

и так далее. Мы не знаем наперед все теги так что не пытайтесь делать ифами

2. Напишите цикл который позволит собирать значения для функции 
(атрибут - значение), прерывается по "q" и вызывает вышеописанную функцию. 
(да тут надо будет поискать про unpack arguments)
"""

def draw_tag(name="", inner="", **kwargs):
    tag_str = f"<{name}"
    for key, elem in kwargs.items():
        tag_str += f" {key}=\"{elem}\""
    tag_str += f">{inner}</{name}>"
    return tag_str


tag_name = input("enter tag name: ")
tag_inner = input("enter tag inner: ")
print("you can add various attributes")
print("if you are enough, enter \"q\"")
attributes = {}

while True:
    attr_name = input("enter attribute name: ")
    if attr_name in ("q", "Q"):
        print(draw_tag(name=tag_name, inner=tag_inner, **attributes))
        break
    attr_value = input("enter attribute value: ")
    if attr_value in ("q", "Q"):
        attributes[attr_name] = ""
        print(draw_tag(name=tag_name, inner=tag_inner, **attributes))
        break
    else:
        attributes[attr_name] = attr_value
