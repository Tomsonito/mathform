from django.test import TestCase
import math
import logging
from django.shortcuts import render
logger = logging.getLogger(__name__)

def triangle_calculate(request):
    if request.method == 'POST':
        first_side = int(request.POST.get('first_side',))
        second_side = int(request.POST.get('second_side',))
        third_side = int(request.POST.get('third_side'))
        action = request.POST.get('action', '')

        logger.debug(f"POST data: first_side={first_side}, second_side={second_side},third_side={third_side}, action={action}")
        result_perimeter = None
        result_area = None

        if action == 'calculate_equilateral_triangle':
            result_perimeter = 3 * first_side
            result_area = (math.sqrt(3) / 4) * (first_side ** 2)
        elif action == 'calculate_isosceles_triangle':
            result_perimeter = 2 * first_side + second_side
            result_area = (second_side / 4) * math.sqrt(4 * first_side ** 2 - second_side ** 2)
        elif action == 'calculate_scalene_triangle':
            result_perimeter = first_side + second_side + third_side
            s = result_perimeter / 2
            result_area = math.sqrt(s * (s - first_side) * (s - second_side) * (s - third_side))
        elif action == 'calculate_right_triangle':
            hypotenuse = math.sqrt(first_side ** 2 + second_side ** 2)
            result_perimeter = first_side + second_side + hypotenuse
            result_area = 0.5 * first_side * second_side

        return render(request, 'formulas/triangle_calculate.html', {
            'first_side': first_side,
            'second_side': second_side,
            'third_side': third_side,
            'action': action,
            'result_perimeter': result_perimeter,
            'result_area': result_area
        })
    else:
        return render(request, 'formulas/triangle_calculate.html', {
            'first_side': 0,
            'second_side': 0,
            'third_side': 0,
            'result_perimeter': None,
            'result_area': None
        })

