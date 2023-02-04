from django.shortcuts import HttpResponse, redirect
from django.views import View
from store.models import Coupon



def apply_coupon(request, pk):
        try:
            coupon = Coupon.objects.get(id=pk)
            request.session['coupon_id'] = int(coupon.id)
        except Coupon.DoesNotExist:
            return redirect('checkout', status=404)
        return redirect('checkout')



def remove_coupon(request):
        try:
            request.session['coupon_id'] = None
        except Coupon.DoesNotExist:
            return redirect('checkout', status=404)
        return redirect('checkout')
