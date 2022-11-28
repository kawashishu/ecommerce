<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
 (function ($) {
     "use strict";
    
    //   Dropdown on mouse hover
     $(document).ready(function () {
         function toggleNavbarMethod() {
             if ($(window).width() > 992) {
                 $('.navbar .dropdown').on('mouseover', function () {
                     $('.dropdown-toggle', this).trigger('click');
                 }).on('mouseout', function () {
                     $('.dropdown-toggle', this).trigger('click').blur();
                 });
             } else {
                 $('.navbar .dropdown').off('mouseover').off('mouseout');
             }
         }
         toggleNavbarMethod();
         $(window).resize(toggleNavbarMethod);
     });
    
    
    //   Back to top button
     $(window).scroll(function () {
         if ($(this).scrollTop() > 100) {
             $('.back-to-top').fadeIn('slow');
         } else {
             $('.back-to-top').fadeOut('slow');
         }
     });
     $('.back-to-top').click(function () {
         $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
         return false;
     });


    //   Vendor carousel
     $('.vendor-carousel').owlCarousel({
         loop: true,
         margin: 29,
         nav: false,
         autoplay: true,
         smartSpeed: 1000,
         responsive: {
             0:{
                 items:2
             },
             576:{
                 items:3
             },
             768:{
                 items:4
             },
             992:{
                 items:5
             },
             1200:{
                 items:6
             }
         }
     });


    //   Related carousel
     $('.related-carousel').owlCarousel({
         loop: true,
         margin: 29,
         nav: false,
         autoplay: true,
         smartSpeed: 1000,
         responsive: {
             0:{
                 items:1
             },
             576:{
                 items:2
             },
             768:{
                 items:3
             },
             992:{
                 items:4
             }
         }
     });

    //   Product Quantity
    var toastTrigger = document.getElementById('liveToastBtn')
    var toastLiveExample = document.getElementById('liveToast')
    if (toastTrigger) {
      toastTrigger.addEventListener('click', function () {
        var toast = new bootstrap.Toast(toastLiveExample)
    
        toast.show()
      })
    }
     
    // Cart
        
    //  ajax call 
     
 })(jQuery);

function removeCart(id){
    const object = event.target
    
    $.ajax({
      url:  "{% url 'cart-list' %}",
      type: 'POST',
        data: {
            'id': id,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
      success: function(response){
        $(object).closest('tr').remove()
        $('.total').html(response)
        $('.sumtotal').html(response)
      }
    })
  }

  function add(id){
    const object = event.target
    $.ajax({
      url:  "{% url 'btn' %}",
      type: 'POST',
        data: {
            'id': id,
            'btn': object.className,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
      success: function(total){
        $('.total').html(total)
        var total = parseInt(total) + 10
        $('.sumtotal').html(total)
        
        if ( object.className == "fa fa-plus") {
            object.closest('td').querySelector('.countInput').value = parseInt(object.closest('td').querySelector('.countInput').value) + 1
        }
        else {
            object.closest('td').querySelector('.countInput').value = parseInt(object.closest('td').querySelector('.countInput').value) - 1
        }
      }
 })
}


