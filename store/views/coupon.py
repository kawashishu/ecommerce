from django.shortcuts import HttpResponse
from django.views import View
from store.models import Coupon


class ApplyCouponView(View):
    def post(self, request, *args, **kwargs):
        code = request.POST.get('code')
        try:
            coupon = Coupon.objects.get(code=code)
            self.request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            return HttpResponse('Coupon does not exist', status=404)
        return HttpResponse(f'Congratolations.\
                            Coupon {coupon.code} applied', status=200)


class RemoveCouponView(View):
    def post(self, *args, **kwargs):
        if 'coupon_id' in self.request.session:
            self.request.session['coupon_id'] = None
        return HttpResponse('Coupon removed', status=200)
