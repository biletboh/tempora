$(function () {
  var books_owl = $('#books .owl-carousel');
  books_owl.owlCarousel({
    loop:true,
    autoplay:true,
    autoplayTimeout:4500,
    autoplaySpeed:400,
    autoplayHoverPause:true,
    margin:10,
    nav:true,
    navText:["<i class='fa fa-angle-left' aria-hidden='true'></i>", "<i class='fa fa-angle-right' aria-hidden='true'></i>"],
    responsive:{
      0:{
        items:1
      },
      600:{
        items:3
      },
      1000:{
        items:4
      }
    }
  })

  var projects_owl = $('#projects .owl-carousel');
  projects_owl.owlCarousel({
    loop:true,
    autoplay:true,
    autoplayTimeout:6500,
    autoplaySpeed:1000,
    autoplayHoverPause:true,
    margin:0,
    items:1,
    nav:true,
    navText:["<i class='fa fa-angle-left' aria-hidden='true'></i>", "<i class='fa fa-angle-right' aria-hidden='true'></i>"],
  })
  function delay(element, action, time) {
    element.addClass('hidden');
    setTimeout(function() {
      element.removeClass('hidden');
      element.addClass('animated ' + action);
    }, time);
  };
  function setAnimation(item, direction) {
    var p = item.find('p');
    var button = item.find('a.btn');
    var caption = item.find('div.caption');
    var h2 = item.find('h2');
    caption.addClass(direction['position']);
    delay(h2, direction['action'], 600);
    delay(p, direction['action'], 1200);
    delay(button, direction['action'], 1800);
  }
  projects_owl.on('changed.owl.carousel', function(event) {
    var current = event.item.index;	
    var page = event.page.index + 1;

    function getDirection (page) {
      if (page%3 == 0) {
        return {position:'text-right', action:'fadeInRight'} 
      } else if ((page+1)%3 == 0) {
        return {position:'text-left', action:'fadeInLeft'} 
      } else {
        return {position:'text-center', action:'fadeInDown'}
      };
    };
    var item = $(event.target).find(".owl-item").eq(current);
    var d = getDirection(page);
    setAnimation(item, d);

  });
  // Projects owl mobile
  var projects_owl_mobile = $('#projects-mobile .owl-carousel');
  projects_owl_mobile.owlCarousel({
    loop:true,
    autoplay:true,
    autoplayTimeout:6500,
    autoplaySpeed:1000,
    autoplayHoverPause:true,
    margin:0,
    items:1,
    nav:true,
    navText:["<i class='fa fa-angle-left' aria-hidden='true'></i>", "<i class='fa fa-angle-right' aria-hidden='true'></i>"],
  })
  function delay(element, action, time) {
    element.addClass('hidden');
    setTimeout(function() {
      element.removeClass('hidden');
      element.addClass('animated ' + action);
    }, time);
  };
  function setAnimation(item, direction) {
    var p = item.find('p');
    var button = item.find('a.btn');
    var caption = item.find('div.caption');
    var h2 = item.find('h2');
    caption.addClass(direction['position']);
    delay(h2, direction['action'], 600);
    delay(p, direction['action'], 1200);
    delay(button, direction['action'], 1800);
  }
  projects_owl_mobile.on('changed.owl.carousel', function(event) {
    var current = event.item.index;	
    var page = event.page.index + 1;

    function getDirection (page) {
      if (page%3 == 0) {
        return {position:'text-right', action:'fadeInRight'} 
      } else if ((page+1)%3 == 0) {
        return {position:'text-left', action:'fadeInLeft'} 
      } else {
        return {position:'text-center', action:'fadeInDown'}
      };
    };
    var item = $(event.target).find(".owl-item").eq(current);
    var d = getDirection(page);
    setAnimation(item, d);

  });
  // Set initial animations
  //$('.first-owl-item').css('opacity', 0);

  $('.first-owl-item').waypoint(function() {
    var item = $('.first-owl-item');
    var d = {position:'text-center', action:'fadeInDown'};
    setAnimation(item, d);
  }, { offset: '50%' });
});
