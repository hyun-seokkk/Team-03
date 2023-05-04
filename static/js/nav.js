$(window).scroll(function() {
  var headerHeight = $('#header1').outerHeight();
  var boxBottom = $('#box').offset().top + $('#box').outerHeight();
  var scrollPosition = $(window).scrollTop();
  var triggerPoint = boxBottom - headerHeight;

  if (scrollPosition >= triggerPoint) {
    $('#header1').hide();
    $('#header2').show().addClass('fixed-top');
  } else {
    $('#header1').show();
    $('#header2').hide().removeClass('fixed-top');
  }

  if (scrollPosition + $(window).height() >= $(document).height() - headerHeight) {
    $('#header1').show();
  }
});