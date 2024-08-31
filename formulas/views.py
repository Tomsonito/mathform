from django.shortcuts import render
from .models import Formula
import logging
import math

logger = logging.getLogger(__name__)


def custom_sqrt(x):
    return x ** 0.5


def home(request):
    formulas = Formula.objects.all()
    context = {
        'formulas': formulas,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about_us.html')


def links(request):
    return render(request, 'links.html')


def square_calculate(request):
    side_length = 0
    length = 0
    result = None
    action = ''

    if request.method == 'POST':
        # Получение данных из формы
        side_length_str = request.POST.get('side_length', '0')
        length_str = request.POST.get('length', '0')
        action = request.POST.get('action', '')

        # Преобразование данных в целые числа с обработкой исключений
        try:
            side_length = int(side_length_str)
        except ValueError:
            side_length = 0

        try:
            length = int(length_str)
        except ValueError:
            length = 0

        logger.debug(f"POST data: side_length={side_length}, length={length}, action={action}")

        if action == 'area':
            result = side_length ** 2
        elif action == 'perimeter':
            result = 4 * length

    return render(request, 'formulas/square_calculate.html', {
        'side_length': side_length,
        'length': length,
        'action': action,
        'result': result,
    })


def triangle_calculate(request):
    if request.method == 'POST':
        first_side_e = int(request.POST.get('first_side_e', 0))
        first_side_i = int(request.POST.get('first_side_i', 0))
        second_side_i = int(request.POST.get('second_side_i', 0))
        first_side_s = int(request.POST.get('first_side_s', 0))
        second_side_s = int(request.POST.get('second_side_s', 0))
        third_side_s = int(request.POST.get('third_side_s', 0))
        first_side_r = int(request.POST.get('first_side_r', 0))
        second_side_r = int(request.POST.get('second_side_r', 0))
        action = request.POST.get('action', '')

        logger.debug(f"POST data: first_side_i={first_side_i}, second_side_i={second_side_i}, "
                     f"first_side_s={first_side_s},"
                     f" second_side_s={second_side_s}, first_side_e={first_side_e}, "
                     f"third_side_s={third_side_s},"
                     f"first_side_r={first_side_r}, second_side_r={second_side_r},action={action}")
        result_perimeter = None
        result_area = None

        if action == 'calculate_equilateral_triangle':
            result_perimeter = 3 * first_side_e
            result_area = (custom_sqrt(3) / 4) * (first_side_e ** 2)
        elif action == 'calculate_isosceles_triangle':
            result_perimeter = 2 * first_side_i + second_side_i
            result_area = (second_side_i / 4) * custom_sqrt(4 * first_side_i ** 2 - second_side_i ** 2)
        elif action == 'calculate_scalene_triangle':
            result_perimeter = first_side_s + second_side_s + third_side_s
            s = result_perimeter / 2
            result_area = custom_sqrt(s * (s - first_side_s) * (s - second_side_s) * (s - third_side_s))
        elif action == 'calculate_right_triangle':
            hypotenuse = custom_sqrt(first_side_r ** 2 + second_side_r ** 2)
            result_perimeter = first_side_r + second_side_r + hypotenuse
            result_area = 0.5 * first_side_r * second_side_r

        return render(request, 'formulas/triangle_calculate.html', {
            'first_side_e': first_side_e,
            'first_side_i': first_side_i,
            'second_side_i': second_side_i,
            'first_side_s': first_side_s,
            'second_side_s': second_side_s,
            'third_side_s': third_side_s,
            'first_side_r': first_side_r,
            'second_side_r': second_side_r,
            'action': action,
            'result_perimeter': result_perimeter,
            'result_area': result_area
        })
    else:
        return render(request, 'formulas/triangle_calculate.html', {
            'first_side_e': 0,
            'first_side_i': 0,
            'second_side_i': 0,
            'first_side_s': 0,
            'second_side_s': 0,
            'third_side_s': 0,
            'first_side_r': 0,
            'second_side_r': 0,
            'action': None,
            'result_perimeter': None,
            'result_area': None,
        })


def calculate_circle(request):
    if request.method == 'POST':
        try:
            radius = float(request.POST.get('radius', 0))
            if radius < 0:
                raise ValueError("Radius cannot be negative.")
            circumference = 2 * math.pi * radius
            area = math.pi * (radius ** 2)
        except ValueError:
            radius = None
            circumference = None
            area = None
            error_message = "Please enter a valid non-negative number for radius."

        return render(request, 'formulas/circle_calculate.html', {
            'radius': radius,
            'circumference': circumference,
            'area': area,
            'error_message': error_message if 'error_message' in locals() else None
        })
    else:
        return render(request, 'formulas/circle_calculate.html', {
            'radius': 0,
            'circumference': None,
            'area': None,
            'error_message': None
        })