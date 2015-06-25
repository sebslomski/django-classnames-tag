from django.shortcuts import render


def test(request):
    return render(request, 'test.html', {
        'percentage': 20,
        'important': True
    })
